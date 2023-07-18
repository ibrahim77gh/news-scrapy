import firebase_admin
from firebase_admin import credentials
import os

serviceAccountKey = {
  
}


class Firebase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # Call the __new__ method of the Object Class i.e. create a new instance
            cls._instance._initialize_firebase()
        return cls._instance

    def _initialize_firebase(self):
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # key_file = os.path.join(current_dir, 'serviceAccountKey.json')
        self.cred = credentials.Certificate(serviceAccountKey)
        self.firebase_app = firebase_admin.initialize_app(self.cred)

    def get_app(self):
        return self.firebase_app