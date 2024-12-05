from hummingbot.core.data_type.common import OrderType, PositionMode
from hummingbot.core.data_type.in_flight_order import OrderState

EXCHANGE_NAME = "levana_perpetual"

DEFAULT_DOMAIN = "levana_perpetual_main"

DEFAULT_TIME_IN_FORCE = "GTC"

GAS_LIMIT = 500000
CRANK_FEE = 0.04  # this is USD value, need to conver to token value

REST_URLS = {
    "levana_perpetual_main": "https://api.levana.io/",
    "levana_perpetual_testnet": "https://api-testnet.levana.io/",
}

_production_markets_dict = {
    "BTC_USD": "osmo1nzddhaf086r0rv0gmrepn3ryxsu9qqrh7zmvcexqtfmxqgj0hhps4hruzu",
    "RUNE_USDC": "osmo1mrc3zk2fvqvcg9j693u0mlcd8g6329e3w9ld4t7qg20635sfcvuswaxgjm",
    "ATOM_USD": "osmo1hd7r733w49wrqnxx3daz4gy7kvdhgwsjwn28wj7msjfk4tde89aqjqhu8x",
    "INJ_USDC": "osmo1353cxacx74lfugp0sdkdpasa7d09rlwwdaeeql9usw2w6g773vqsxgp053",
    "SOL_USDC": "osmo1jprh8f4ytxar0q3z5n5p6swqnmunnsvuuhnhteskwxjzyc8jayms4r7e3e",
    "axlETH_USD": "osmo19c7hdlfvu7cddr0smfz9luaj8375qhfr3s0gtsk087laqfzxlu3qsnk47e",
    "OSMO_USD": "osmo127aqy4697zqn27z0vqr3x2n8lraf27t7udvl6ef5hcwmwhjadegq9vytdj",
    "PYTH_USDC": "osmo1wszczd8y6lk53ygr59cxt60ualydtwsnr7tu63zkgvu704r7yqdshc47w8",
    "TIA_USD": "osmo1kqzkupfec3zemmaj3kuhcf0h2wke02wa7sgp2a9vq5mugtgs5pzs8avjzt",
    "wBTC_USD": "osmo1x09tzaf7nplch4xjnfp2gfecazmayg84djc4mqvmqqygeddvlcnsm4mnuf",
    "DYM_USD": "osmo1mlmxsjlq4vqymfvj29xv4jlyp536xmq32mjsnc9730jfcanrlj7qv4ryew",
    "milkTIA_USD": "osmo1cts0agkdces0lc3x0s25ezudruhm038n59nwlkm5paes6wx45clq3pn0tw",
    "DYDX_USDC": "osmo1my45yym085dj5jxrtdgy2y4wjlvxf2uwp8plmxq25e0phdyuckzqq5r73w",
    "SEI_USD": "osmo186nlf2fwfglq8u4nj3f7mwg8uc79j22qhaau4scdyur47e0fatas34vcn9",
    "AVAX_USDC": "osmo1gprafrgxx0tlf4u3dxnxcvvmsg2yl4hgqxc68xmkq07h2n0lk9zqycckgc",
    "DOGE_USDC": "osmo19ua8dlul0hq9jfwfq9d0eqcz0lvx5jd8segmn85rz2nv94jlhwcqnkypv3",
    "BNB_USDC": "osmo164357hnc5jc0pw9lv958h6chrpjucr4sy47hwpm9k4av6zh74gnq7uvcpj",
    "stATOM_USD": "osmo1ufpu3nudumzh53sek246zrwvv2cc7leplaqruuggeny7wlcvfrzq4cqmwd",
    "GOLD_USDC": "osmo1vztfv3t3w07vgk06txe0xtrw6spvfvpfx2gcs6lcesxaj2y0znnqx2z5l4",
    "AXL_USD": "osmo1xmuwpu2v97cgk2lmevdylkfvtzrlznv826zht8mezh7979fh9y5sdck8ws",
    "LINK_USDC": "osmo19uqdjvk6j9yjtev7j25sc0v0mszqy3jwwak8z4n0qf6l4wp9csvq0jn0qw",
    "AKT_USD": "osmo13kgh3aksdnhs5jkd63uut9x3us9hfeyzldjgnma6eksj9g3c0cfs3z7wcp",
    "ryETH_USD": "osmo1l5sfd86s7cmyy2fpm4xtklg9q3halrxnsw3d5qhnf24n5c77k65qavf6ke",
    "MEME_USDC": "osmo1nzt529p7mpd0jvp09c9fzuk9nez9c2j3kzkrcz4excnprew7xs4syudjev",
    "WIF_USDC": "osmo19vfrkcve7q62s9pw2xt033qeke6fwhpp6p8pe6ntsz4sx6wkdcksgvmtnc",
    "PEPE_USDC": "osmo1cap92693vajj3chllnvp7yma6p54rwdujy5trwnu7c55ndajskyqut9uxu",
    "NTRN_USDC": "osmo1dyt0wupd5sdefwh53y6e6murnnpfeg27rc7aknhm7tynqzphuwfsr7d4h2",
    "FLOKI_USDC": "osmo1kc5xwad8ss2nper7zqwfqa4kz8xrr6t6tecemt2r458e4xqcl9xq998cxe",
    "BONK_USDC": "osmo1cm9vmw3gdkjg5vqrq7h7ek0hq583ry6v3c53vg4s67pq7x83r8yqpqmlg3",
    "stOSMO_USD": "osmo1uhyscxda8ljzg95a3u2u7rvzfdy6u4dhpj65u8xdja5kext228eq5u8vyp",
    "stDYM_USD": "osmo1xweuhaglh29glzjcsj0n4744u59z0y9cpm965nmxk4pzxg059urs4c2zdd",
    "DOT_USDC": "osmo1cpdkrutx97m7lkxpryx5p7ktkmwrznu0njgwcxpfvjkfknvhl36sl4m6x6",
    "LUNA_USDC": "osmo1u7usfl8wxtzkwllagxxv9u0y5ulv4gyan47gmn76re0830ndk8hsnd05l9",
    "stDYDX_USD": "osmo196l7z8fvqz2v685vpsk2vuw5qyesw4v7y3w7ek08aacx5c0k5heqy8twn4",
    "SHIB_USDC": "osmo16cdpze425guzfnm6av90vqh5ptd0apu4dxrpdhk7yry4kkh65l8qx57fe0",
    "stTIA_USD": "osmo1qkd9mk20gmfuet64rndtsmu7cez3vm6vm0acj743pfadsrxrjs0slp2cw8",
    "SILVER_USDC": "osmo1ctk5cn7vcv0s9xqqzs8sfuph3delcardnddqvgarplrvhdg0258q4hc868",
    "EUR_USDC": "osmo16v36jtfjc933htukqfrk8lk8e2uj8xpp3zjdh0ll04qe9jevlnrsuwhhx8",
    "GBP_USDC": "osmo1rhgn3mp5q7vfr43xgzwtcrnklll6w7e0gv5jvmk9sz26qvcnf3tsw8axyn",
    "CNH_USDC": "osmo1yawtc8n0hckvvmfm6puyhpsatka2wxps9khlg5rr56srz0tlw96q27t99a",
    "stkATOM_USD": "osmo1nu86q2m7j7xacwrsd0asc9lt4eh3205gu90fnu2ssfh2ac6ahjjslp329m",
}
# ATOM_USD contract address on Osmosis testnet
_testnet_markets_dict = {
    "ATOM_USD": "osmo1kus6tmx9ggmvgg5tf88ukgxcz0ynakx38hyjy0sjgahvp7d3ut2qqtfhf4",
    # "WIF_USDC": "osmo19vfrkcve7q62s9pw2xt033qeke6fwhpp6p8pe6ntsz4sx6wkdcksgvmtnc",
}


