# safety.py
import re

HELPLINES = [
    "India: Kiran (24x7) 1800-599-0019",
    "India: AASRA 24x7 +91-9820466726",
    "Global list: https://www.opencounseling.com/suicide-hotlines",
]

TRIGGERS = [
    r"\bkill myself\b",
    r"\bsuicide\b",
    r"\bend my life\b",
    r"\bno reason to live\b",
    r"\bself[- ]harm\b",
    r"\bhurt myself\b",
]

def crisis_check(text: str):
    t = text.lower()
    hit = any(re.search(p, t) for p in TRIGGERS)
    return {
        "flag": hit,
        "message": "Potential self-harm indicators detected." if hit else "",
        "helplines": HELPLINES if hit else [],
    }
