from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

HEATERS = {
    "leak": "Grzałka antyzamarzaniowa",
    "flowlvl1": "Grzałka CO poziom 1",
    "flowlvl2": "Grzałka CO poziom 2",
    "carter": "Grzałka karteru sprężarki",
}

PUMPS = {
    "pumpcir1": "Pompa obiegu CO 1",
    "pumpcir2": "Pompa obiegu CO 2",
}

OTHER_BINARY = {
    "valve4way": "Zawór 4-drogowy",
}


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []

    for key, name in HEATERS.items():
        entities.append(
            LazarBinarySensor(
                coordinator,
                f"stat.heaters.{key}",
                name,
            )
        )

    for key, name in PUMPS.items():
        entities.append(
            LazarBinarySensor(
                coordinator,
                f"stat.pumps.{key}",
                name,
            )
        )

    for key, name in OTHER_BINARY.items():
        entities.append(
            LazarBinarySensor(
                coordinator,
                f"stat.other.{key}",
                name,
            )
        )

    async_add_entities(entities)


class LazarBinarySensor(CoordinatorEntity, BinarySensorEntity):
    def __init__(self, coordinator, path, name):
        super().__init__(coordinator)
        self._path = path
        self._attr_name = name
        self._attr_unique_id = f"{coordinator.data['boxid']}_{path}"

    @property
    def is_on(self):
        data = self.coordinator.data
        if not data:
            return None

        try:
            value = data
            for key in self._path.split("."):
                value = value[key]
        except Exception:
            return None

        return bool(value)
