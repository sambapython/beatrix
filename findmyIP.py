import aiohttp
import requests
def get_county(ipaddress):
    url = f"https://ipinfo.io/{ipaddress}/country"
    return requests.get(url)
    # with aiohttp.session() as session:
    #     return session.get(url)