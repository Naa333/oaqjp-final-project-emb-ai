import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    #initialize the dominant emotion
    dominant_emotion = None

    if response.status_code == 200:
        #retrieve the dictionary of interest
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

        #store the scores
        anger_score = emotion_dict['anger']
        disgust_score = emotion_dict['disgust']
        fear_score = emotion_dict['fear']
        joy_score = emotion_dict['joy']
        sadness_score = emotion_dict['sadness']

        #find the max score
        max_score = max(anger_score, disgust_score,fear_score, joy_score, sadness_score)

        #find the dominant emotion from the associated max score
        for emotion, score in emotion_dict.items():
            if score == max_score:
                dominant_emotion = emotion
        
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    # Return a dictionary containing emotion detecting results
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )