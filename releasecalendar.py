import json
import requests


class ReleaseCalendar:
    def __init__(self, proxy):
        self.proxy = proxy

        self.products = []

    def fetch_finishline_drops(self):
        endpoint = "https://prodmobloy2.finishline.com/api/shop/drops"
        headers = {"Host": "prodmobloy2.finishline.com", "Accept": "*/*", "Accept-Encoding": "gzip, deflate",
                   "Connection": "keep-alive",
                   "Riskified-User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955F Build/NRD90M)",
                   "User-Agent": "Finish Line/2.7.6 (Android 7.1.2; Build/NRD90M)", "welove": "maltliquor",
                   "X-Api-Version": "3.0"}
        try:
            response = requests.get(endpoint, headers=headers, proxies=self.proxy, timeout=60)
            if response.status_code == 200:
                json_response = json.loads(response.text)
                self.products = json_response["dropProducts"]
                return True, None

            elif response.status_code == 403:
                return False, "Unexpected Request"

            elif response.status_code > 499:
                return False, "Internal Server Error"

            else:
                return False, "Bad Status Code: " + str(response.status_code)

        except Exception as error:
            return False, str(error)
