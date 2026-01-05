
from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api import LazarAPI
from .const import DOMAIN

class LazarFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input:
            session = async_get_clientsession(self.hass)
            api = LazarAPI(session, user_input["login"], user_input["password"])
            await api.login()
            return self.async_create_entry(
                title="Lazar HI20",
                data=user_input
            )
        return self.async_show_form(
            step_id="user",
            data_schema={
                "login": str,
                "password": str
            }
        )
