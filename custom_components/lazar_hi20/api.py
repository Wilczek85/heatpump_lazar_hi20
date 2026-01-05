
import aiohttp
from .const import API_BASE

class LazarAPI:
    def __init__(self, session, login, password):
        self._session = session
        self._login = login
        self._password = password
        self._cookie = None

    async def login(self):
        async with self._session.post(f"{API_BASE}/sollogin", data={
            "login": self._login,
            "haslo": self._password
        }) as resp:
            resp.raise_for_status()
            self._cookie = resp.cookies.get("solaccess")

    async def get_data(self):
        if not self._cookie:
            await self.login()
        async with self._session.get(
            f"{API_BASE}/oemSerwis?what=bcst",
            cookies={"solaccess": self._cookie.value}
        ) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def set_param(self, param, value):
        async with self._session.get(
            f"{API_BASE}/oemSerwis?what=setparam&param={param}&value={value}",
            cookies={"solaccess": self._cookie.value}
        ) as resp:
            resp.raise_for_status()
