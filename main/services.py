"""
Business logic functions.
"""
import math
import logging


from datetime import datetime


from .serializers import TariffInputSerializer, TariffOutputSerializser
from .loggerSettings import CustomLogger

logging.basicConfig(level=logging.INFO, filename="services_log.py",  
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def calculate_duration(data: TariffInputSerializer) -> float:
    """
    Calculate session duration.
    """

    start = data.validated_data['Started_at']
    now = datetime.now(start.tzinfo)
    lpt = data.validated_data.get('LastPaymentTime')
    unpaind_duration = None

    if lpt:
        unpaind_duration = (now - lpt).total_seconds()
    duration = (now - start).total_seconds()

    return duration, unpaind_duration


def duration_transfer(seconds: int, unit: str) -> int:
    """
    Transfer seconds to tariff unit.
    """
    unit = unit.lower()

    if unit == "минута":
        sec = 60
    elif unit == "час":
        sec = 3600
    elif unit == "день":
        sec = 86400
    elif unit == "неделя":
        sec = 604800
    else:
        return
    
    unit = seconds / sec
    return math.ceil(unit)
    

def calculate_cos(deposit: int, duration: int, price: int) -> int:
    """
    Calculate debt.
    """
    return deposit - duration * price


def tariffService(data: TariffInputSerializer) -> TariffOutputSerializser:
    """
    Helpful function for processing data.
    """
    logger = CustomLogger()
    data_json = logger.json_data(data)
    
    duration, unpaind_duration = calculate_duration(data)
    transfer = duration_transfer(duration, data.validated_data['TariffUnit'])

    deposit = data.validated_data.get('Deposit', 0)
    cos = calculate_cos(deposit, transfer,
                        data.validated_data['TariffUnitPrice'])
    
    logging.info(f"Parameters are:\n{data_json}")
    logging.info(f"Results are{duration, unpaind_duration, cos}")
    
    output = TariffOutputSerializser(data={
        'Duration': str(duration),
        'UnpaidDuration': str(unpaind_duration) if unpaind_duration else '',
        'Cost': cos
    })
    if output.is_valid():
        return output.validated_data

   