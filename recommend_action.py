def recommend_action(emotion: str):
    if emotion in ["sadness", "anger"]:
        return {"title": "Calm Reset", "message": "🧘 Try a 2-min Breathing Orb session."}
    elif emotion == "anxiety":
        return {"title": "Check-in", "message": "🧩 Consider a quick GAD-7 self-check."}
    elif emotion == "neutral":
        return {"title": "Reflection", "message": "💬 Talk with MindWave about your day — small chats help clarity."}
    elif emotion == "calm":
        return {"title": "Keep the Flow", "message": "🎮 Play Focus Maze to stay in that calm rhythm."}
    else:
        return {"title": "Mindful Break", "message": "🌱 Step outside, hydrate, and reset your mind for a bit."}
