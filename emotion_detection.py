import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    # Construct input json and fetch response
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=input_json, headers=HEADERS)
    formatted_response = json.loads(response.text)

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

    return emotion_scores

# if __name__ == "__main__":
#     response = emotion_detector("I love this new technology. But I hate its price")
#     print(json.dumps(response, indent=2))
    