""" Update devcontainer.json with latest versions of extensions """
import json
import requests

def get_latest_version(extension_id):
    """ Get latest version of extension from Visual Studio Marketplace """
    url = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery"
    payload = {
        "filters": [{
            "criteria": [{"filterType": 7, "value": extension_id}]
        }],
        "flags": 8704
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json;api-version=6.1-preview.1"
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"][0]["extensions"][0]["versions"][0]["version"]
    return None

def main():
    """ Main function """
    # Load devcontainer.json
    with open(".devcontainer/devcontainer.json", "r") as f:
        devcontainer = json.load(f)

    # Update extensions
    if "extensions" in devcontainer:
        for index, extension in enumerate(devcontainer["extensions"]):
            extension_id = extension.split("@")[0]
            if latest_version := get_latest_version(extension_id):
                devcontainer["extensions"][index] = f"{extension_id}@{latest_version}"
                print(f"Updated {extension_id} to version {latest_version}")

    # Save updated devcontainer.json
    with open(".devcontainer/devcontainer.json", "w") as f:
        json.dump(devcontainer, f, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()
