from textblob import TextBlob
from nrclex import NRCLex

def analyze_emotion(text, user_context=None):
    emotion = NRCLex(text)
    frequencies = emotion.affect_frequencies
    if frequencies:
        top_emotion = max(frequencies, key=frequencies.get)
        result = {"top_emotion": top_emotion, "scores": frequencies}
    else:
        result = {"top_emotion": "None", "scores": {}}
    if user_context:
        result["user_context"] = user_context
    return result
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive Emotion"
    elif polarity < 0:
        return "Negative Emotion"
    else:
        return "Neutral Emotion"