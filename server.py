"""
server.py
This module handles server operations for the emotion detector application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the welcome page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion_detecotor():
    """
    Sends the text for emodtion detection
    """
    # Retrieve the text to detect from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    emotions = emotion_detector(text_to_analyze)
    response = None
    if emotions['dominant_emotion'] is None :
        response ="Invalid text! Please try again!"
    else:
        response = (
    f"For the given statement, the system response is 'anger': {emotions['anger']},"
    f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
    f"and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}"
)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
