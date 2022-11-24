#import pyrebase
from pyrebase import pyrebase


class FilestoCloud:

    def __init__(self,predicted_text='None'):
        self.predicted_text = predicted_text
        self.config = {
            "apiKey": "AIzaSyBWueDd28FZa07qMYDj7I3Jo9_soUQ5YTs",
            "authDomain": "airdrawformyself.firebaseapp.com",
            "databaseURL": "",
            "projectId": "airdrawformyself",
            "storageBucket": "airdrawformyself.appspot.com",
            "serviceAccount": "serviceAccountKey.json"
        }

    def upload_file(self):
        firebase_storage = pyrebase.initialize_app(self.config)
        storage = firebase_storage.storage()

        textobject = open("predicted_text.txt","w")
        textobject.writelines(self.predicted_text)
        textobject.close()
        storage.child("predicted_text.txt").put("predicted_text.txt")
        print("File uploaded")