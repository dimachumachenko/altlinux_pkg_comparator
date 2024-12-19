import requests

BASE_URL = "https://rdb.altlinux.org/api/export/branch_binary_packages"

def fetch_packages(branch: str):

	url = f"{BASE_URL}/{branch}"
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		raise ValueError(f"Error fetching packages for branch '{branch}': {response.status_code}")
