
from homeassistant.components.select import SelectEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

MODES = {
    "Grzanie": 0,
    "Chłodzenie": 1,
    "CWU": 2,
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarModeSelect(coordinator)])

class LazarModeSelect(CoordinatorEntity, SelectEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Tryb pracy"
        self._attr_options = list(MODES.keys())

    @property
    def current_option(self):
        mode = self.coordinator.data["params"]["mode"]
        for k, v in MODES.items():
            if v == mode:
                return k

    async def async_select_option(self, option):
        await self.coordinator.api.set_param("mode", MODES[option])
        await self.coordinator.async_request_refresh()
