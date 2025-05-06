from dataclasses import dataclass

import boto3

from app.src.application.ports.secrets_port import SecretsPort

@dataclass
class SecretsManager(SecretsPort):
    _client: boto3.client

    def get_secret(self, key: str) -> str:
        return self._client.get_secret_value(
            SecretId=key,
        ).get('SecretString')