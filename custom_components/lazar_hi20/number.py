
from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarCWUEco(coordinator), LazarCWUComf(coordinator)])

class LazarCWUEco(CoordinatorEntity, NumberEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "CWU ECO"
        self._attr_native_min_value = 300
        self._attr_native_max_value = 600
        self._attr_native_step = 5

    @property
    def native_value(self):
        return self.coordinator.data["params"]["cwu"]["tseteco"]

    async def async_set_native_value(self, value):
        await self.coordinator.api.set_param("tseteco", int(value))
        await self.coordinator.async_request_refresh()

class LazarCWUComf(CoordinatorEntity, NumberEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "CWU Komfort"
        self._attr_native_min_value = 300
        self._attr_native_max_value = 650
        self._attr_native_step = 5

    @property
    def native_value(self):
        return self.coordinator.data["params"]["cwu"]["tsetcomf"]

    async def async_set_native_value(self, value):
        await self.coordinator.api.set_param("tsetcomf", int(value))
        await self.coordinator.async_request_refresh()
