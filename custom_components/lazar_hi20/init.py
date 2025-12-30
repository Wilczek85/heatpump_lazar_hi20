from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .api import LazarHi20API
from .coordinator import LazarCoordinator
from .const import DOMAIN

PLATFORMS = [
    "sensor",
    "binary_sensor",
    "switch",
    "select",
    "number",
    "climate"
]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    api = LazarHi20API(entry.data["login"], entry.data["password"])
    await hass.async_add_executor_job(api.login_api)

    coordinator = LazarCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
