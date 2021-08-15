import os
from threading import Timer
import requests


class ESignGenie:
    access_token = None
    response = None
    expires_in = None

    def __init__(self):
        self.set_access_token()

    def lookup(self, doc_id=0):
        result = {}
        if doc_id:
            endpoint = f"folders/myfolder?folderId={doc_id}"
            data = self.call_endpoint('get', endpoint)
            if data:
                party_details = data['folder']['folderRecipientParties'][0]['partyDetails']
                result['first_name'] = party_details['firstName'].upper()
                result['last_name'] = party_details['lastName'].upper()
                for field in data["allFieldsNameValue"]:
                    if field.get('name', None):
                        key = field['name'].lower().replace(' ', '_')
                        result[key] = field.get('value', "").upper()
        return result

    def set_access_token(self):
        url = f"{os.getenv('E_SIGN_GENIE_BASE_URL')}/oauth2/access_token"
        data = {
            "client_id": os.getenv('E_SIGN_GENIE_CLIENT_ID'),
            "client_secret": os.getenv('E_SIGN_GENIE_CLIENT_SECRET'),
            "grant_type": "client_credentials",
            "scope": "read-write"
        }
        headers = {
            "Content-Type": "application/x-www-form-URLencoded"
        }
        resp = requests.post(url, data=data, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            self.access_token = data["access_token"]
            self.expires_in = data["expires_in"]
            t = Timer(data["expires_in"]/1000, self.set_access_token)
            t.start()

    def call_endpoint(self, verb, endpoint, data=None):
        # set the access token
        if not self.access_token:
            self.set_access_token()

        # define variables
        result = None
        headers = {"Authorization": f"Bearer {self.access_token}"}

        url = f"{os.getenv('E_SIGN_GENIE_BASE_URL')}/{endpoint}"

        # call the server
        api = getattr(requests, verb.lower())
        if data:
            headers["Content-Type"] = "application/json"
            self.response = api(url, json=data, headers=headers)
        else:
            self.response = api(url, headers=headers)

        # validate the server response
        if self.response.status_code == 200:
            result = self.response.json()

            # check for error response
            if result['result'] == 'error':
                raise Exception(result)

        # return the result
        return result
