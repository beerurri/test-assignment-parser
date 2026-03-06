import time
import urllib.parse

from client.retry import request_with_backoff

from config.settings import VOL_DIVISOR, PART_DIVISOR


class WildberriesClient:
    def __init__(self, session):
        self.session = session
        self.vol_ranges = self.get_cdn_ranges()

    def get_cdn_ranges(self):
        url = f'https://cdn.wbbasket.ru/api/v3/upstreams?t={int(time.time()*1000)}'
        response = request_with_backoff(self.session, url)
        data = response.json()

        return data['recommend']['mediabasket_route_map'][0]['hosts']

    def get_basket(self, product_id):
        vol = product_id // VOL_DIVISOR
        for r in self.vol_ranges:
            if r['vol_range_from'] <= vol <= r['vol_range_to']:
                return r['host']

        raise ValueError(f'Volume {vol} out of range')

    def search(self, query, page):
        query_encoded = urllib.parse.quote_plus(query)
        url = (
            'https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search'
            f'?ab_testing=false'
            f'&appType=1'
            f'&curr=rub'
            f'&dest=123585943'
            f'&hide_vflags=4294967296'
            f'&lang=ru'
            f'&page={page}'
            f'&query={query_encoded}'
            f'&resultset=catalog'
            f'&sort=popular'
            f'&spp=30'
            f'&suppressSpellcheck=false'
        )

        response = request_with_backoff(self.session, url)

        return response.json()

    def get_product_card(self, product_id):
        vol = product_id // VOL_DIVISOR
        part = product_id // PART_DIVISOR
        host = self.get_basket(product_id)
        url = f'https://{host}/vol{vol}/part{part}/{product_id}/info/ru/card.json'

        response = request_with_backoff(self.session, url)

        return response.json()