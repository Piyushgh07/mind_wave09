from transformers import pipeline
import random


print("Loading emotion model…")
emotion_model = pipeline(
    "text-classification",
    model="joeddav/distilbert-base-uncased-go-emotions-student",
    framework="pt",
    top_k=None
)

print("Loading stress/toxicity model…")
stress_model = pipeline(
    "text-classification",
    model="s-nlp/roberta_toxicity_classifier",
    framework="pt",
    top_k=None
)

print("Models loaded on CPU ✅")


def full_emotion_analysis(text: str):
    """Run multi-model emotional + stress + crisis analysis."""

   
    emo_pred = emotion_model(text)[0]
    emo_sorted = sorted(emo_pred, key=lambda x: x["score"], reverse=True)
    top_emotion = emo_sorted[0]["label"]
    confidence = float(emo_sorted[0]["score"])

    
    stress_pred = stress_model(text)[0]
    stress_sorted = sorted(stress_pred, key=lambda x: x["score"], reverse=True)
    stress_label = stress_sorted[0]["label"]
    stress_conf = float(stress_sorted[0]["score"])

    stress_level = (
        stress_conf if stress_label.lower() in ["toxic", "severe_toxic", "obscene"] else 0.2
    )

    
    crisis_flag = any(k in text.lower() for k in ["suicide", "kill myself", "end my life"])
    crisis = {
        "flag": crisis_flag,
        "helplines": [
            "📞 National Helpline: 9152987821 (AASRA, India)",
            "💬 Text ‘HELLO’ to 741741 (India Mental Health Line)",
        ] if crisis_flag else [],
    }

    return {
        "emotion": top_emotion,
        "confidence": confidence,
        "stress_level": round(stress_level, 3),
        "crisis": crisis,
    }


def forecast_next():
    """Simulate mood forecast until ML predictor is trained."""
    moods = ["happiness", "calm", "neutral", "sadness", "anxiety"]
    return random.choice(moods)
