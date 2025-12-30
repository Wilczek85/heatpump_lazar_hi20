from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfTemperature, UnitOfPower
from .const import DOMAIN

TEMP_SENSORS = {
    "zew": "Temperatura zewnętrzna",
    "out": "Zasilanie CO",
    "ret": "Powrót CO",
    "cwu": "CWU",
    "zadactcwu": "CWU zadana",
    "compevap": "Parownik",
    "compsuc": "Ssanie sprężarki",
}

POWER_SENSORS = {
    "powerneed": "Pobór mocy",
    "comprpow": "Moc sprężarki",
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = []

    for key, name in TEMP_SENSORS.items():
        entities.append(LazarTempSensor(coordinator, key, name))

    for key, name in POWER_SENSORS.items():
        entities.append(LazarPowerSensor(coordinator, key, name))

    async_add_entities(entities)

class LazarTempSensor(SensorEntity):
    def __init__(self, coordinator, key, name):
        self.coordinator = coordinator
        self.key = key
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    @property
    def native_value(self):
        val = self.coordinator.data["stat"]["temps"].get(self.key)
        if val in (None, -9999):
            return None
        return val / 10

class LazarPowerSensor(SensorEntity):
    def __init__(self, coordinator, key, name):
        self.coordinator = coordinator
        self.key = key
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfPower.WATT

    @property
    def native_value(self):
        return self.coordinator.data["stat"]["unit"].get(self.key)
