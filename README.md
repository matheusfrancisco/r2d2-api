# R2D2 Recommendation Api Engine

## Description

R2-D2 is the resourceful recommendation robot designed to suggest the best rolês in Brazil.


The R2-D2 recommendation system is based on Content-based Recommendation Systems.

# How to use API:

pipenv run python main.py 
```
Call route [route]/recommendations with POST method, containing:
user_id (float): ID of user which is using the app,
answers (dictionary with format {
    how_much: int,
    like: int,
    number_of_ppl: int
}): Answers this user provided when starting the app.
```

For more information on how it works, check these sources:
https://youtu.be/2uxXPzm-7FY
https://link.springer.com/chapter/10.1007/978-0-387-85820-3_3


## Dependencies

### Install
* python 3.8
* FastApi
* Python packages installed via `pipenv install`

## How deploy api
`npm install`

before running this command our aws should be configured
```
cat ~/.aws/credentials
region = us-east-1
aws_access_key_id=ACCESS_KEY
aws_secret_access_key=SECRETE_ACCESS_KEY
```

* serverless command line`serverless deploy`
* serverless plugin from package.json

## Development Dependencias

* Python packages `pipenv install --dev`

## Folder Structure



/app
 - api.py
 - asg.py
 - config.py
 - models.py

/tests
 - test_api.py
 - test_asgi.py
 - test_models.py

main.py


* models.py: At this file contains our pydantic models
* asg.py: ASGI wrapper for AWS API Gateway integration,
* config.py: Env config
* api.py: Http entrypoint

* tests/test_api.py: How test http calls
* tests/asgi.py: How tests our asgi
* tests/models.py How test pure models or logic

