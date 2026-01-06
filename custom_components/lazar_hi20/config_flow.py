
from homeassistant import config_entries
from .const import DOMAIN, CONF_USERNAME, CONF_PASSWORD

class LazarHI20Flow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title="Lazar HI20", data=user_input)
        return self.async_show_form(step_id="user", data_schema=self.schema({
            CONF_USERNAME: str,
            CONF_PASSWORD: str
        }))
