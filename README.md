# Whoogle Search MCP

A FastAPI-based search proxy server that integrates with Whoogle search engine for AI chat applications, specifically designed for Open WebUI integration.

## Overview

This project provides a REST API wrapper around Whoogle search engine, designed to be used as a proxy service for Open WebUI and other AI chat applications that require search functionality. It normalizes search results into a consistent format and provides a clean API interface that seamlessly integrates with Open WebUI's search capabilities.

### Open WebUI Integration

This service acts as a **search proxy** for Open WebUI, enabling users to:
- Perform web searches through Whoogle (privacy-focused Google search alternative)
- Get real-time search results in their AI conversations
- Maintain privacy while accessing web information
- Use search functionality without exposing personal data to Google

## Features

- 🔍 **Open WebUI Integration**: Seamlessly integrates with Open WebUI as a search tool
- 🚀 **FastAPI Backend**: High-performance async web framework
- 📊 **Normalized Results**: Consistent JSON response format compatible with AI chat interfaces
- 🔒 **Privacy-Focused**: Uses Whoogle (privacy-focused Google search alternative)
- 🐳 **Docker Support**: Easy deployment with Docker and Docker Compose
- ⚙️ **Configurable**: Environment-based configuration for flexible deployment
- 🌐 **Real-time Search**: Provides live web search results in AI conversations

## API Endpoints

### GET /search

Performs a search query through Whoogle and returns normalized results.

**Parameters:**
- `q` or `query`: Search query string (required)

**Response Format:**
```json
{
  "query": "search term",
  "number_of_results": 10,
  "results": [
    {
      "url": "https://example.com",
      "title": "Example Title",
      "content": "Example description",
      "img_src": "https://example.com/image.jpg",
      "engine": "whoogle",
      "category": "general"
    }
  ],
  "answers": [],
  "infoboxes": []
}
```

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/your-username/whoogle-search-mcp.git
cd whoogle-search-mcp
```

2. Build and run with Docker:
```bash
docker build -t whoogle-search-mcp .
docker run -p 8080:8080 -e WHOOGLE_BASE_URL=http://your-whoogle-instance:5000 whoogle-search-mcp
```

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export WHOOGLE_BASE_URL=http://localhost:5000
```

3. Run the application:
```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Open WebUI Configuration

### Setting up Search Proxy in Open WebUI

1. **Deploy this service** using Docker or locally
2. **Configure Open WebUI** to use this service as a search proxy:
   - Go to Open WebUI Settings
   - Navigate to "Tools" or "Search" section
   - Add a new search tool with the following configuration:
     - **Name**: Whoogle Search
     - **URL**: `http://your-server:8080/search`
     - **Method**: GET
     - **Parameters**: `q` (query parameter)

### Environment Variables

- `WHOOGLE_BASE_URL`: URL of your Whoogle instance (default: `http://whoogle:5000`)

### Example Configuration

```bash
# For local development
WHOOGLE_BASE_URL=http://localhost:5000

# For production
WHOOGLE_BASE_URL=https://your-whoogle-instance.com
```

### Docker Compose Example (with Open WebUI)

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

## Usage Examples

### Basic Search
```bash
curl "http://localhost:8080/search?q=python programming"
```

### With Query Parameter
```bash
curl "http://localhost:8080/search?query=machine learning"
```

## Development

### Project Structure
```
whoogle-search-mcp/
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # This file
└── LICENSE            # MIT License
```

### Dependencies
- **FastAPI**: Web framework for building APIs
- **httpx**: Async HTTP client for making requests to Whoogle
- **uvicorn**: ASGI server for running the application

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Requirements

- Python 3.11+
- Access to a running Whoogle instance
- Docker (optional, for containerized deployment)
