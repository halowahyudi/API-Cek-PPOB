import json
import requests
from src.ScraperAPI import ScraperAPI


class telkomIndihome(ScraperAPI):

    def __init__(self, customer_number):
        super().__init__()
        self.customer_number = customer_number
        if len(self.customer_number) < 12 or len(self.customer_number) > 12:
            raise Exception("Customer number must be 12 digits")
        elif self.customer_number is None:
            raise Exception("Customer number cannot be empty")

        self.access_token = ScraperAPI()._get_access_token("telkom-indihome")
        if self.access_token is None:
            raise Exception("Failed to get access token")

    def _get_data(self):
        try:
            response = None
            response = requests.post(
                url=ScraperAPI.API_URL + "telkom-postpaids/inquiries",
                params={
                    "access_token": self.access_token,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={
                    "customer_number": self.customer_number,
                }
            )

            return {
                "status": True,
                "customer_number": self.customer_number,
                "customer_name": response.json()['data']['customer_name'],
                "periods": response.json()['data']['periods'],
                "amount": response.json()['data']['base_amount'],
            }


        except KeyError:
            return {
                "status": False,
                "customer_number": self.customer_number,
                "message": response.json()['errors'][0]['message'],
            }

        except json.decoder.JSONDecodeError:
            return None

        except requests.exceptions.ConnectionError:
            return None

        except requests.exceptions.ReadTimeout:
            return None
