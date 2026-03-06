import requests
from requests.adapters import HTTPAdapter
from config.settings import HEADERS, CARD_POOL_WORKERS


def create_session():
    session = requests.Session()
    adapter = HTTPAdapter(pool_connections=CARD_POOL_WORKERS, pool_maxsize=CARD_POOL_WORKERS)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    session.headers.update(HEADERS)
    return session