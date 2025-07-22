"""
Import the necessary dependencies
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def analyze_emotion():
    """
    Pass a text into the detector function.
    Store the response
    Peform error handling if text was blank
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if "The dominant emotion is None" in response:
        return "Invalid text! Please try again!"
    return response

@app.route("/")
def render_index_page():
    """
    Display the html page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
