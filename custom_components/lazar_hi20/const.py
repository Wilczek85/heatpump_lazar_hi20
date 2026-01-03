
DOMAIN = "heatpump_lazdar_hi20"
NAME = "Lazar HI20 Heat Pump"
API_BASE = "https://hkslazar.net"
LOGIN_URL = "/sollogin"
DATA_URL = "/oemSerwis?what=bcst"
SET_URL = "/oemSerwis?what=setparam"
PLATFORMS = ["sensor", "switch", "number", "select"]
UPDATE_INTERVAL = 10
