import sys
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment



class PayPalClient:
    def __init__(self):
        self.client_id = "AfB4xdTAZZsDkgqnZgJtChedUFgpUDVWyDbGaB5WUbJETyfQl7vXvMQNfJLZS2MeThflrUB2ikPSM0kp"
        self.client_secret = "EL2zuBk14ve77U6cRhUnfVqFjBSPkVJSvF5lJ-_DGT2FOgZyG7hUzIjKPa0iDIz-JgTd-DQLgT_u6Aoz"
        self.environment = SandboxEnvironment(client_id = self.client_id, client_secret = self.client_secret)
        self.client = PayPalHttpClient(self.environment)