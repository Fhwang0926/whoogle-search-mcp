# Whoogle Search MCP

[![Docker Hub](https://img.shields.io/badge/Docker-hdh0926%2Fwhoogle--search--mcp-blue)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp)
[![Docker Version](https://img.shields.io/docker/v/hdh0926/whoogle-search-mcp?sort=semver)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp/tags)
[![Docker Pulls](https://img.shields.io/docker/pulls/hdh0926/whoogle-search-mcp)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp)
[![Image Size (latest)](https://img.shields.io/docker/image-size/hdh0926/whoogle-search-mcp/latest)](https://hub.docker.com/r/hdh0926/whoogle-search-mcp/tags)
[![Build and Push (Release Only)](https://github.com/Fhwang0926/whoogle-search-mcp/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Fhwang0926/whoogle-search-mcp/actions/workflows/docker-build.yml)

专为Open WebUI集成而设计的Whoogle搜索引擎FastAPI搜索代理服务器。

## 概述

本项目是为Open WebUI和其他AI聊天应用程序需要搜索功能时设计的Whoogle搜索引擎REST API包装器。它将搜索结果标准化为一致的格式，并提供与Open WebUI搜索功能无缝集成的简洁API接口。

### Open WebUI集成

此服务作为Open WebUI的**搜索代理**，使用户能够：
- 通过Whoogle（注重隐私的Google搜索替代方案）执行网络搜索
- 在AI对话中接收实时搜索结果
- 在访问网络信息的同时保持隐私
- 在不向Google暴露个人数据的情况下使用搜索功能

## 主要功能

- 🔍 **Open WebUI集成**: 作为搜索工具与Open WebUI无缝集成
- 🚀 **FastAPI后端**: 高性能异步Web框架
- 📊 **标准化结果**: 与AI聊天界面兼容的一致JSON响应格式
- 🔒 **隐私优先**: 使用Whoogle（注重隐私的Google搜索替代方案）
- 🐳 **Docker支持**: 通过Docker和Docker Compose轻松部署
- ⚙️ **可配置**: 基于环境的灵活部署配置
- 🌐 **实时搜索**: 在AI对话中提供实时网络搜索结果

## API端点

### GET /search

通过Whoogle执行搜索查询并返回标准化结果。

**参数:**
- `q` 或 `query`: 搜索查询字符串（必需）

**响应格式:**
```json
{
  "query": "搜索词",
  "number_of_results": 10,
  "results": [
    {
      "url": "https://example.com",
      "title": "示例标题",
      "content": "示例描述",
      "img_src": "https://example.com/image.jpg",
      "engine": "whoogle",
      "category": "general"
    }
  ],
  "answers": [],
  "infoboxes": []
}
```

## 安装

### 使用预构建的Docker镜像（推荐）

最新的Docker镜像在所有版本中自动构建并推送到Docker Hub：

```bash
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 your-username/whoogle-search-mcp:latest
```

### 从源码构建

1. 克隆仓库：
```bash
git clone https://github.com/your-username/whoogle-search-mcp.git
cd whoogle-search-mcp
```

2. 使用Docker构建和运行：
```bash
docker build -t whoogle-search-mcp .
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 whoogle-search-mcp
```

### 本地开发

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 设置环境变量：
```bash
export WHOOGLE_BASE_URL=http://localhost:5000
```

3. 运行应用程序：
```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Open WebUI配置

### 在Open WebUI中配置搜索代理

1. **在Docker或本地部署此服务**
2. **配置Open WebUI使用此服务作为搜索代理**：
   - 转到Open WebUI设置
   - 转到"工具"或"搜索"部分
   - 使用以下配置添加新的搜索工具：
     - **名称**: Whoogle搜索
     - **URL**: `http://your-server:8080/search`
     - **方法**: GET
     - **参数**: `q`（查询参数）

### 环境变量

- `WHOOGLE_BASE_URL`: Whoogle实例的URL（默认: `http://whoogle:5000`）

### 配置文件

将`env.sample`复制为`.env`并根据需要修改值：

```bash
cp env.sample .env
```

`env.sample`文件内容：
```bash
# Whoogle Search MCP Server Configuration

# Whoogle server url
# 默认: http://whoogle:5000
WHOOGLE_BASE_URL=http://whoogle:5000

# 示例:
# WHOOGLE_BASE_URL=http://localhost:5000
# WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### 配置示例

```bash
# 本地开发
WHOOGLE_BASE_URL=http://localhost:5000

# 生产环境
WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### Docker Compose示例（与Open WebUI一起）

```yaml
version: '3.8'
services:
  whoogle-search-mcp:
    image: your-username/whoogle-search-mcp:latest
    ports:
      - "8080:8080"
    environment:
      - WHOOGLE_BASE_URL=http://whoogle:5000
    depends_on:
      - whoogle

  whoogle:
    image: benbusby/whoogle-search:latest
    ports:
      - "5000:5000"

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OPENAI_API_BASE_URL=http://your-llm-server:8000/v1
```

## 使用示例

### 基本搜索
```bash
curl "http://localhost:8080/search?q=Python编程"
```

### 使用查询参数
```bash
curl "http://localhost:8080/search?query=机器学习"
```

## 开发

### 项目结构
```
whoogle-search-mcp/
├── app.py                    # 主FastAPI应用程序
├── requirements.txt          # Python依赖
├── Dockerfile               # Docker配置
├── env.sample               # 环境变量模板
├── README.md                # 英文文档
├── README.ko.md             # 韩文文档
├── README.ja.md             # 日文文档
├── README.zh.md             # 中文文档
├── LICENSE                  # MIT许可证
└── .github/
    └── workflows/
        └── docker-build.yml # Docker Hub的GitHub Actions
```

### 依赖
- **FastAPI**: 构建API的Web框架
- **httpx**: 向Whoogle发送请求的异步HTTP客户端
- **uvicorn**: 运行应用程序的ASGI服务器

### CI/CD管道
- **GitHub Actions**: 自动构建和推送Docker镜像到Docker Hub
- **多平台支持**: 为linux/amd64和linux/arm64架构构建
- **自动标记**: 为分支、版本和最新版本创建标签

## 许可证

此项目在MIT许可证下。详细信息请参阅[LICENSE](LICENSE)文件。

## 贡献

1. Fork仓库
2. 创建功能分支
3. 应用更改
4. 提交拉取请求

## 要求

- Python 3.11+
- 访问运行中的Whoogle实例
- Docker（可选，用于容器化部署）
