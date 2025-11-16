# cbt_engine.py
from typing import Dict, List, Tuple

DISTORTIONS: Dict[str, Dict[str, List[str]]] = {
    "all-or-nothing": {
        "triggers": ["always", "never", "completely", "totally", "ruined"],
        "reframes": [
            "Perfection isn’t required; partial progress still matters.",
            "One setback doesn’t define the whole picture.",
        ],
        "questions": [
            "What evidence supports and contradicts this thought?",
            "If a friend said this, how would you respond kindly?",
        ],
    },
    "overgeneralization": {
        "triggers": ["every time", "nothing ever", "everyone", "no one"],
        "reframes": [
            "This happened now, but does it happen in every situation?",
            "List one exception to this thought.",
        ],
        "questions": [
            "When was the last time the outcome was different?",
            "Is there a more balanced way to describe this?",
        ],
    },
    "catastrophizing": {
        "triggers": ["disaster", "ruined", "can’t handle", "the end"],
        "reframes": [
            "Even if it’s hard, I can take it one step at a time.",
            "What’s the most likely (not worst) outcome?",
        ],
        "questions": [
            "If the worst happened, how would you cope?",
            "What’s a smaller action you can take right now?",
        ],
    },
    "mind-reading": {
        "triggers": ["they think", "everyone thinks", "people will judge"],
        "reframes": [
            "I can’t know what others think without evidence.",
            "Their thoughts aren’t facts; I’ll focus on my actions.",
        ],
        "questions": [
            "What proof do you have for what they think?",
            "Could there be a neutral explanation?",
        ],
    },
    "should-statements": {
        "triggers": ["should", "must", "have to"],
        "reframes": [
            "Preferences are healthier than rigid rules.",
            "It’s okay to be human and make mistakes.",
        ],
        "questions": [
            "What’s a kinder, flexible version of this rule?",
            "What would ‘good enough’ look like?",
        ],
    },
    "emotional-reasoning": {
        "triggers": ["I feel, so it is", "because I feel", "feels true"],
        "reframes": [
            "Feelings are valid signals, but not facts.",
            "Let’s check facts alongside feelings.",
        ],
        "questions": [
            "What facts support or challenge this feeling?",
            "What would change this feeling even 10%?",
        ],
    },
}

def detect_distortion(text: str) -> Tuple[str, Dict[str, List[str]]]:
    t = text.lower()
    # check multi-word trigger substrings
    for name, cfg in DISTORTIONS.items():
        if any(trigger in t for trigger in cfg["triggers"]):
            return name, cfg
    # fallback: none detected
    return "none", {
        "reframes": ["Try a balanced statement: what’s a fair middle ground?"],
        "questions": ["What’s the smallest helpful step you can take next?"],
    }

def cbt_reframe(text: str) -> Dict[str, object]:
    name, cfg = detect_distortion(text)
    return {
        "distortion": name,
        "reframes": cfg.get("reframes", []),
        "questions": cfg.get("questions", []),
    }
