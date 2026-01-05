from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([LazarPowerSwitch(hass, entry)])

class LazarPowerSwitch(SwitchEntity):
    _attr_name = "Lazar HI20 Power"
    _attr_unique_id = "lazar_hi20_power"

    def __init__(self, hass, entry):
        self.coordinator = hass.data[DOMAIN][entry.entry_id]

    @property
    def is_on(self):
        return self.coordinator.data["params"]["onoff"] == 1

    async def async_turn_on(self, **kwargs):
        await self.coordinator.api.set_param("onoff", "on")

    async def async_turn_off(self, **kwargs):
        await self.coordinator.api.set_param("onoff", "off")
