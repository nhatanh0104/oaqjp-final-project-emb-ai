import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    # Construct input json
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request and get response, then format it
    response = requests.post(URL, json=input_json, headers=HEADERS)
    formatted_response = json.loads(response.text)

    # if status is 200, then find dominant emotion
    if response.status_code == '200':
        # Get emotion scores
        emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]

        # Initialize dominate emotion and score
        dominant_emotion = None
        dominant_score = 0

        # Find dominant emotion
        for emotion, score in emotion_scores.items():
            if score > dominant_score:
                dominant_emotion = emotion
                dominant_score = score

        # Add dominant emtion to the score dict and return
        emotion_scores["dominant_emotion"] = dominant_emotion
    # Else if status code is 500, return None
    elif response.status_code == 400:
        emotion_scores = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    return emotion_scores

# if __name__ == "__main__":
#     response = emotion_detector("I love this new technology. But I hate its price")
#     print(json.dumps(response, indent=2))
    