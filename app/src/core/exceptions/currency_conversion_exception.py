class CurrencyConversionException(Exception):
    def __init__(self, code: int):
        super().__init__(f"erro ao converter cambio; codigo de resposta: {code}")