from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["lazar_hi20"][entry.entry_id]
    async_add_entities([LazarRawSensor(coordinator)])

class LazarRawSensor(SensorEntity):
    name = "Lazar HI20 Raw"
    entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def native_value(self):
        return str(self.coordinator.data)