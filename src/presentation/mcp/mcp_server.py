from fastmcp import FastMCP
import json
import os

mcp_port = int(os.getenv("MCP_PORT", 8001))
mcp = FastMCP("Globo News MCP 📰", port=mcp_port)

@mcp.tool()
def get_news() -> str:
    """Get a hardcoded news article as JSON string"""
    news_data = {
        "id": 1,
        "title": "Nova tecnologia revoluciona mercado brasileiro",
        "content": "Uma inovadora tecnologia desenvolvida por pesquisadores brasileiros está transformando o mercado nacional de forma significativa. A solução promete aumentar a produtividade em até 40% e já está sendo testada por grandes empresas do país.",
        "category": "Tecnologia",
        "author": "João Silva",
        "published_at": "2024-01-15T10:00:00Z",
        "views": 15420,
        "tags": ["tecnologia", "inovação", "mercado", "brasil"]
    }
    
    return json.dumps(news_data, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print(f"🚀 Starting Globo News MCP Server on port {mcp_port}...")
    print("Available tool: get_news()")
    print(f"MCP Server: http://localhost:{mcp_port}")
    print("FastAPI: http://localhost:8000")
    print("Server is running... Press Ctrl+C to stop")
    
    try:
        # Run as SSE server for HTTP access
        mcp.run()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        exit(1)
