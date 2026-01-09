import logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)

class LazarCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(
            hass,
            _LOGGER,
            name="lazar_hi20",
            update_interval=timedelta(seconds=UPDATE_INTERVAL)
        )
        self.api = api

    async def _async_update_data(self):
        data = await self.api.async_fetch()
        data.setdefault("energy_total", 0.0)
        data.setdefault("energy_compressor", 0.0)
        data.setdefault("troom", None)
        return data
