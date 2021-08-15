import json
from callback_listeners import folder_completed


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


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    with open('test.json', "r") as outfile:
        lambda_handler(json.load(outfile), {})
