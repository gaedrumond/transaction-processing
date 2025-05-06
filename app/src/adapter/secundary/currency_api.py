from dataclasses import dataclass
from decimal import Decimal

import requests
from diskcache import Cache

from app.src.application.ports.currency_port import CurrencyPort
from app.src.application.ports.secrets_port import SecretsPort
from app.src.utils.logger_mixin import logger

_cache = Cache('.tmp/currency_cache')

@dataclass
class CurrencyAPI(CurrencyPort):
    _secrets: SecretsPort

    def convert_to_brl(self, base_currency: str, value: Decimal) -> Decimal:
        if base_currency not in _cache:
            logger.info(f"calling currency api because {base_currency} isn't at cache db")
            url_base = self._secrets.get_secret(key='url')
            api_key = self._secrets.get_secret(key='api_key')
            response = requests.get(f'{url_base}/{api_key}/pair/{base_currency}/BRL/{value}').json()
            _cache.set(response.get('base_code'), response.get('conversion_rate'), expire=3600)
            return response.get('conversion_result')
        else:
            logger.info(f"getting currency {base_currency} from cache")
            return _cache.get(base_currency) * float(value)