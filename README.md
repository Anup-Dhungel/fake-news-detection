📰 Fake News Detection using Machine Learning
📌 Project Overview

This project is a Fake News Detection System built using Machine Learning.
It classifies news articles as Real 🟢 or Fake 🔴 based on their textual content.

The model is trained on a labeled dataset and deployed using Streamlit for an interactive user interface.

🚀 Features
Detects whether news is Real or Fake
Clean and simple Streamlit UI
Text preprocessing using NLP techniques
High accuracy using TF-IDF + Logistic Regression
Real-time prediction from user input
🧠 Machine Learning Approach
Text Cleaning (lowercase, remove punctuation, URLs, numbers)
Feature Extraction using TF-IDF Vectorizer
Model Used: Logistic Regression
Evaluation Metrics: Accuracy, Precision, Recall, F1-score
📂 Project Structure
fake_news_detection/
│
├── app.py                 # Streamlit app
├── model.jb              # Trained ML model
├── vectorizer.jb         # TF-IDF vectorizer
├── requirements.txt      # Dependencies
├── fake-news-detection.ipynb  # Training notebook (optional)
└── README.md
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
2. Create virtual environment
python -m venv fenv
fenv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the application
streamlit run app.py
💻 Usage
Enter or paste a news article
Click Analyze News
Get prediction:
✅ Real News
🚨 Fake News
📊 Example

Input:

The Federal Reserve kept interest rates unchanged...

Output:

✅ REAL NEWS

⚠️ Note
This model is trained on a specific dataset and may not generalize perfectly to all news sources.
Always verify critical information from trusted sources.
🛠️ Technologies Used
Python
Scikit-learn
Pandas, NumPy
Streamlit
NLP (TF-IDF)
👨‍💻 Author

Anup Dhungel

