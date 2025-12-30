from homeassistant.components.select import SelectEntity
from .const import DOMAIN

MODES = {
    0: "Grzanie",
    1: "Chłodzenie",
    2: "CWU"
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    api = coordinator.api
    async_add_entities([LazarModeSelect(api, coordinator)])

class LazarModeSelect(SelectEntity):
    _attr_name = "Tryb pracy"
    _attr_options = list(MODES.values())

    def __init__(self, api, coordinator):
        self.api = api
        self.coordinator = coordinator

    @property
    def current_option(self):
        return MODES[self.coordinator.data["params"]["mode"]]

    async def async_select_option(self, option):
        for k, v in MODES.items():
            if v == option:
                await self.hass.async_add_executor_job(
                    self.api.set_param, "mode", k
                )
