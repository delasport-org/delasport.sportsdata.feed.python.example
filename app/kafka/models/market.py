from pydantic import BaseModel
from typing import Optional, List


class Odd(BaseModel):
    id: str
    key: Optional[str]
    value: Optional[str]

    """
    Converts object literal(dict) to a Clock instance.
    Args:
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
    obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj: dict):
        if obj is None:
            return None

        return Odd(
            id=obj.get('id', None),
            key=obj.get('key', None),
            value=obj.get('value', None),
        )


class MarketMessage(BaseModel):
    id: str
    event_id: str
    invalidated_at: Optional[str]
    market_type_id: Optional[str]
    game_period_id: Optional[str]
    line_entity_id: Optional[str]
    market_key: Optional[str]
    spread: Optional[float]
    index: Optional[int]
    is_hidden: Optional[int]
    is_suspended: Optional[int]
    odds: List[Odd] = []

    @staticmethod
    def from_dict(obj, ctx):
        market = MarketMessage(
            id=obj.get('id'),
            event_id=obj.get('eventId', None),
            invalidated_at=obj.get('invalidatedAt', None),
            market_type_id=obj.get('marketTypeId', None),
            game_period_id=obj.get('gamePeriodId', None),
            line_entity_id=obj.get('lineEntityId', None),
            market_key=obj.get('marketKey', None),
            spread=obj.get('spread', None),
            index=obj.get('index', None),
            is_hidden=obj.get('isHidden', None),
            is_suspended=obj.get('isSuspended', None)
        )

        for odd in obj.get('odds', []):
            market.odds.append(Odd.from_dict(odd))

        return market

