'''
Emotion Detector
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Construct Flask app
app = Flask("Emotion detector")

# Route for emotion detector
@app.route("/emotionDetector")
def sent_detector():
    '''
    Get text to analyze from the request object and send a POST
    request to extract emotion score
    '''
    # Get text to analyze from request object
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to emotion detector to get response
    response = emotion_detector(text_to_analyze)

    # Get scores from response
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Construct output
    if anger is None:
        output = "Invalid text! Please try again!"
    else:
        output = f"For the given statement, the system response is 'anger': {anger}, \
                'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
                The dominant emotion is {dominant_emotion}."

    return output

# Route for index page
@app.route("/")
def render_index_page():
    '''
    Render index page (home page)
    '''
    return render_template("index.html")

# Deploy the app on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
