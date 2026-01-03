
import aiohttp

class LazarAPI:
    def __init__(self, session, username, password):
        self.session = session
        self.username = username
        self.password = password
        self.cookie = None

    async def login(self):
        async with self.session.post(
            "https://hkslazar.net/sollogin",
            data={"login": self.username, "haslo": self.password},
        ) as resp:
            if "solaccess" in resp.cookies:
                self.cookie = resp.cookies["solaccess"].value
                return True
            raise ConnectionError("Login failed")

    async def _headers(self):
        return {"Cookie": f"solaccess={self.cookie}"}

    async def get_data(self):
        async with self.session.get(
            "https://hkslazar.net/oemSerwis?what=bcst",
            headers=await self._headers(),
        ) as resp:
            return await resp.json()

    async def set_param(self, param, value):
        url = f"https://hkslazar.net/oemSerwis?what=setparam&param={param}&value={value}"
        async with self.session.get(url, headers=await self._headers()) as resp:
            return await resp.text()
