# TourFind


Tourist Destination Finder with Sentiment Analysis

Overview
This project is a Streamlit application that allows users to explore tourist destinations and analyze sentiment from reviews. The app includes functionality for image uploads, sentiment analysis of reviews, and visualizing the results with a bar chart.

Features
•	Destination Input: Enter a tourist destination to analyze.
•	Review Analysis: Input the number of reviews to analyze.
•	Media Display: Upload and display an image related to the destination.
•	Sentiment Analysis: Analyze sentiment of sample reviews using TextBlob.
•	Progress Indicator: Show a progress bar while processing reviews.
•	Visualization: Display a bar chart of sentiment analysis results.

 Installation

Prerequisites
Ensure you have [Anaconda](https://www.anaconda.com/products/distribution) and [VS Code](https://code.visualstudio.com/) installed.



Setup

1. Clone the repository
bash
   git clone https://github.com/your-username/your-repository.git

2. Navigate to the project directory
  bash
   cd your-repository

3. Create and activate a Conda environment
   bash
   conda create -n streamlit_env python=3.9
   conda activate streamlit_env

4. Install required packages
   bash
   pip install streamlit textblob pillow matplotlib pandas

 Running the App
1. Open VS Code and navigate to the project directory.
2. Open the terminal in VS Code (press `Ctrl + \``).
3. Run the Streamlit app
  bash
   streamlit run tourist_destination_finder.py

4. Access the app in your browser at `http://localhost:8501`.

 Usage
1. Enter a destination in the sidebar.
2. Choose the number of reviews to analyze using the slider.
3. Upload an image related to the destination (optional).
4. Click the "Analyze Reviews" button to perform sentiment analysis.
5. View the sentiment analysis results and the bar chart.

Contributing

If you would like to contribute to this project, please fork the repository and create a pull request. 

