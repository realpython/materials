codes = {
    "1001": "Townsville",
    "1002": "Lakeview",
    "1003": "Mountainview",
    "1101": "Riverside",
    "1102": "Hilltop",
    "1201": "Greenfield",
    "1202": "Sunnydale",
    "1301": "Meadowbrook",
    "1302": "Creekwood",
}
print({code: town for code, town in codes.items() if "1100" <= code <= "1300"})