# unit in millisecond and default value is 5,000, to specify how long an HTTP request is valid.
# It is also used to prevent replay attacks.
X_API_RECV_WINDOW = str(50000)

X_API_SIGN_TYPE = str(2)


HBOT_BROKER_ID = "Hummingbot"

MAX_ID_LEN = 36
SECONDS_TO_WAIT_TO_RECEIVE_MESSAGE = 30
POSITION_IDX_ONEWAY = 0
POSITION_IDX_HEDGE_BUY = 1
POSITION_IDX_HEDGE_SELL = 2

ORDER_TYPE_MAP = {
    OrderType.LIMIT: "Limit",
    OrderType.MARKET: "Market",
}

POSITION_MODE_API_ONEWAY = 0
POSITION_MODE_API_HEDGE = 3
POSITION_MODE_MAP = {
    PositionMode.ONEWAY: POSITION_MODE_API_ONEWAY,
    PositionMode.HEDGE: POSITION_MODE_API_HEDGE,
}

# REST API Public Endpoints
LINEAR_MARKET = "linear"
NON_LINEAR_MARKET = "non_linear"

# Covers: Spot / USDT perpetual / USDC contract / Inverse contract / Option
LATEST_SYMBOL_INFORMATION_ENDPOINT = {
    LINEAR_MARKET: "v5/market/tickers",
    NON_LINEAR_MARKET: "v5/market/tickers",
}

QUERY_SYMBOL_ENDPOINT = {
    LINEAR_MARKET: "v5/market/instruments-info",
    NON_LINEAR_MARKET: "v5/market/instruments-info",
}
ORDER_BOOK_ENDPOINT = {
    LINEAR_MARKET: "v5/market/orderbook",
    NON_LINEAR_MARKET: "v5/market/orderbook",
}
SERVER_TIME_PATH_URL = {
    LINEAR_MARKET: "v5/market/time",
    NON_LINEAR_MARKET: "v5/market/time",
}

