
import aiohttp

class LazarAPI:
    def __init__(self, session, username, password):
        self._session = session
        self._username = username
        self._password = password
        self._cookie = None

    async def login(self):
        async with self._session.post(
            "https://hkslazar.net/sollogin",
            data={"login": self._username, "haslo": self._password},
        ) as resp:
            cookies = resp.cookies
            if "solaccess" in cookies:
                self._cookie = cookies["solaccess"].value
                return True
            return False

    async def get_data(self):
        headers = {"Cookie": f"solaccess={self._cookie}"}
        async with self._session.get(
            "https://hkslazar.net/oemSerwis?what=bcst",
            headers=headers,
        ) as resp:
            return await resp.json()

    async def set_param(self, param, value):
        headers = {"Cookie": f"solaccess={self._cookie}"}
        url = f"https://hkslazar.net/oemSerwis?what=setparam&param={param}&value={value}"
        async with self._session.get(url, headers=headers) as resp:
            return await resp.text()
