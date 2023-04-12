'''
Helper function for translator app
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('api_key')
url = os.getenv('url')
version = os.getenv('version')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    translate english to french
    returns french text
    '''
    if english_text == '':
        return ''
    result = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = result['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    '''
    translates french to english
    returns english text
    '''
    if french_text == '':
        return ''
    result = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = result['translations'][0]['translation']
    return english_text
