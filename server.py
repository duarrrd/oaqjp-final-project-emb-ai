"""
Emotion Detection Web Application

This script defines a Flask web application for performing emotion detection on user-provided text.

"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    """
    Emotion Detector API Endpoint

    Retrieves emotion scores and dominant emotion for the given text.

    Returns:
        JSON response with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        response_message = "Invalid text! Please try again!"
    else:
        response_message = (
            f"For the given statement, the system response is 'anger': {anger_score}, "
            f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
            f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
        )

    return jsonify(response_message)

@app.route("/")
def render_index_page():
    """
    Render Index Page

    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
