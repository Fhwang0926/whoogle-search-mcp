
FROM python:3.11-slim
RUN pip install --no-cache-dir fastapi uvicorn httpx
WORKDIR /app
COPY app.py /app/app.py
EXPOSE 8080
ENV WHOOGLE_BASE_URL=http://172.17.0.1:3006
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8080"]