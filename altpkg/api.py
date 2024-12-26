import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def perform_get_request(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return ""

def parse_json_structures(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка при разборе JSON-данных: {e}")
        return {}

def find_arch(json_string):
    parsed_json = parse_json_structures(json_string)
    return list(set(package["arch"] for package in parsed_json.get("packages", [])))
