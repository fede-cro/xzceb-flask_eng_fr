"""
translator module
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Function to translate from english to french
    """
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    """
    Function to translate from french to english
    """
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]

if __name__=='__main__':
    print(english_to_french("Hello"))
    print(english_to_french(" "))
    print(french_to_english("Bonjour"))
