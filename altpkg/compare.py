import os
import json
from altpkg.api import perform_get_request, parse_json_structures

def existence_packages(json_sis, json_p10):
    result = []
    for package_sis in json_sis.get("packages", []):
        if not any(package_sis["name"] == package_p10["name"] for package_p10 in json_p10.get("packages", [])):
            result.append(package_sis)
    return result

def single_compare_version(version1, release1, version2, release2):
    full_version1 = version1 + release1
    full_version2 = version2 + release2
    return (full_version1 > full_version2) - (full_version1 < full_version2)

def version_comparison(json_sis, json_p10):
    result = []
    for package_sis in json_sis.get("packages", []):
        if any(
            package_sis["name"] == package_p10["name"] and
            single_compare_version(package_sis["version"], package_sis["release"], package_p10["version"], package_p10["release"]) > 0
            for package_p10 in json_p10.get("packages", [])
        ):
            result.append(package_sis)
    return result

def print_json_structure(result_json, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result_json, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Ошибка: Невозможно открыть файл для записи: {e}")

def compare_json_structures(sisyphus_url, p10_url, arch, result_json, index):
    sisyphus_response = perform_get_request(sisyphus_url)
    p10_response = perform_get_request(p10_url)
    json_sis = parse_json_structures(sisyphus_response)
    json_p10 = parse_json_structures(p10_response)

    print(f"Сравнение по первому критерию: {arch}")
    result_json[index] = existence_packages(json_sis, json_p10)

    print(f"Сравнение по второму критерию: {arch}")
    result_json[index].extend(existence_packages(json_p10, json_sis))

    print(f"Сравнение по третьему критерию: {arch}")
    result_json[index].extend(version_comparison(json_sis, json_p10))

    out_dir = os.path.join("Outputs", arch)
    os.makedirs(out_dir, exist_ok=True)
    print_json_structure(result_json[index], os.path.join(out_dir, f"{arch}.json"))