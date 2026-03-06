import logging
import time
import random
from config.settings import MAX_RETRIES, INITIAL_DELAY

logger = logging.getLogger(__name__)


def request_with_backoff(session, url):
    delay = INITIAL_DELAY

    for i in range(MAX_RETRIES):
        response = session.get(url)
        if response.status_code == 200:
            logger.info(f'Success: {url}')
            return response

        if response.status_code == 429 and i < MAX_RETRIES - 1:
            sleep_time = delay + random.uniform(0, delay / 3)
            
            logger.warning(f'Retry #{i+1} -> sleep {sleep_time:.2f}s')
            time.sleep(sleep_time)

            delay *= 2
            continue

        logger.error(f'Failed to fetch {url} - Status code: {response.status_code}')
        raise Exception(f'Request failed: {response.status_code}')

    logger.error(f'Max retries exceeded for {url}')
    raise Exception('Max retries exceeded')