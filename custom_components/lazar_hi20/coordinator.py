from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
from datetime import timedelta
import aiohttp

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, entry):
        self.username = entry.data["username"]
        self.password = entry.data["password"]
        self.session = aiohttp.ClientSession()
        super().__init__(
            hass,
            logger=None,
            name="Lazar HI20",
            update_interval=timedelta(seconds=60),
        )

    async def _async_update_data(self):
        async with self.session.get("https://hkslazar.net/oemSerwis?what=bcst", auth=aiohttp.BasicAuth(self.username, self.password)) as resp:
            if resp.status != 200:
                return {}
            return await resp.json()