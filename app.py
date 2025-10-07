from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import httpx, os

WHOOGLE = os.getenv("WHOOGLE_BASE_URL", "http://whoogle:5000")
app = FastAPI()

def map_item(it):
    # Whoogle 결과 키 보정: href/url -> url, text/description -> content
    url = it.get("url") or it.get("href") or it.get("link")
    title = it.get("title") or it.get("header") or ""
    content = it.get("text") or it.get("description") or it.get("snippet") or ""
    img = it.get("img") or it.get("img_src") or None
    return {
        "url": url, "title": title, "content": content,
        "img_src": img, "engine": "whoogle", "category": "general"
    }

@app.get("/search")
async def search(request: Request):
    params = dict(request.query_params)
    q = params.get("q") or params.get("query")
    if not q:
        raise HTTPException(400, "missing q")

    # Whoogle에 전달: format=json 강제
    params["q"] = q
    params["format"] = "json"

    async with httpx.AsyncClient(timeout=15) as cli:
        r = await cli.get(f"{WHOOGLE}/search", params=params, headers={"Accept":"application/json"})
    if r.status_code != 200:
        raise HTTPException(r.status_code, r.text)

    data = r.json() if r.headers.get("content-type","").startswith("application/json") else None
    if not isinstance(data, dict) or "results" not in data:
        raise HTTPException(502, "unexpected whoogle response")

    items = [map_item(x) for x in (data.get("results") or []) if (x.get("url") or x.get("href"))]
    out = {
        "query": q,
        "number_of_results": len(items),
        "results": items,
        "answers": [],
        "infoboxes": []
    }
    return JSONResponse(out)