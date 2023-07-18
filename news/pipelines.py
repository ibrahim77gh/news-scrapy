from firebase_admin import firestore
from .Firebase import Firebase

class Pipeline:
    def __init__(self, collection_name):
        firebase = Firebase()
        firebase.get_app()
        self.db = firestore.client()
        self.collection_name = collection_name  # Name of the collection for politics spider data
        
        # Clear the collection before adding new documents
        self.clear_collection()

    def clear_collection(self):
        docs = self.db.collection(self.collection_name).stream()
        for doc in docs:
            doc.reference.delete()

class PoliticsPipeline(Pipeline):
    def __init__(self):
        super().__init__(collection_name="politics_collection")

    def process_item(self, item, spider):
        # Convert the item to a dictionary
        item_dict = dict(item)

        # Save the item as a new document in the collection
        self.db.collection(self.collection_name).add(item_dict)

        return item


class SportsPipeline(Pipeline):
    def __init__(self):
        super().__init__(collection_name="sports_collection")

    def process_item(self, item, spider):
        # Convert the item to a dictionary
        item_dict = dict(item)

        # Save the item as a new document in the collection
        self.db.collection(self.collection_name).add(item_dict)

        return item


class BusinessPipeline(Pipeline):
    def __init__(self):
        super().__init__(collection_name="business_collection")

    def process_item(self, item, spider):
        # Convert the item to a dictionary
        item_dict = dict(item)

        # Save the item as a new document in the collection
        self.db.collection(self.collection_name).add(item_dict)

        return item

class LocalnewsPipeline(Pipeline):
    def __init__(self):
        super().__init__(collection_name="localnews_collection")

    def process_item(self, item, spider):
        # Convert the item to a dictionary
        item_dict = dict(item)

        # Save the item as a new document in the collection
        self.db.collection(self.collection_name).add(item_dict)

        return item

    
class HedgePipeline(Pipeline):
    def __init__(self):
        super().__init__(collection_name="hedge_collection")

    def process_item(self, item, spider):
        # Convert the item to a dictionary
        item_dict = dict(item)

        # Save the item as a new document in the collection
        self.db.collection(self.collection_name).add(item_dict)

        return item
    
class RockwellPipeline(Pipeline):
    def __init__(self):
        super().__init__(collection_name="rockwell_collection")

    def process_item(self, item, spider):
        # Convert the item to a dictionary
        item_dict = dict(item)

        # Save the item as a new document in the collection
        self.db.collection(self.collection_name).add(item_dict)

        return item
