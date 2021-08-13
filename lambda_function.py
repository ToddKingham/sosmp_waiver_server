import json

from constants import E_SIGN_GENIE_BASE_URL
from e_sign_genie import ESignGenie
from elastic_co import ElasticCo


# ENTRY POINT
def lambda_handler(event, context):
    data = json.loads(event.get("body", "{}"))

    # register event listeners
    folder_completed(**data)

    # send a response
    return {
        'statusCode': 200,
        'body': "success"
    }


# EVENT LISTENERS (currently only listening for the "folder_completed" event)
def folder_completed(event_name="", event_date=None, data=None, **kwargs):
    if event_name == "folder_completed":
        # 1: parse event to get the folder_id
        doc_id = data.get("folder", {}).get('folderId', 0)

        # 2: send the folder_id to e_sign_genie to get the details
        doc_provider = ESignGenie()
        doc_details = doc_provider.lookup(doc_id)

        # 3: send the details to elastic.co
        if doc_details:
            elastic_provider = ElasticCo()
            elastic_provider.insert_document(doc_details)
