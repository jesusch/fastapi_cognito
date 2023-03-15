from pydantic import BaseSettings, BaseModel
from fastapi.security import OpenIdConnect

class CognitoUserpoolSettings(BaseSettings):
    aws_region: str = ''
    aws_cognito_userPoolId: str

    @property
    def userpool_base_url(self):
        return f'https://cognito-idp.{self.aws_region}.amazonaws.com/{self.aws_cognito_userPoolId}'

    @property
    def openid_configuration(self):
        """A directory of the OIDC architecture of your user pool."""
        return f'{self.userpool_base_url}/.well-known/openid-configuration'

    @property
    def jwks(self):
        """Public keys that you can use to validate Amazon Cognito tokens."""
        return f'{self.userpool_base_url}/.well-known/jwks.json'

    class Config:
        env_file = '.env'


class AccessUser(BaseModel):
    sub: str


cognito_settings = CognitoUserpoolSettings()
oauth2_scheme = OpenIdConnect(openIdConnectUrl=cognito_settings.openid_configuration)