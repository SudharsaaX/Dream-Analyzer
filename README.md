# Dream Analyzer

**An AI-powered application for interpreting dream narratives.**

Dream Analyzer is a Streamlit-based web application that analyzes user-submitted dream descriptions using Natural Language Processing (NLP) techniques. It offers insights through emotional, symbolic, and cultural analysis, and provides visualizations along with relevant book and podcast recommendations.

---

## Features

- **Emotion Detection**: Uses NRCLex and TextBlob to identify emotional content such as joy, fear, anger, and sadness.
- **Symbol Interpretation**: Extracts and interprets symbols and themes from dream text.
- **Cultural Context Analysis**: Considers cultural elements in the interpretation process.
- **Visual Insights**: Presents word clouds and pie charts to highlight key findings.
- **Personalized Recommendations**: Suggests relevant books and podcasts based on the dream content.
- **Modular Architecture**: Built with a rule-based, explainable structure for transparency.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP Libraries**: NLTK, TextBlob, NRCLex
- **Visualization**: Matplotlib, WordCloud

---

## Project Structure

```
Dream-Analyzer/
├── assets/                 # Image and visualization assets
├── data/                   # Datasets and CSV files
├── experts/                # Rule-based expert system
├── moegate/                # External integrations
├── preprocessing/          # Data cleaning and preprocessing scripts
├── dashboard.py            # Main Streamlit app script
├── main.py                 # Execution script
├── model.ipynb             # Jupyter notebook for model experimentation
├── requirements.txt        # Python dependency list
└── README.md               # Project documentation
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SudharsaaX/Dream-Analyzer.git
cd Dream-Analyzer
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or macOS
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Launch the application:

```bash
streamlit run dashboard.py
```

2. Open a browser and visit: `http://localhost:8501/`

3. Enter a dream description in the input field to receive a detailed analysis.

---

## Output Examples

- **Word Cloud**: Displays the most frequent words used in the dream.
- **Emotion Pie Chart**: Shows the distribution of emotional tones.
- **Recommendations**: Provides related books and podcasts.

---

## Screenshots

> Place the following images in the `/assets/` directory.

| Word Cloud | Interpretation | Recommendations |
|------------|----------------|------------------|
| ![WordCloud](assets/wordcloud.png) | ![Interpretation](assets/interpretation.png) | ![Recommendations](assets/recommendations.png) |

---

## Data Sources

- DreamBank Annotated Dataset
- Manually curated expert rules and references

---

## Contributing

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes:

```bash
git commit -m "Add YourFeature"
```

4. Push to your branch:

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to [@Tamil157](https://github.com/Tamil157) for contributions and support.
