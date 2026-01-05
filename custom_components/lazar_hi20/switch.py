
from homeassistant.components.switch import SwitchEntity

async def async_setup_entry(hass, entry, async_add_entities):
    api = hass.data["lazar_api"]
    async_add_entities([LazarOnOff(api)])

class LazarOnOff(SwitchEntity):
    _attr_name = "Pompa ciepła"

    def __init__(self, api):
        self.api = api

    async def async_turn_on(self, **kwargs):
        await self.api.set_param("onoff", "on")

    async def async_turn_off(self, **kwargs):
        await self.api.set_param("onoff", "off")
