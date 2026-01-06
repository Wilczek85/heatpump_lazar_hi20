
import aiohttp
from .const import API_BASE

class LazarHI20API:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = aiohttp.ClientSession()

    async def login(self):
        async with self.session.post(f"{API_BASE}/sollogin", data={
            "login": self.username,
            "password": self.password
        }) as resp:
            if resp.status != 200:
                raise Exception("Login failed")

    async def get_bcst(self):
        async with self.session.get(f"{API_BASE}/oemSerwis?what=bcst") as resp:
            if "application/json" not in resp.headers.get("Content-Type",""):
                return {}
            return await resp.json()
