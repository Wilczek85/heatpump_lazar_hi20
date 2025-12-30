from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVACMode
from homeassistant.const import UnitOfTemperature
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    api = coordinator.api
    async_add_entities([LazarCWUClimate(api, coordinator)])

class LazarCWUClimate(ClimateEntity):
    _attr_name = "CWU"
    _attr_hvac_modes = [HVACMode.HEAT]
    _attr_temperature_unit = UnitOfTemperature.CELSIUS

    def __init__(self, api, coordinator):
        self.api = api
        self.coordinator = coordinator

    @property
    def current_temperature(self):
        return self.coordinator.data["stat"]["temps"]["cwu"] / 10

    @property
    def target_temperature(self):
        return self.coordinator.data["params"]["cwu"]["tsetcomf"] / 10

    async def async_set_temperature(self, **kwargs):
        value = int(kwargs["temperature"] * 10)
        await self.hass.async_add_executor_job(
            self.api.set_param, "tsetcomf", value
        )
