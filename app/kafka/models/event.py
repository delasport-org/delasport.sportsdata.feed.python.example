from pydantic import BaseModel
from typing import Optional, List


class Country(BaseModel):
    id: Optional[str]
    title: Optional[str]

    """
    Converts object literal(dict) to a Country instance.
    Args:
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
        obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj: dict) -> object:
        if obj is None:
            return None

        return Country(
            id=obj.get('id', None),
            title=obj.get('title', None)
        )


class Sport(BaseModel):
    id: Optional[str]
    title: Optional[str]
    key: Optional[str]

    """
        Converts object literal(dict) to a Sport instance.
        Args:
            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.
            obj (dict): Object literal(dict)
        """
    @staticmethod
    def from_dict(obj: dict) -> object:
        if obj is None:
            return None

        return Sport(
            id=obj.get('id', None),
            title=obj.get('title', None),
            key=obj.get('key', None)
        )


class League(BaseModel):
    id: Optional[str]
    title: Optional[str]
    format: Optional[str]

    """
    Converts object literal(dict) to a League instance.
    Args:
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
        obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj: dict) -> object:
        if obj is None:
            return None

        return League(
            id=obj.get('id', None),
            title=obj.get('title', None),
            format=obj.get('format', None)
        )


class Clock(BaseModel):
    start_timestamp: Optional[int]
    start_second: Optional[int]
    is_stopped: Optional[bool]
    is_countdown: Optional[bool]

    """
    Converts object literal(dict) to a Clock instance.
    Args:
       ctx (SerializationContext): Metadata pertaining to the serialization
           operation.
       obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj: dict) -> object:
        if obj is None:
            return None

        return Clock(
            start_timestamp=obj.get('startTimestamp', None),
            start_second=obj.get('startSecond', None),
            is_stopped=obj.get('isStopped', None),
            is_countdown=obj.get('isCountdown', None),
        )


class Team(BaseModel):
    id: Optional[str]
    name: Optional[str]
    color: Optional[str]

    """
    Converts object literal(dict) to a Clock instance.
    Args:
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
    obj (dict): Object literal(dict)
    """
    @staticmethod
    def from_dict(obj: dict) -> object:
        if obj is None:
            return None

        return Team(
            id=obj.get('id', None),
            name=obj.get('name', None),
            color=obj.get('color', None),
        )


class LiveScore(BaseModel):
    line_entity_id: str
    line_entity_name: str
    game_period_id: str
    game_period_name: str
    home_team: str
    away_team: str

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

        return LiveScore(
            line_entity_id=obj.get('lineEntityId', None),
            line_entity_name=obj.get('lineEntityName', None),
            game_period_id=obj.get('gamePeriodId', None),
            game_period_name=obj.get('gamePeriodName', None),
            home_team=obj.get('homeTeam', None),
            away_team=obj.get('awayTeam', None),
        )


class EventMessage(BaseModel):
    id: str
    state: Optional[str] = None
    status: Optional[str] = None
    live_game_period: Optional[str] = None
    live_minute: Optional[str] = None
    market_count: Optional[int] = None
    start_date: Optional[str] = None
    has_live_streaming: Optional[bool] = None
    invalidated_at: Optional[str] = None
    time_range: Optional[str] = None
    country: Optional[Country] = None
    sport: Optional[Sport] = None
    league: Optional[League] = None
    clock: Optional[Clock] = None
    away_team: Optional[Team] = None
    home_team: Optional[Team] = None
    live_scores: List[LiveScore] = []

    @staticmethod
    def from_dict(obj, ctx):
        event = EventMessage(
            id=obj.get('id', None),
            state=obj.get('state', None),
            status=obj.get('status', None),
            live_game_period=obj.get('liveGamePeriod', None),
            live_minute=obj.get('liveMinute', None),
            market_count=obj.get('marketCount', None),
            start_date=obj.get('startDate', None),
            has_live_streaming=obj.get('hasLiveStreaming', None),
            invalidated_at=obj.get('invalidatedAt', None),
            time_range=obj.get('timeRange', None),
            country=Country.from_dict(obj.get('country', None)),
            sport=Sport.from_dict(obj.get('sport', None)),
            league=League.from_dict(obj.get('league', None)),
            clock=Clock.from_dict(obj.get('clock', None)),
            awayTeam=Team.from_dict(obj.get('awayTeam', None)),
            homeTeam=Team.from_dict(obj.get('homeTeam', None))
        )

        for score in obj.get('liveScores', []):
            event.live_scores.append(LiveScore.from_dict(score))

        return event
