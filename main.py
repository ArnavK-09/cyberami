# imports
import time
from datetime import timedelta
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from flask import Flask, request, jsonify

# Step 0: Setup Helper functions
def get_system_uptime():
    """
        Function to get uptime
    """
    with open('/proc/uptime', 'r', encoding='utf-8') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds=uptime_seconds))
    return uptime_string


# Step 1: Data Preprocessing
print("[Model] Started Processing Data...")
data = pd.read_csv("data/main.csv")
data["Label"] = data["Label"].map({"bad": 0, "good": 1})
X = data["URL"]
Y = data["Label"]

# Step 2: Model Training
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', LogisticRegression(solver='lbfgs', max_iter=500000))
])
model.fit(X, Y)
print("[Model] Processing Done...")

# Step 3: Create an API using Flask
app = Flask(__name__)

# Step 4: Configure routes
@app.route('/')
def index():
    """
        GET /
        { introduction, usage_time, uptime }
    """
    introduction = "Welcome to the System Usage API! This API provides information about system usage time and uptime."
    usage_time = time.strftime("%Y-%m-%d %H:%M:%S")
    uptime = get_system_uptime()
    return jsonify({
        "introduction": introduction,
        "usage_time": usage_time,
        "uptime": uptime
    })

@app.route('/checkurl', methods=['GET'])
def check_url():
    """
        GET /checkurl?url=...
        { url, type }
    """
    url = request.args.get('url', '')
    prediction = model.predict([url])[0]
    # return
    return jsonify({"url": url, "type": "good" if prediction == 1 else "bad"})

# Step 5: Startup API Server
if __name__ == '__main__':
    app.run(debug=True)
