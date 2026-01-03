
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarPowerSwitch(coordinator)])

class LazarPowerSwitch(CoordinatorEntity, SwitchEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Lazar HI20 Power"

    @property
    def is_on(self):
        return self.coordinator.data["params"]["onoff"] == 1

    async def async_turn_on(self, **kwargs):
        await self.coordinator.api.set_param("onoff", 1)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        await self.coordinator.api.set_param("onoff", "off")
        await self.coordinator.async_request_refresh()
