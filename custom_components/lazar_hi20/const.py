
DOMAIN = "heatpump_lazdar_hi20"
NAME = "Lazar HI20 Heat Pump"

API_BASE = "https://hkslazar.net"
LOGIN_ENDPOINT = "/sollogin"
DATA_ENDPOINT = "/oemSerwis?what=bcst"
SET_ENDPOINT = "/oemSerwis?what=setparam"

PLATFORMS = ["sensor", "binary_sensor", "switch", "select", "number"]
SCAN_INTERVAL = 10
