"""Парсинг карточек товаров и преобразование в модели Product.

Функция collect_cards принимает список словарей из каталога и
параллельно (ThreadPoolExecutor) запрашивает карточку и хост корзины
для каждого товара, затем вызывает parse_product_card.
"""

import logging

from config.settings import VOL_DIVISOR, PART_DIVISOR, CARDS_LIMIT, CARD_POOL_WORKERS
from api.wildberries_client import WildberriesClient
from models.product import Product
import json

from concurrent.futures import ThreadPoolExecutor, as_completed

logger = logging.getLogger(__name__)


def collect_cards(client: WildberriesClient, products: list, max_workers: int = CARD_POOL_WORKERS):
    # для отладки можно ограничить количество карточек
    if CARDS_LIMIT:
        products = products[:CARDS_LIMIT]

    def _fetch(product_json, index, total):
        article = product_json['id']
        logger.info(f'Collecting card {index+1} out of {total} - Article: {article}')
        # получаем JSON карточки и хост корзины
        card = client.get_product_card(article)
        basket = client.get_basket(article)
        return parse_product_card(card, product_json, basket)

    results = []
    total = len(products)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(_fetch, p, i, total)
                   for i, p in enumerate(products)]

        for fut in as_completed(futures):
            results.append(fut.result())

    return results


def parse_product_card(card_json: dict, product_json: dict, basket: str):
    """Собирает объект Product из сырых данных карточки и каталога.
    """
    properties = extract_properties(card_json)
    return Product(
        url=f'https://www.wildberries.ru/catalog/{product_json["id"]}/detail.aspx',
        article=product_json['id'],
        name=product_json['name'],
        price=extract_price(product_json),
        description=card_json.get('description', ''),
        image_urls=[
            f'https://{basket}/vol{product_json["id"] // VOL_DIVISOR}/part{product_json["id"] // PART_DIVISOR}/{product_json["id"]}/images/c516x688/{i+1}.webp'
            for i in range(product_json['pics'])
            ],
        properties=json.dumps(properties, ensure_ascii=False),
        seller_name=product_json['brand'],
        seller_url=f'https://www.wildberries.ru/brands/{product_json["brandId"]}',
        sizes=[s['name'] for s in product_json['sizes']],
        stock=product_json['totalQuantity'],
        rating=product_json['reviewRating'],
        reviews=product_json['feedbacks'],
        country=properties.get('Страна производства', '')
    )


def extract_properties(card_json: dict):
    props = dict()
    for p in card_json.get('options', []):
        name = p.get('name')
        value = p.get('value')
        if name and value:
            props[name] = value

    return props


def extract_price(product_json: dict):
    """Ищет первую попавшуюся цену в описании размеров товара.
    """
    sizes = product_json.get('sizes', [])
    if sizes:
        for size in sizes:
            price = size.get('price', {})
            if not price:
                continue

            for field in ['product', 'basic']:
                value = price.get(field)
                if value:
                    return value

    return None