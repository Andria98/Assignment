import requests
import json
from googletrans import Translator, constants
from pprint import pprint
#this is a test to check if google trans library works
translator = Translator()
adviceList = "Hello world! Example"
translations = translator.translate(adviceList, dest="pl")
print(translations)