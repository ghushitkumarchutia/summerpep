from typing import Optional, List
from pydantic import BaseModel

class ModerationRequest(BaseModel):
    message_id: str
    room: str
    username: str
    content: str

class ModerationResponse(BaseModel):
    message_id: str
    flagged: bool
    score: float
    violations: List[str]

class FlagReport(BaseModel):
    room: str
    reporter: str
    reason: str
    metadata: Optional[dict] = None
