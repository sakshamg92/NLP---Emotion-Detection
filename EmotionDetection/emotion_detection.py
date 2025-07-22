import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {
        "Content-Type" : "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload =  { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers= headers, json = payload)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = json.loads(response.text)
    emotion_scores = response_dict['emotionPredictions'][0]['emotion']

    formatted_result = {
        'anger' : emotion_scores['anger'],
        'disgust' : emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy' : emotion_scores['joy'],
        'sadness' : emotion_scores['sadness'],
        'dominant_emotion': max(emotion_scores, key=emotion_scores.get)
    }
    return formatted_result