
from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["lazar_hi20"]
    async_add_entities([LazarTempSensor(coordinator, "zew", "Temperatura zewnętrzna")])

class LazarTempSensor(Entity):
    def __init__(self, coordinator, key, name):
        self.coordinator = coordinator
        self.key = key
        self._attr_name = name

    @property
    def state(self):
        return self.coordinator.data["stat"]["temps"][self.key] / 10
