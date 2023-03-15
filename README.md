# FastAPI Cognito

## Usage
### Mandatory Environment variables
Either as exported ENV vars or in `./.env`

```
region=sa-east-1
aws_cognito_userPoolId=	sa-east-1_abc
```

```
from fastapi import FastAPI, Depends
from fastapi_cognito import oauth2_scheme

app = FastAPI()


@app.get("/secured/")
def secure_user(dependencies=Depends(oauth2_scheme)):
    # ID token is valid and getting user info from ID token
    return "Hello"

```