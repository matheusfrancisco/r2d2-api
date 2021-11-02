# R2D2 Recommendation Api Engine V0.1

## Description
R2-D2 is the resourceful recommendation robot designed to suggest the best rolês in Brazil.
The R2-D2 recommendation system is based on Content-based Recommendation Systems.

# How to use API:
TODO needs to write

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

##  Run locally

* Active you virtualenv or not..
* Install the dependencies
* Python packages `pip install -r requirements.txt`


Run locally as fastapi server

```bash
pip install -r requirements.txt
export ENVFILE=.env && python main.py
```

Run locally as serverless-offline
