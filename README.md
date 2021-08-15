# sosmp_waiver_server
AWS middleware for SOSMP Waiver Module



* Create the following two files and place them in your project root if you would like to test locally.
* Swap out placeholder values with real values
* Create a virtual environment and run the following line from inside the project root:
  - `pip install -r requirements.txt`

# .env
```
# ELASTIC.CO
ELASTIC_ENDPOINT=[YOUR_VALUE_HERE]
ELASTIC_ENGINE_NAME=[YOUR_VALUE_HERE]
ELASTIC_PRIVATE_KEY=[YOUR_VALUE_HERE]

# ESIGN GENIE
E_SIGN_GENIE_BASE_URL=[YOUR_VALUE_HERE]
E_SIGN_GENIE_CLIENT_ID=[YOUR_VALUE_HERE]
E_SIGN_GENIE_CLIENT_SECRET=[YOUR_VALUE_HERE]
```



# test.json
```
{
    "body": "{\"event_name\": \"folder_completed\", \"event_date\": 1628876175523, \"data\": {\"folder\": {\"folderId\": [YOU_VALUE_HERE]}}}"
}
```
