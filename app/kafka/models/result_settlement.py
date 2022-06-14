from pydantic import BaseModel
from typing import Optional, List


class Odd(BaseModel):
    id: str
    selectionStatus: str

    """
    Converts object literal(dict) to a Odd instance.
    Args:
        obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj: dict):
        if obj is None:
            return None

        return Odd(
            id=obj.get('id', None),
            selection_status=obj.get('selectionStatus', None),
        )

class ResultSettlementMessage(BaseModel):
    id: str
    event_id: str
    market_type_id: Optional[str]
    sport_id: Optional[str]
    league_id: Optional[str]
    foreign_key: Optional[str]
    timestamp: Optional[int]
    odds: List[Odd] = []

    """
    Converts object literal(dict) to a ResultSettlementMessage instance.
    Args:
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
        obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj, ctx):
        result_settlement = ResultSettlementMessage(
            id=obj.get('id'),
            event_id=obj.get('eventId', None),
            market_type_id=obj.get('marketTypeId', None),
            sport_id=obj.get('sportId', None),
            league_id=obj.get('leagueId', None),
            foreign_key=obj.get('foreignKey', None),
            timestamp=obj.get('timestamp', None),
        )

        for odd in obj.get('odds', []):
            result_settlement.odds.append(Odd.from_dict(odd))

        return result_settlement