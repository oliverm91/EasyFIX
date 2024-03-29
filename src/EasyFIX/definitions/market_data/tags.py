from enum import Enum


class MDTags(Enum):
    MDReqID = '262'
    NoMDEntries = '268'

    MDUpdateAction = '279'
    MDEntryType = '269'
    MDEntryID = '278'
    MDEntryRefID = '280'
    MDEntryPx = '270'
    BookingRefID = '466'
    Currency = '15'
    Symbol = '55'
    PaymentCurreny = '10225'
    MDEntrySize = '271'
    MDEntryDate = '272'
    MDEntryTime = '273'
    TradeCondition = '277'
    SecurityType = '167'
    MDEntryOriginator = '282' # For MDEntryType=2 (TRADE)
    ExpireTime = '126'
    OrderID = '37'
    MDEntryBuyer = '288' # For MDEntryType=2 (TRADE)
    MDEntrySeller = '289' # For MDEntryType=2 (TRADE)
    
    MaturityDate = '541'
    MDentryPositionNo = '290'
    PriceDelta = '881'
    Text = '58'
    TradeID = '5463'
    ClOrdID = '11'
    ExpireDate = '432'

    MDMaturity = '10163'
    MDAdjustmentCurrency = '10159' # For MDEntryType=2 (TRADE)
    Duration = '10170'
    TIR = '10168' # For MDEntryType=2 (TRADE)
    LocalCurrencyValue = '10169' # For MDEntryType=2 (TRADE)
    ValuedAmount = '10175'
    
    LastFragment = '893'

    #Repeating groups
    # For MDEntryType=2 (TRADE)
    NoSides = '552'
    # TradeParties
    Side = '54'
    EnteringFirm = '10140'
    ExecutingFirm = '10141'
    EnteringTrader = '10142'
    FundManager = '10143'

    #Repeating groups
    # For Bid and offer, MDUpdateAction.New
    NoPartyID = '453'
    # Parties
    PartyID = '448'
    PartyIDSource = '447'
    PartyRole = '452'



md_tags_dict: dict[str, MDTags] = {market_data_tag.value.encode(): market_data_tag for market_data_tag in MDTags}
accepted_md_tags: set[str] = set(md_tags_dict.keys())


class MDRepeatingGroupConfiguration:
    def __init__(self, repeating_tags: list[MDTags], group_starter_tag: MDTags):
        self.repeating_tags = repeating_tags
        if group_starter_tag not in self.repeating_tags:
            raise ValueError(f'Group starter tag {group_starter_tag} not in repeating rags.')
        self.group_starter_tag = group_starter_tag

repeating_group_configurations: dict[MDTags: MDRepeatingGroupConfiguration] = {
    MDTags.NoSides: MDRepeatingGroupConfiguration([
                                    MDTags.Side, # Starter Tag
                                    MDTags.EnteringFirm,
                                    MDTags.ExecutingFirm,
                                    MDTags.EnteringTrader,
                                    MDTags.FundManager
                                  ],
                                  MDTags.Side),
    MDTags.NoPartyID: MDRepeatingGroupConfiguration([
                                    MDTags.PartyID, # Starter Tag
                                    MDTags.PartyIDSource,
                                    MDTags.PartyRole
                                  ],
                                  MDTags.PartyID),
}