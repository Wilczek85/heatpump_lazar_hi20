from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(
            hass,
            logger=None,
            name=DOMAIN,
            update_interval=timedelta(seconds=30)
        )
        self.api = api

    async def _async_update_data(self):
        try:
            return await self.hass.async_add_executor_job(self.api.get_data)
        except Exception as err:
            raise UpdateFailed(err)
