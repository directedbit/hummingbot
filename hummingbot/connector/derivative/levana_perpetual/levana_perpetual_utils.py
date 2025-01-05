from decimal import Decimal
from typing import Any, Dict, List, Tuple

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import (
    BaseConnectorConfigMap,
    ClientFieldData,
)
from hummingbot.connector.utils import split_hb_trading_pair
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

# TODO Levana fees
DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.0006"),
    taker_percent_fee_decimal=Decimal("0.0001"),
)

CENTRALIZED = True

EXAMPLE_PAIR = "BTC-USD"


class LevanaPerpetualConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="levana_perpetual", client_data=None)
    levana_perpetual_secret_phrase: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Osmosis memonic secret phrase",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )
    levana_perpetual_chain_address: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Levana private key (need to use Leap not keplr), remove the leading 0x",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )

    class Config:
        title = "levana_perpetual"


KEYS = LevanaPerpetualConfigMap.construct()

OTHER_DOMAINS = ["levana_perpetual_testnet"]
OTHER_DOMAINS_PARAMETER = {
    "levana_perpetual_testnet": "levana_perpetual_testnet"
}
OTHER_DOMAINS_EXAMPLE_PAIR = {"levana_perpetual_testnet": "BTC-USDT"}
OTHER_DOMAINS_DEFAULT_FEES = {
    "levana_perpetual_testnet": TradeFeeSchema(
        maker_percent_fee_decimal=Decimal("-0.00025"),
        taker_percent_fee_decimal=Decimal("0.00075"),
    )
}


class LevanaPerpetualTestnetConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default="levana_perpetual_testnet", client_data=None)
    levana_perpetual_secret_phrase: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Osmosis Testnet memonic secret phrase",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )
    levana_perpetual_chain_address: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=lambda cm: "Enter your Osmosis Testnet chain address (starts with osmo)",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        ),
    )

    class Config:
        title = "levana_perpetual"

    class Config:
        title = "levana_perpetual_testnet"


OTHER_DOMAINS_KEYS = {
    "levana_perpetual_testnet": LevanaPerpetualTestnetConfigMap.construct()
}
