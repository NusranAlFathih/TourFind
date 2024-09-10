import streamlit as st
import time
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
from PIL import Image

# Set the title of the application
st.title("Tourist Destination Finder with Sentiment Analysis")

# Sidebar for input widgets
st.sidebar.header("Search Options")

# 1. Sidebar Input Widgets (Text input for destination and slider for review count)
destination = st.sidebar.text_input("Enter Destination", "Paris")
review_count = st.sidebar.slider("Number of Reviews to Analyze", 1, 10, 5)

# 2. Media Display (Upload image relevant to the destination)
st.subheader(f"Upload an image of {destination}")
uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'png'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption=f"Image of {destination}")

# Simulating a list of tourist reviews (for simplicity)
sample_reviews = [
    "The place was beautiful and full of amazing sights!",
    "The service was terrible and the staff were rude.",
    "I had the best time of my life, I want to visit again!",
    "The weather was terrible, but the city was still charming.",
    "The food was amazing and the people were friendly."
]

# 3. Machine Learning Task: Sentiment Analysis
st.subheader(f"Sentiment Analysis of Tourist Reviews for {destination}")

def analyze_sentiment(review):
    analysis = TextBlob(review)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative"

# 4. Progress and Status Updates (Progress bar while processing reviews)
if st.button('Analyze Reviews'):
    progress = st.progress(0)
    sentiments = []
    
    for i in range(review_count):
        time.sleep(0.5)  # Simulating processing time
        progress.progress(int((i+1)/review_count * 100))
        sentiment = analyze_sentiment(sample_reviews[i % len(sample_reviews)])
        sentiments.append(sentiment)
    
    # Show status message after analysis
    st.success(f"Sentiment analysis completed for {review_count} reviews.")

    # 5. Graphs: Display the results with a bar chart
    sentiment_df = pd.DataFrame({
        'Review': [f"Review {i+1}" for i in range(review_count)],
        'Sentiment': sentiments
    })
    
    sentiment_summary = sentiment_df['Sentiment'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(sentiment_summary.index, sentiment_summary.values)
    ax.set_title('Sentiment Analysis Results')
    ax.set_ylabel('Number of Reviews')
    
    st.pyplot(fig)

# Footer text
st.write("Analyze tourist reviews to find out whether people had a positive or negative experience!")