
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    data = coordinator.data
    entities = [
        LazarSensor(coordinator, "Temperatura zewnętrzna", ["stat","temps","zew"], 0.1, "°C"),
        LazarSensor(coordinator, "Temperatura CWU", ["stat","temps","cwu"], 0.1, "°C"),
        LazarSensor(coordinator, "Pobór mocy", ["stat","unit","powerneed"], 1, "W"),
    ]
    async_add_entities(entities)

class LazarSensor(SensorEntity):
    def __init__(self, coordinator, name, path, factor, unit):
        self.coordinator = coordinator
        self._name = name
        self._path = path
        self._factor = factor
        self._unit = unit

    @property
    def name(self):
        return self._name

    @property
    def native_unit_of_measurement(self):
        return self._unit

    @property
    def state(self):
        data = self.coordinator.data
        for p in self._path:
            data = data.get(p, {})
        if isinstance(data, (int, float)):
            return data * self._factor
        return None

    async def async_update(self):
        await self.coordinator.async_request_refresh()
