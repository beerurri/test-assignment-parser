import pandas as pd
from models.product import Product
from typing import List


def _get_alias_map():
    return {
        name: field.alias
        for name, field in Product.model_fields.items()
        if field.alias
    }


def export_catalog(products: List[Product]):
    data = [p.model_dump(by_alias=True) for p in products]
    df = pd.DataFrame(data)
    df.to_excel('catalog.xlsx', index=False)


def export_filtered(products: List[Product]):
    data = [p.model_dump() for p in products]
    df = pd.DataFrame(data)

    filtered = df[
        (df['rating'] >= 4.5)
        & (df['price'] < 10_000_00)
        & (df['country'] == 'Россия')
    ]

    filtered = filtered.rename(columns=_get_alias_map())
    filtered.to_excel('filtered_catalog.xlsx', index=False)