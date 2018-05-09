import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            return ''


