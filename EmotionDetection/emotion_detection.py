import requests
import json
def emotion_detector(text_to_analyze: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    anger_score = ('anger', formatted_response["emotionPredictions"][0]["emotion"]["anger"])
    disgust_score = ('disgust', formatted_response["emotionPredictions"][0]["emotion"]["disgust"])
    fear_score = ('fear', formatted_response["emotionPredictions"][0]["emotion"]["fear"])
    joy_score = ('joy', formatted_response["emotionPredictions"][0]["emotion"]["joy"])
    sadness_score = ('sadness', formatted_response["emotionPredictions"][0]["emotion"]["sadness"])
    dominant_emotion = sorted([anger_score, disgust_score, fear_score, joy_score, sadness_score], key=lambda x: x[1], reverse=True)[0]
    return {
'anger': anger_score[1],
'disgust': disgust_score[1],
'fear': fear_score[1],
'joy': joy_score[1],
'sadness': sadness_score[1],
'dominant_emotion': dominant_emotion[0]
}