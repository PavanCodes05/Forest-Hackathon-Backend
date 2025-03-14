import os
import firebase_admin
from firebase_admin import credentials, db, messaging

cred = credentials.Certificate("firebase_cred.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": os.getenv("DATABASE_URL")
})

db = db.reference()
messaging = messaging