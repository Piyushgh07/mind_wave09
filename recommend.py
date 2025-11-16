from typing import Dict

def recommend_action(emotion: str) -> Dict[str, str]:
    emotion = emotion.lower()
    if emotion in ["sadness", "depression", "hopelessness"]:
        return {
            "type": "CBT",
            "title": "Gentle Reframing",
            "message": "Try our guided CBT reflection — it helps you see today differently.",
            "link": "/chat",
        }
    elif emotion in ["anxiety", "fear", "nervousness"]:
        return {
            "type": "Game",
            "title": "Breathing Orb",
            "message": "Your breath controls your calm — try a 2-minute breathing orb session.",
            "link": "/games",
        }
    elif emotion in ["anger", "irritation"]:
        return {
            "type": "PSS",
            "title": "Stress Check",
            "message": "You seem tense — a quick PSS stress test can help you assess and reset.",
            "link": "/assessments",
        }
    else:
        return {
            "type": "Tip",
            "title": "Keep Journaling ✍️",
            "message": "Your emotional balance looks good today. Keep noting small wins!",
            "link": "/graph",
        }
