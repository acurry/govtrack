import requests
import pprint
import json
from datetime import date

BASE_URL = 'https://aacoprod.aacounty.org/AACORest/rest/SubdivisionActivity/apps/'
DATE_FORMAT = '%Y-%m-%d'

ending_date = date.today()
starting_date = date(2018, 10, 1)

data_url = BASE_URL + starting_date.strftime(DATE_FORMAT) + '/' + ending_date.strftime(DATE_FORMAT)

response = requests.get(data_url)
pruned_response_text = response.text[5:-1]
parsed_json = json.loads(pruned_response_text)

clean_data = [{ k: v.strip() if v else '' for (k, v) in item.items()} for item in parsed_json]

sorted_clean_data = sorted(clean_data, key = lambda i: i['submitDate'], reverse=True)

pprint.pprint(sorted_clean_data[:5])

