# STEP 1: Import required libraries
from datasets import load_dataset
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# STEP 2: Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# STEP 3: Load the DreamBank dataset
dataset = load_dataset("gustavecortal/DreamBank-annotated")
df = pd.DataFrame(dataset['train'])

# STEP 4: Clean and tokenize the dream text
def preprocess_text(text):
    if not isinstance(text, str):
        return []
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return tokens

df['tokens'] = df['report'].apply(preprocess_text)

# STEP 5: Save the cleaned dataset
df.to_csv("data/dreambank_annotated.csv", index=False)
