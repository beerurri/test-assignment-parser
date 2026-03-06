from pydantic import BaseModel, Field, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    url: str = Field(alias='URL')
    article: int = Field(alias='Артикул')
    name: str = Field(alias='Название')
    price: int = Field(alias='Цена')
    description: str = Field(alias='Описание')
    image_urls: list = Field(alias='Изображения')
    properties: str = Field(alias='Характеристики')
    seller_name: str = Field(alias='Продавец')
    seller_url: str = Field(alias='URL продавца')
    sizes: list = Field(alias='Размеры')
    stock: int = Field(alias='Остаток')
    rating: float = Field(alias='Рейтинг')
    reviews: int = Field(alias='Отзывы')
    country: str = Field(alias='Страна производства')