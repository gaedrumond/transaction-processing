import boto3

from app.src.adapter.secundary.currency_api import CurrencyAPI
from app.src.adapter.secundary.transaction_db import TransactionDB
from app.src.application.use_cases.process_transaction_data import ProcessTransactionData
from app.src.utils.logger_mixin import logger


def lambda_handler(event, context):
    dynamodb_client = boto3.client('dynamodb')
    secrets_client = boto3.client('secretsmanager')
    table = 'transactions'
    logger.info("starting execution of transaction data processing")
    processor = ProcessTransactionData(CurrencyAPI(secrets_client), TransactionDB(dynamodb_client, table))
    for record in event['Records']:
        processor.process_data(record['SNS']['Message'])