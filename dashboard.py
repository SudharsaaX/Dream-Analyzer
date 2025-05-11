import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import sys
import base64

# Set page configuration to wide mode and add custom title/icon
st.set_page_config(
    page_title="Dream Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

from experts.symbol_expert import interpret_symbols
from experts.emotion_expert import analyze_emotion
from experts.psychology_expert import interpret_psychology
from experts.culture_expert import cultural_context
from experts.recommendations import get_book_recommendations, get_podcast_recommendations
from moegate.gating_network import gate_experts
from preprocessing.preprocess import preprocess_text

# Custom CSS to make the app more visually appealing
def local_css():
    st.markdown("""
    <style>
        .main {padding: 0rem 1rem !important;}
        .stApp {max-width: 100% !important;}
        h1 {color: #4b2e83; text-align: center; margin-bottom: 2rem;}
        h2 {color: #4b2e83; margin-top: 2rem;}
        h3 {color: #4b2e83;}
        .stExpander {border: 1px solid #e6e6e6; border-radius: 5px;}
        .stRadio > div {flex-direction: row;}
        .stRadio label {margin-right: 15px;}
        .stTextArea {height: 150px;}
        
        /* Dream Text Section */
        .dream-card {background-color: #e6f7ff; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #1890ff; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        /* Dream Context Section */
        .context-section {background-color: #fff7e6; padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #fa8c16; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        /* Word Cloud Section */
        .wordcloud-section {background-color: #f6ffed; padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #52c41a; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        /* Dream Analysis Results Section */
        .interpretation-card {background-color: #f9f0ff; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #722ed1; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        /* Expert Contributions Section */
        .expert-section {background-color: #fff0f6; padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #eb2f96; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        /* Book Recommendations Section */
        .book-card {background-color: #e6fffb; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #13c2c2; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        /* Podcast Recommendations Section */
        .podcast-card {background-color: #fcffe6; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #a0d911; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
        
        .sidebar-content {padding: 20px;}
        .stButton>button {width: 100%;}
    </style>
    """, unsafe_allow_html=True)

# Apply custom CSS
local_css()

# Load dream data
try:
    df = pd.read_csv("data/dreambank_annotated.csv")
except FileNotFoundError:
    try:
        df = pd.read_csv("dreambank_annotated.csv")
    except FileNotFoundError:
        st.sidebar.error("Dream dataset not found. Please ensure the CSV file exists.")
        df = pd.DataFrame(columns=['report', 'tokens'])

# Sidebar for navigation and controls
with st.sidebar:
    st.title("Dream Analyzer")
    st.markdown("---")
    
    st.subheader("Input Options")
    option = st.radio("Choose dream input method", ("Select from list", "Type your own"))
    
    if option == "Select from list" and not df.empty:
        dream_index = st.slider("Select a dream number", 0, len(df)-1, 0)
        dream_text = df['report'][dream_index]
        try:
            tokens = eval(df['tokens'][dream_index]) if isinstance(df['tokens'][dream_index], str) else df['tokens'][dream_index]
        except:
            tokens = preprocess_text(dream_text)
    else:
        dream_text = st.text_area("Type your dream text here", "")
        tokens = preprocess_text(dream_text) if dream_text else []  # Or run your tokenizer if available
    
    st.markdown("---")
    st.subheader("About")
    st.info("""
    ### Dream Analyzer
    This application analyzes dreams using advanced AI models to provide personalized insights:
    
    **Features:**
    - Personalized dream analysis
    - Book and podcast recommendations
    - Visual representation of dream elements
    
    **Created by:**
    Sudharsan and Tamilarasan
    
    NLP Project - 2025
    """)

# Main content area
st.title("AI-Powered Dream Analyzer")

# Dream text display in a card-like container
st.markdown("<div class='dream-card'>", unsafe_allow_html=True)
st.subheader("Dream Text")
st.write(dream_text)
st.markdown("</div>", unsafe_allow_html=True)

# Three-column layout for clarifying questions, word cloud, and interpretation
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # --- Dream Context Questions Section ---
    st.markdown("<div class='context-section'>", unsafe_allow_html=True)
    st.subheader("Dream Context: Share additional details about your dream")
    clarifying_questions = [
        "How did the dream make you feel?",
        "Were there any recurring symbols or themes?",
        "Did you recognize any people or places?",
        "Did you wake up with any strong emotions?",
        "Is there anything in your life that you think relates to this dream?",
        "Did the dream have a clear narrative or was it fragmented?",
        "Were there any colors that stood out in your dream?",
        "Have you had similar dreams before?"
    ]

    if 'clarify_answers' not in st.session_state:
        st.session_state['clarify_answers'] = {}

    # Display all questions directly (not in an expander)
    for q in clarifying_questions:
        st.session_state['clarify_answers'][q] = st.text_input(q, value=st.session_state['clarify_answers'].get(q, ""))

    # Optionally enrich context with clarifying answers
    user_context = {k: v for k, v in st.session_state['clarify_answers'].items() if v.strip()}
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Word Cloud visualization (if dream text is provided)
    if dream_text and tokens:
        st.markdown("<div class='wordcloud-section'>", unsafe_allow_html=True)
        st.subheader("Word Cloud of Keywords")
        wordcloud = WordCloud(width=400, height=300, background_color='white', colormap='viridis').generate(" ".join(tokens))
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

# Run expert models if dream text is provided
if dream_text:
    try:
        # Create a spinner to show loading state
        with st.spinner("Analyzing your dream..."): 
            symbols = interpret_symbols(tokens, user_context if user_context else None)
            emotion = analyze_emotion(dream_text, user_context if user_context else None)
            psychology = interpret_psychology(tokens, user_context if user_context else None)
            culture = cultural_context(tokens, user_context if user_context else None)

            if user_context:
                result = gate_experts(symbols, emotion, psychology, culture, user_context)
            else:
                result = gate_experts(symbols, emotion, psychology, culture)
        
        # Display interpretation in a card-like container in the third column
        with col3:
            st.markdown("<div class='interpretation-card'>", unsafe_allow_html=True)
            st.subheader("Dream Analysis Results")
            st.json(result)
            st.markdown("</div>", unsafe_allow_html=True)

        # Pie chart of expert contributions in the second column (next to word cloud)
        if result:
            with col2:
                st.markdown("<div class='expert-section'>", unsafe_allow_html=True)
                labels = list(result.keys())
                sizes = [len(str(result[k])) for k in result]  # Use string length as a measure of contribution

                st.subheader("Expert Contributions")
                fig2, ax2 = plt.subplots(figsize=(4, 4))
                ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
                        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
                ax2.axis('equal')
                st.pyplot(fig2)
                st.markdown("</div>", unsafe_allow_html=True)
                
        # Get book and podcast recommendations based on interpretation and dream text
        # Add dream text to the interpretation dictionary
        interpretation_with_dream = result.copy()
        interpretation_with_dream['dream_text'] = dream_text
        
        # Get recommendations with the enhanced interpretation
        book_recommendations = get_book_recommendations(interpretation_with_dream)
        podcast_recommendations = get_podcast_recommendations(interpretation_with_dream)
        
        # Display recommendations in two separate container boxes
        st.subheader("Recommendations Based on Your Dream")
        
        # Create two columns for book and podcast recommendations
        book_col, podcast_col = st.columns(2)
        
        # Book recommendations in left column
        with book_col:
            st.markdown("<div class='book-card' style='height:100%;'>", unsafe_allow_html=True)
            st.markdown("### 📚 Book Recommendations")
            if book_recommendations:
                for i, book in enumerate(book_recommendations):
                    with st.container():
                        st.markdown(f"**{book['title']}** by {book['author']}")
                        st.markdown(f"*{book['description']}*")
                        
                        # Display dream relevance information from the recommendation
                        if 'dream_relevance' in book:
                            st.markdown(f"**Relevance to your dream:** *{book['dream_relevance']}*")
                        # Fallback to the previous method if dream_relevance is not available
                        elif 'symbols' in result and any(symbol.lower() in book['description'].lower() for symbol in str(result['symbols']).split()):
                            matching_symbols = [symbol for symbol in str(result['symbols']).split() if symbol.lower() in book['description'].lower()]
                            st.markdown(f"**Relevance to your dream:** This book relates to the *{', '.join(matching_symbols)}* symbols in your dream.")
                        elif 'emotion' in result and any(emotion.lower() in book['description'].lower() for emotion in str(result['emotion']).split()):
                            matching_emotions = [emotion for emotion in str(result['emotion']).split() if emotion.lower() in book['description'].lower()]
                            st.markdown(f"**Relevance to your dream:** This book connects with the *{', '.join(matching_emotions)}* emotions in your dream.")
                        else:
                            st.markdown("**Relevance to your dream:** This book addresses themes present in your dream interpretation.")
                            
                        if i < len(book_recommendations) - 1:
                            st.markdown("---")
            else:
                st.info("No specific book recommendations found for this dream interpretation.")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Podcast recommendations in right column
        with podcast_col:
            st.markdown("<div class='podcast-card' style='height:100%;'>", unsafe_allow_html=True)
            st.markdown("### 🎧 Podcast Recommendations")
            if podcast_recommendations:
                for i, podcast in enumerate(podcast_recommendations):
                    with st.container():
                        st.markdown(f"**{podcast['title']}** hosted by {podcast['host']}")
                        st.markdown(f"*{podcast['description']}*")
                        
                        # Display dream relevance information from the recommendation
                        if 'dream_relevance' in podcast:
                            st.markdown(f"**Relevance to your dream:** *{podcast['dream_relevance']}*")
                        # Fallback to the previous method if dream_relevance is not available
                        elif 'symbols' in result and any(symbol.lower() in podcast['description'].lower() for symbol in str(result['symbols']).split()):
                            matching_symbols = [symbol for symbol in str(result['symbols']).split() if symbol.lower() in podcast['description'].lower()]
                            st.markdown(f"**Relevance to your dream:** This podcast explores the *{', '.join(matching_symbols)}* symbols in your dream.")
                        elif 'emotion' in result and any(emotion.lower() in podcast['description'].lower() for emotion in str(result['emotion']).split()):
                            matching_emotions = [emotion for emotion in str(result['emotion']).split() if emotion.lower() in podcast['description'].lower()]
                            st.markdown(f"**Relevance to your dream:** This podcast discusses the *{', '.join(matching_emotions)}* emotions in your dream.")
                        elif 'culture' in result and any(cultural_element.lower() in podcast['description'].lower() for cultural_element in str(result['culture']).split()):
                            matching_cultural = [cultural_element for cultural_element in str(result['culture']).split() if cultural_element.lower() in podcast['description'].lower()]
                            st.markdown(f"**Relevance to your dream:** This podcast relates to the *{', '.join(matching_cultural)}* cultural elements in your dream.")
                        else:
                            st.markdown("**Relevance to your dream:** This podcast covers themes connected to your dream interpretation.")
                            
                        if i < len(podcast_recommendations) - 1:
                            st.markdown("---")
            else:
                st.info("No specific podcast recommendations found for this dream interpretation.")
            st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error during dream analysis: {str(e)}")
else:
    st.info("Please enter or select a dream to analyze.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 10px;'>Dream Analyzer | Created by Sudharsan and Tamilarasan | NLP Project 2023</div>
""", unsafe_allow_html=True)
