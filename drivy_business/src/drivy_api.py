from typing import Any

from pydantic import BaseModel


class DrivyAPI(BaseModel):
    client: Any

    header = {
        'author ity': 'be.getaround.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="92", "Opera";v="78"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-csrf-token': 'qCsmTOmwAZtBbOO1vvxpQgam7SvnAXJtz37V7cvtVZiE0HCLr9wwCI91tT45MKVc3K4RuJbY95PhQgMblNHoNQ==',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 OPR/78.0.4093.184',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://be.getaround.com/je-auto-verhuren',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_gcl_au=1.1.1503342619.1632294263; _tracked-properties={%221.0%22:{%22landing-url%22:%22https://www.getaround.com/guarantee%22%2C%22http-referer%22:%22https://www.google.com/%22}%2C%22latestVersion%22:%221.0%22}; _ga=GA1.2.1389757912.1632294263; ajs_anonymous_id=%22b5b64548-e92c-4ddc-83e7-7781c7cb6e9c%22; amplitude_idundefinedgetaround.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; ajs_user_id=%22b5b64548-e92c-4ddc-83e7-7781c7cb6e9c%22; user_reference=9561bad050221b2a46a90ae6d420bd64; _session_id=97e9920e5e531d2844ff6f4beae0da08; dt_anonymous_id=00d7c6cd-44dd-46bf-83d8-e2028c52925e; cookie_consent=%7B%22categories%22%3A%7B%22audience%22%3Afalse%2C%22performance%22%3Afalse%2C%22targeting%22%3Afalse%7D%2C%22updated_at%22%3A%222021-09-22T07%3A19%3A11.644Z%22%7D; ab_cookie=7a0287072333847cf62551e112b8f29e; v2.getaround.session=eef7bfada6a8de18c5eb03136e4f1e6b53fcf940OGJrjJmhh8pgaGmrWiyoCm+FxbCcHSmuWlddAidPMDVXjti0v9odKyXpZrvmmxUsVRdy3cZvuRxpuSqhv/BeXgoOVbd1QZKnZvgeMK1wvRaYtODidUtSOKJD8YF4iY5HRogbN2w/zFZVnXfDBg6ohebUAe7unbSBmXxsIUPwzbwkWiydKgk/lFRFQXf7YcscV9ZE+0efL5Ywof7Iw8mKR8I11tjfhht51RDptJZWpdcM8LGEZBuDLwoceApQClWsrMOSuzFxzIt/nhvNSy+K1agurhqLlPHgk2993G8IKaykKvESkW32q/BULWImg4nSBhC2+Rp5eMNPfMKKPAnKj66Z; amplitude_id_59ead78e9d5d4b881e2f891647bc829egetaround.com=eyJkZXZpY2VJZCI6IjhmZjI1NThmLTIxOTEtNDFjYS05N2NhLTY2YjIxNzc0YTA5ZVIiLCJ1c2VySWQiOiJiNWI2NDU0OC1lOTJjLTRkZGMtODNlNy03NzgxYzdjYjZlOWMiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MzIyOTQyNjMyMTAsImxhc3RFdmVudFRpbWUiOjE2MzIyOTU5NDUwODQsImV2ZW50SWQiOjgsImlkZW50aWZ5SWQiOjksInNlcXVlbmNlTnVtYmVyIjoxN30=; owner_estimation_model_id=619; owner_estimation_release_year=2018; owner_estimation_mileage_key=5',
    }

    def get_estimated_earning(self, brand, model, year, km):
        pass

    async def get_models(self, brand_id):
        with
        pass
