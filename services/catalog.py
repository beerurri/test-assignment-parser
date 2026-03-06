"""Модуль для сбора плоского каталога товаров.

Выполняет поиск по QUERY и обходит все страницы, возвращая
список сырых словарей с атрибутами каждого товара.
"""

from config.settings import QUERY
from api.wildberries_client import WildberriesClient
import logging

logger = logging.getLogger(__name__)

def collect_catalog(client: WildberriesClient):
    page = 1
    products = list()

    init = client.search(QUERY, page)
    
    total = init['total']
    logger.info(f'Total products: {total}')

    products.extend(init['products'])

    last_page = total // 100 + 1

    for page in range(2, last_page + 1):
        logger.info(f'Page {page}/{last_page}')

        data = client.search(QUERY, page)
        products.extend(data['products'])

    return products