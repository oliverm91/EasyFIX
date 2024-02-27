from enum import Enum


class MarketDataTags(Enum):
    MDUpdateAction = '279'
    MDEntryType = '269'
    MDEntryPrice = '270'
    Currency = '15'
    MDEntrySize = '271'
    MDEntryTime = '273'
    TradingSessionID = '336'
    NoSides = '552'
    PriceDelta = '881'
    Text = '58'
    TradeID = '5463'
    ExpireDate = '432'

    PublicRate = '10150'
    AuctionID = '10167'
    MDMaturity = '10163'
    MDAdjustmentCurrency = '10159' # For MDEntryType=2 (TRADE)
    CoraMaturity = '10171'
    Duration = '10170'
    TIR = '10168' # For MDEntryType=2 (TRADE)
    LocalCurrencyValue = '10169' # For MDEntryType=2 (TRADE)
    SettlDate = '64' # For MDEntryType=2 (TRADE)
    Side = '54'

    LastFragment = '893'

    # TradeParties
    EnteringFirm = '10140'
    ExecutingFirm = '10141'
    EnteringTrader = '10142'
    FundManager = '10143'


md_tags_dict: dict[str, MarketDataTags] = {market_data_tag.value: market_data_tag for market_data_tag in MarketDataTags}
accepted_md_tags: str[str] = set(md_tags_dict.keys())
