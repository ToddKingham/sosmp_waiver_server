from elastic_enterprise_search import AppSearch
from constants import ELASTIC_ENDPOINT, ELASTIC_PRIVATE_KEY, ELASTIC_ENGINE_NAME


class ElasticCo:
    app_search = None

    def __init__(self):
        self.app_search = AppSearch(
            ELASTIC_ENDPOINT,
            http_auth=ELASTIC_PRIVATE_KEY
        )

    def insert_document(self, data):
        foo = self.app_search.index_documents(
            engine_name=ELASTIC_ENGINE_NAME,
            documents=[data]
        )
