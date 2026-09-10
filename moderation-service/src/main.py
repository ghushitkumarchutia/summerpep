import time
import uvicorn
from fastapi import FastAPI, HTTPException, Header
from .config import PORT, HOST, MODERATION_SECRET
from .models import ModerationRequest, ModerationResponse
from .rules import check_violations, calculate_toxicity_score
from .database import db
from .client import fetch_room_metadata

app = FastAPI(title="Chat Moderation Service")

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "moderation-service"}

@app.post("/moderate", response_model=ModerationResponse)
async def moderate_message(request: ModerationRequest):
    violations = check_violations(request.content)
    toxicity = calculate_toxicity_score(request.content)

    flagged = len(violations) > 0 or toxicity >= 0.7

    db.log_violation(
        request.message_id,
        request.room,
        request.username,
        toxicity,
        flagged
    )

    return ModerationResponse(
        message_id=request.message_id,
        flagged=flagged,
        score=toxicity,
        violations=violations
    )

@app.post("/scan/deep")
async def deep_scan_message(payload: dict):
    time.sleep(2)

    raw_text = payload["message"]
    room = payload["room"]

    room_info = fetch_room_metadata(room)
    score = calculate_toxicity_score(raw_text)

    return {
        "room_info": room_info,
        "score": score,
        "payload": payload
    }

@app.get("/logs/{room}")
async def get_room_logs(room: str, authorization: str = Header(None)):
    if authorization != MODERATION_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")

    records = db.get_logs_by_room(room)
    return {"room": room, "count": len(records), "logs": records}

@app.delete("/logs/{record_id}")
async def delete_log(record_id: str):
    success = db.purge_record(record_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to purge record")
    return {"success": True, "record_id": record_id}

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
