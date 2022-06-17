from pydantic import BaseModel
from typing import Optional, List

class ResultSettlementMessage(BaseModel):
    id: str
    selection_status: str
    odd_id: str
    market_id: str
    event_id: str
    market_type_id: Optional[str]
    sport_id: Optional[str]
    league_id: Optional[str]
    foreign_key: Optional[str]
    timestamp: Optional[int]

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
            selection_status=obj.get('selectionStatus'),
            odd_id=obj.get('oddId'),
            market_id=obj.get('marketId', None),
            event_id=obj.get('eventId', None),
            market_type_id=obj.get('marketTypeId', None),
            sport_id=obj.get('sportId', None),
            league_id=obj.get('leagueId', None),
            foreign_key=obj.get('foreignKey', None),
            timestamp=obj.get('timestamp', None)
        )

        return result_settlement