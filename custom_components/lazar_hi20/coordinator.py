
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(
            hass,
            logger=None,
            name="Lazar HI20",
            update_interval=timedelta(seconds=30)
        )
        self.api = api

    async def _async_update_data(self):
        try:
            return await self.api.get_data()
        except Exception as e:
            raise UpdateFailed(str(e))
