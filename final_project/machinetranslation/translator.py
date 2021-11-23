from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LangaugeTranslatorV3(
  version = '2018-05-01',
  authenticator = authenticator)

language_translator.set_service_url(url)

def english_to_french(text):
  french_translation = language_translator.translate(
    text = text,
    model_id = 'en_fr')
  .get_result()
  return french_translation.get('translation')[0].get('translation')

def french_to_english(text):
  english_translation = language_translator.translate(
    text = text,
    model_id = 'fr_en')
  .get_result()
  return english_translation.get('translation')[0].get('translation')
    
