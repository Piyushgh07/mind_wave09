# interventions.py
from typing import List, Dict

BASE: Dict[str, List[str]] = {
    "joy": ["Savor the moment for 30s", "Share gratitude with someone"],
    "neutral": ["3 mindful breaths", "Hydrate and stretch"],
    "sadness": ["List 3 small wins", "Short daylight walk (5 min)"],
    "anxiety": ["4-7-8 breathing (2 min)", "5-4-3-2-1 grounding"],
    "anger": ["Box breathing 4-4-4-4", "10 wall push-ups / quick discharge"],
    "fear": ["Safe-place visualization", "Write evidence for/against fear"],
}

def suggest_for(emotion: str) -> List[str]:
    return BASE.get(emotion, BASE["neutral"])
