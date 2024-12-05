from typing import Any, Dict, List, Optional

from hummingbot.connector.derivative.bybit_perpetual import (
    bybit_perpetual_constants as CONSTANTS,
)
from hummingbot.connector.derivative.bybit_perpetual.bybit_perpetual_utils import (
    is_linear_perpetual,
)
from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
from hummingbot.core.api_throttler.data_types import (
    LinkedLimitWeightPair,
    RateLimit,
)
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import (
    RESTMethod,
    RESTRequest,
)
from hummingbot.core.web_assistant.rest_pre_processors import (
    RESTPreProcessorBase,
)
from hummingbot.core.web_assistant.web_assistants_factory import (
    WebAssistantsFactory,
)


def build_api_factory(
    throttler: Optional[AsyncThrottler] = None,
    auth: Optional[AuthBase] = None,
) -> WebAssistantsFactory:
    throttler = throttler
    api_factory = WebAssistantsFactory(
        throttler=throttler,
        auth=auth,
        rest_pre_processors=[],
    )
    return api_factory
