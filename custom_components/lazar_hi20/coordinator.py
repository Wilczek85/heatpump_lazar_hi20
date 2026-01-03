
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, SCAN_INTERVAL

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(
            hass,
            logger=None,
            name=DOMAIN,
            update_interval=timedelta(seconds=SCAN_INTERVAL),
        )
        self.api = api

    async def _async_update_data(self):
        data = await self.api.get_data()
        if data.get("error", 0) != 0:
            raise UpdateFailed("API error")
        return data