# REST API Private Endpoints
SET_LEVERAGE_PATH_URL = {
    LINEAR_MARKET: "v5/position/set-leverage",
    NON_LINEAR_MARKET: "v5/position/set-leverage",
}
GET_LAST_FUNDING_RATE_PATH_URL = {
    LINEAR_MARKET: "v5/account/transaction-log",
    NON_LINEAR_MARKET: "v5/account/contract-transaction-log",
}
GET_POSITIONS_PATH_URL = {
    LINEAR_MARKET: "v5/position/list",
    NON_LINEAR_MARKET: "v5/position/list",
}
PLACE_ACTIVE_ORDER_PATH_URL = {
    LINEAR_MARKET: "v5/order/create",
    NON_LINEAR_MARKET: "v5/order/create",
}
CANCEL_ACTIVE_ORDER_PATH_URL = {
    LINEAR_MARKET: "v5/order/cancel",
    NON_LINEAR_MARKET: "v5/order/cancel",
}
QUERY_ACTIVE_ORDER_PATH_URL = {
    LINEAR_MARKET: "v5/order/realtime",
    NON_LINEAR_MARKET: "v5/order/realtime",
}
USER_TRADE_RECORDS_PATH_URL = {
    LINEAR_MARKET: "v5/execution/list",
    NON_LINEAR_MARKET: "v5/execution/list",
}
GET_WALLET_BALANCE_PATH_URL = {
    LINEAR_MARKET: "v5/account/wallet-balance",
    NON_LINEAR_MARKET: "v5/account/wallet-balance",
}
SET_POSITION_MODE_URL = {LINEAR_MARKET: "v5/position/switch-mode"}

# Funding Settlement Time Span
FUNDING_SETTLEMENT_DURATION = (
    5,
    5,
)  # seconds before snapshot, seconds after snapshot

# WebSocket Public Endpoints
WS_PING_REQUEST = "ping"
WS_TRADES_TOPIC = "publicTrade"
WS_ORDER_BOOK_EVENTS_TOPIC = "orderbook.200"
WS_INSTRUMENTS_INFO_TOPIC = "tickers"

# WebSocket Private Endpoints
WS_AUTHENTICATE_USER_ENDPOINT_NAME = "auth"
WS_SUBSCRIPTION_POSITIONS_ENDPOINT_NAME = "position"
WS_SUBSCRIPTION_ORDERS_ENDPOINT_NAME = "order"
WS_SUBSCRIPTION_EXECUTIONS_ENDPOINT_NAME = "execution"
WS_SUBSCRIPTION_WALLET_ENDPOINT_NAME = "wallet"

# Order Statuses
ORDER_STATE = {
    "Created": OrderState.OPEN,
    "New": OrderState.OPEN,
    "Filled": OrderState.FILLED,
    "PartiallyFilled": OrderState.PARTIALLY_FILLED,
    "Cancelled": OrderState.CANCELED,
    "PendingCancel": OrderState.PENDING_CANCEL,
    "Rejected": OrderState.FAILED,
}

GET_LIMIT_ID = "GETLimit"
POST_LIMIT_ID = "POSTLimit"
GET_RATE = 49  # per second
POST_RATE = 19  # per second

NON_LINEAR_PRIVATE_BUCKET_100_LIMIT_ID = "NonLinearPrivateBucket100"
NON_LINEAR_PRIVATE_BUCKET_600_LIMIT_ID = "NonLinearPrivateBucket600"
NON_LINEAR_PRIVATE_BUCKET_75_LIMIT_ID = "NonLinearPrivateBucket75"
NON_LINEAR_PRIVATE_BUCKET_120_B_LIMIT_ID = "NonLinearPrivateBucket120B"
NON_LINEAR_PRIVATE_BUCKET_120_C_LIMIT_ID = "NonLinearPrivateBucket120C"

LINEAR_PRIVATE_BUCKET_100_LIMIT_ID = "LinearPrivateBucket100"
LINEAR_PRIVATE_BUCKET_600_LIMIT_ID = "LinearPrivateBucket600"
LINEAR_PRIVATE_BUCKET_75_LIMIT_ID = "LinearPrivateBucket75"
LINEAR_PRIVATE_BUCKET_120_A_LIMIT_ID = "LinearPrivateBucket120A"

# Request error codes
RET_CODE_OK = 0

RET_CODE_MODE_POSITION_NOT_EMPTY = 110024
RET_CODE_MODE_NOT_MODIFIED = 110025
RET_CODE_MODE_ORDER_NOT_EMPTY = 110028
RET_CODE_HEDGE_NOT_SUPPORTED = 110029

RET_CODE_LEVERAGE_NOT_MODIFIED = 110043

RET_CODE_ORDER_NOT_EXISTS = 110001

RET_CODE_PARAMS_ERROR = 10001
RET_CODE_API_KEY_INVALID = 10003
RET_CODE_AUTH_TIMESTAMP_ERROR = 10021
RET_CODE_API_KEY_EXPIRED = 33004
RET_CODE_POSITION_ZERO = 130125
