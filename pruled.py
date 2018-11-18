import firebase_admin

from firebase_admin import credentials

from firebase_admin import db


cred = credentials.Certificate('/home/pi/iot/cred.json')


# Initialize the app with a service account, granting admin privileges

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://controlcasa-9eaaf.firebaseio.com/'

})


ref = db.reference('home')

print(ref.get())

print ('Ok !')