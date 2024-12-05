from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import (
    RESTRequest,
    WSRequest,
)


class LevanaPerpetualAuth(AuthBase):

    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        """
        Adds the server time and the signature to the request, required for authenticated interactions. It also adds
        the required parameter in the request header.
        :param request: the request to be configured for authenticated interaction
        """
        raise NotImplementedError(
            "Levana Perpetual does not use REST authentication"
        )

    async def ws_authenticate(self, request: WSRequest) -> WSRequest:
        """
        This method is intended to configure a websocket request to be authenticated. Levana does not use this
        functionality
        """
        raise NotImplementedError(
            "Levana Perpetual does not use websocket authentication"
        )
