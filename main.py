import pandas as pd

from experts.symbol_expert import interpret_symbols
from experts.emotion_expert import analyze_emotion
from experts.psychology_expert import interpret_psychology
from experts.culture_expert import cultural_context
from moegate.gating_network import gate_experts

# Load preprocessed dreams
df = pd.read_csv("data/dreambank_annotated.csv")

def analyze_dream(dream_text, tokens):
    symbols = interpret_symbols(tokens)
    emotion = analyze_emotion(dream_text)
    psychology = interpret_psychology(tokens)
    culture = cultural_context(tokens)

    final_result = gate_experts(symbols, emotion, psychology, culture)
    return final_result

# Test on the first dream
dream_text = df['report'][0]
tokens = eval(df['tokens'][0]) if isinstance(df['tokens'][0], str) else df['tokens'][0]
result = analyze_dream(dream_text, tokens)

print("Dream:")
print(dream_text)
print("\nAnalysis Result:")
print(result)
