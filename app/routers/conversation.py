# app/routers/conversation.py

from fastapi import APIRouter
from app.models.schemas import (
    EventInput,
    ConversationRequest,
    ConversationResponse,
    FactCheckRequest,
    FactCheckResponse,
)

from app.services import (
    event_analyzer,
    topic_generator,
    fact_checker,
    history_logger,
)

router = APIRouter()


@router.post("/analyze-event")
def analyze_event(data: EventInput):
    themes = event_analyzer.extract_event_themes(data.description)
    return {"topics": themes}


@router.post("/fact-check", response_model=FactCheckResponse)
def fact_check(data: FactCheckRequest):
    summary = fact_checker.fact_check(data.query)
    return FactCheckResponse(summary=summary)


@router.post("/generate-conversation", response_model=ConversationResponse)
def generate_conversation(data: ConversationRequest):
    # Extract event themes
    themes = event_analyzer.extract_event_themes(data.description)

    # Generate conversation starters
    suggestions = topic_generator.generate_topics(
        themes,
        data.interests
    )

    # Save conversation history
    history_logger.log_conversation({
        "description": data.description,
        "interests": data.interests,
        "topics": themes,
        "suggestions": suggestions
    })

    # Return response
    return ConversationResponse(
        topics=themes,
        suggestions=suggestions
    ) 