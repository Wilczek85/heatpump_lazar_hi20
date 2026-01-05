from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = []
    for key in coordinator.data["stat"]["temps"]:
        entities.append(LazarTempSensor(coordinator, key))
    async_add_entities(entities)

class LazarTempSensor(SensorEntity):
    def __init__(self, coordinator, key):
        self.coordinator = coordinator
        self._key = key
        self._attr_unique_id = f"lazar_hi20_temp_{key}"
        self._attr_name = f"Lazar {key}"

    @property
    def native_value(self):
        return self.coordinator.data["stat"]["temps"][self._key] / 10
