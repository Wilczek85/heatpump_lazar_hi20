from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

SENSORS = {
    "energy_total": ("Energia całkowita", "kWh"),
    "energy_compressor": ("Energia sprężarki", "kWh"),
    "troom": ("Temperatura pokojowa", "°C"),
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        LazarSensor(coordinator, key, name, unit)
        for key, (name, unit) in SENSORS.items()
    )

class LazarSensor(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator, key, name, unit):
        self.coordinator = coordinator
        self.key = key
        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"{coordinator.name}_{key}"

    @property
    def native_value(self):
        return self.coordinator.data.get(self.key)
