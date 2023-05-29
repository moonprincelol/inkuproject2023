import firebase_admin





def open_database():

    credentials_object = firebase_admin.credentials.Certificate('databasekeys.json')
    default_app = firebase_admin.initialize_app(credentials_object, {
        'databaseURL': "https://studyvault-4cd10-default-rtdb.europe-west1.firebasedatabase.app/"
        })