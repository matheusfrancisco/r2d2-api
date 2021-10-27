# R2D2 Recommendation Api Engine

## Description

R2-D2 is the resourceful recommendation robot designed to suggest the best rolês in Brazil.


The R2-D2 recommendation system is based on Content-based Recommendation Systems.

# How to use API:

pipenv run python main.py 
```
Call api by using [route]/recommendations/user_id  with POST method, containing:
user_id (float): ID of user which is using the app,
answers (dict): Answers this user provided when starting the app. Format:
{
    how_much: int,
    like: int,
    number_of_ppl: int
}

The API will return a dictionary containing a list of strings, that represent the
ID's of the top 10 establishment recommendations for the user.
 
```

For more information on how it works, check these sources:
https://youtu.be/2uxXPzm-7FY
https://link.springer.com/chapter/10.1007/978-0-387-85820-3_3


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

* Python packages `pip install -r requirements.txt`

