import requests
import json

def emotion_detector(text_to_analyse):
    """
    Emotion detection function.
    """
    # URL of the Emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    result = {}
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
       # Extract emotions
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        # Prepare the output in the desired format
        result = {
            'anger': emotions['anger'],'disgust': emotions['disgust'],'fear': emotions['fear'],
            'joy': emotions['joy'],'sadness': emotions['sadness'],'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
            result = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None,  'sadness': None,
                'dominant_emotion': None
            }
    return result