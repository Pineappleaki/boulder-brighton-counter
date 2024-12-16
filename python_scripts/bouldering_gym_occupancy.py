import requests
import re
from bs4 import BeautifulSoup

# URL to fetch the data
URL = "https://portal.rockgympro.com/portal/public/620b59568a6c93407373bda88564f747/occupancy?&iframeid=occupancyCounter&fId="

def fetch_occupancy():
    """Fetch the climber count from the gym website."""
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        script_content = soup.find("script", text=re.compile(r"var data =")).string

        # Extract JavaScript object
        match = re.search(r"var data = ({.*?});", script_content, re.DOTALL)
        if not match:
            logger.error("Could not find data variable in script.")
            return None

        # Convert to Python dictionary
        data = match.group(1).replace("'", '"')
        import json
        data_dict = json.loads(data)

        # Extract climber count
        return data_dict["AAA"]["count"]
    except Exception as e:
        logger.error(f"Error fetching occupancy: {e}")
        return None

# Main logic for the script
occupancy = fetch_occupancy()
if occupancy is not None:
    logger.info(f"Climber count: {occupancy}")
    # Update a Home Assistant entity with the climber count
    hass.states.set("sensor.bouldering_gym_occupancy", occupancy)
