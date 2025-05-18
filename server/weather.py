from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
            
# Initiliaze the FASTMCP server
mcp = FastMCP("weather")

# constants 
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/0.1"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API and return the response data with proper error handling"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try: 
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            mcp.log.error(f"Error fetching data from NWS: {e}")
            return None

def format_alert(feature: dict) -> str:
    """Format a weather alert feature into a readable string"""
    props = feature["properties"]
    return f"""
        Event: {props.get('event', 'Unknown')}
        Area: {props.get('areaDesc', 'Unknown')}
        Severity: {props.get('severity', 'Unknown')}
        Description: {props.get('description', 'No description available')}
        Instructions: {props.get('instruction', 'No specific instructions provided')}
    """
    
@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get current weather alerts for a specific state
    
    Args:
        state (str): The two-letter state code (e.g., 'CA', 'NY')
    """
    
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)
    
    if not data or "features" not in data:
        return "No active alerts found for the given state"
    
    if not data["features"]:
        return "No active alerts found for the given state"
    
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n\n".join(alerts)
    

@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echomessage as as resource"""
    return f"Resource Echo: {message}"