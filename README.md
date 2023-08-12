# **Phishing URL Detection Website**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/Flask-2.1%2B-red.svg)
![License](https://img.shields.io/github/license/ArnavK-09/phishing-detection)

## 📚 Overview

This repository contains a FastAPI-based web API that helps determine if a URL is bad (potentially phishing) or good (not malicious). The API uses a Machine Learning model trained on a dataset of over 4,000 URLs, categorizing them as "bad" or "good".

The model is based on a Logistic Regression classifier using the Term Frequency-Inverse Document Frequency (TF-IDF) vectorizer for text representation. It has been pre-trained on the provided dataset of URLs and can quickly classify new URLs.

## 🚚 Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/phishing-url-detection.git
cd phishing-url-detection
```

2. Install the required dependencies using `pip`:

```bash
pip install flask pandas scikit-learn gunicorn
```


## 🖥️ Using Website or API

1. Prepare your dataset:
   - Ensure you have a CSV file named `data/main.csv` containing the list of URLs to be categorized.
   - The CSV file should have two columns: `URL` (containing the URLs) and `Label` (with values "bad" or "good" indicating the classification).

2. Prepare Model with Dataset

```bash
python3 model.py
````

3. Start the Flask server:

```bash
gunicorn app:app 
```

4. Access the Web Interface:
   - Open your web browser or a tool like Postman.
   - Go to `http://localhost:8000` to view the API introduction and server information.

5. Check URLs API for Phishing:

   - To check if a specific URL is bad or good, use the `/checkurl` endpoint with the `url` parameter:

   - **Request:**

     ```
     GET http://localhost:8000/checkurl?url=https://example.com
     ```

   - **Response:**

     ```
     {
         "url": "https://example.com",
         "result": "safe" || "harmful"
     }
     ```

   The `type` field can have values "good" or "bad," indicating the classification result.

## ⚡ Key Points

- 🚀 - Exciting features and blazing-fast performance.
- 💡 - Insightful explanations and helpful tips.
- 📝 - Clear and concise code blocks.
- ⚔️ - API plus Website UI
- ✨ - Beautiful Materialize UI for Website
- 📦 - Simple installation and setup instructions.
- 🤖 - Smart Machine Learning model behind the scenes.
- 🔒 - Improved security with URL classification.

# 📃 License

This project is licensed under the 'Unlicense' License - see the [LICENSE](LICENSE) file for details.

---

> **For Fast API Version:- [Click Here](https://github.com/ArnavK-09/phishing-detection/tree/with/fastapi)**