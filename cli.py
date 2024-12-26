import os
import threading
from altpkg.api import perform_get_request, find_arch
from altpkg.compare import compare_json_structures

def main():
    branch1 = input("Введите имя первой ветки: ") or "sisyphus"
    branch2 = input("Введите имя второй ветки: ") or "p10"
    sisyphus_url = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch1}"
    p10_url = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch2}"

    sisyphus_response = perform_get_request(sisyphus_url)
    p10_response = perform_get_request(p10_url)

    arch1 = find_arch(sisyphus_response)
    arch2 = find_arch(p10_response)
    arch_list = list(set(arch1 + arch2))

    os.makedirs("Outputs", exist_ok=True)

    threads = []
    results = [{} for _ in range(len(arch_list))]

    for i, arch in enumerate(arch_list):
        if arch != "null":
            sisyphus_url_arch = f"{sisyphus_url}?arch={arch}"
            p10_url_arch = f"{p10_url}?arch={arch}"
            thread = threading.Thread(
                target=compare_json_structures,
                args=(sisyphus_url_arch, p10_url_arch, arch, results, i)
            )
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print("Все потоки завершены.")

if __name__ == "__main__":
    main()
