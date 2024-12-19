import requests

BASE_URL = "https://rdb.altlinux.org/api/export/branch_binary_packages"

def fetch_packages(branch: str, arch: str = None):
    
    params = {"arch": arch} if arch else {}
    url = f"{BASE_URL}/{branch}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, dict) and "packages" in data:
            return data["packages"]
        else:
            raise ValueError(f"Unexpected data format: {data}")
    else:
        raise ValueError(f"Error fetching packages for branch '{branch}': {response.status_code}")
