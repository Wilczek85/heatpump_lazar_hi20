from .const import DOMAIN, CONF_USERNAME, CONF_PASSWORD
from .api import LazarAPI
from .coordinator import LazarCoordinator

PLATFORMS = ["sensor"]

async def async_setup_entry(hass, entry):
    api = LazarAPI(entry.data[CONF_USERNAME], entry.data[CONF_PASSWORD])
    await api.async_login()

    coordinator = LazarCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass, entry):
    coordinator = hass.data[DOMAIN].pop(entry.entry_id)
    await coordinator.api.async_close()
    return True
