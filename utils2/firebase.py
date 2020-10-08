import pyrebase

import os

config = {
    "apiKey": str(os.getenv('FIRE_API_KEY')),
    "authDomain":str(os.getenv('FIRE_AUTH_DOMAIN') ),
    "databaseURL":str(os.getenv('FIRE_DB_URL') ),
    "storageBucket": str(os.getenv('FIRE_STORAGE_BUCKET')),
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
