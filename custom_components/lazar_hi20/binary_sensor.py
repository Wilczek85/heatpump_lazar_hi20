from homeassistant.components.binary_sensor import BinarySensorEntity
from .const import DOMAIN

BINARY_SENSORS = {
    "leak": "Grzałka antyzamarzaniowa",
    "flowlvl1": "Grzałka poziom 1",
    "flowlvl2": "Grzałka poziom 2",
    "carter": "Grzałka karteru"
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        LazarBinary(coordinator, k, v)
        for k, v in BINARY_SENSORS.items()
    )

class LazarBinary(BinarySensorEntity):
    def __init__(self, coordinator, key, name):
        self.coordinator = coordinator
        self.key = key
        self._attr_name = name

    @property
    def is_on(self):
        return bool(self.coordinator.data["stat"]["heaters"].get(self.key))
