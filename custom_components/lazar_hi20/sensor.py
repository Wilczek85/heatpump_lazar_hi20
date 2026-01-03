
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import UnitOfTemperature, UnitOfPower
from .const import DOMAIN

SENSORS = [
    ("zew", "Temperatura zewnętrzna", ["stat","temps","zew"], 0.1, UnitOfTemperature.CELSIUS),
    ("out", "Zasilanie CO", ["stat","temps","out"], 0.1, UnitOfTemperature.CELSIUS),
    ("ret", "Powrót CO", ["stat","temps","ret"], 0.1, UnitOfTemperature.CELSIUS),
    ("cwu", "Temperatura CWU", ["stat","temps","cwu"], 0.1, UnitOfTemperature.CELSIUS),
    ("power", "Pobór mocy", ["stat","unit","powerneed"], 1, UnitOfPower.WATT),
]

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LazarSensor(coordinator, *s) for s in SENSORS])

class LazarSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, key, name, path, factor, unit):
        super().__init__(coordinator)
        self._attr_unique_id = f"lazar_{key}"
        self._attr_name = name
        self.path = path
        self.factor = factor
        self._attr_native_unit_of_measurement = unit

    @property
    def native_value(self):
        data = self.coordinator.data
        for p in self.path:
            data = data.get(p, {})
        if isinstance(data, (int, float)):
            return data * self.factor
        return None
