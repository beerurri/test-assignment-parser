from client.session import create_session
from api.wildberries_client import WildberriesClient
from services.catalog import collect_catalog
from services.cards import collect_cards
from exporters.xlsx_exporter import export_catalog, export_filtered

from config.logger_config import setup_logger


def main():
    setup_logger()

    session = create_session()
    client = WildberriesClient(session)

    catalog = collect_catalog(client)
    collected = collect_cards(client, catalog)
    
    export_catalog(collected)

    export_filtered(collected)


if __name__ == '__main__':
    main()