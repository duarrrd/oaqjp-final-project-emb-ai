import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_data = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=input_data, headers=headers)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_predictions['anger']
        disgust_score = emotion_predictions['disgust']
        fear_score = emotion_predictions['fear']
        joy_score = emotion_predictions['joy']
        sadness_score = emotion_predictions['sadness']
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
