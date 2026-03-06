from client.session import create_session
from api.wildberries_client import WildberriesClient
from services.catalog import collect_catalog
from services.cards import collect_cards
from exporters.xlsx_exporter import export_catalog, export_filtered

from config.logger_config import setup_logger


def main():
    setup_logger()

    # создаём HTTP-сессию, используем пул соединений для параллельных запросов
    session = create_session()
    client = WildberriesClient(session)

    # сначала получаем "плоский" каталог товаров по ключевому запросу
    catalog = collect_catalog(client)

    # затем собираем подробные карточки; функция сама распараллеливает запросы
    collected = collect_cards(client, catalog)
    
    # экспортируем полный набор
    export_catalog(collected)

    # и экспорт с фильтрацией по рейтингу/цене/стране
    export_filtered(collected)


if __name__ == '__main__':
    main()