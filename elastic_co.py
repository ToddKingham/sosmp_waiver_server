import os
from elastic_enterprise_search import AppSearch


class ElasticCo:
    app_search = None

    def __init__(self):
        self.app_search = AppSearch(
            os.getenv('ELASTIC_ENDPOINT'),
            http_auth=os.getenv('ELASTIC_PRIVATE_KEY')
        )

    def insert_document(self, data):
        foo = self.app_search.index_documents(
            engine_name=os.getenv('ELASTIC_ENGINE_NAME'),
            documents=[data]
        )
