import json
import sys
from typing import Optional

import requests


def get_latest_version(extension_id: str) -> Optional[str]:
    """ Get the latest version of a Visual Studio Code extension """
    try:
        url = f"https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery"
        headers = {"Content-Type": "application/json", "Accept": "application/json;api-version=3.0-preview.1"}
        payload = {
            "filters": [{"criteria": [{"filterType": 7, "value": extension_id}]}],
            "assetTypes": [],
            "flags": 870,
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        if data["results"]:
            return data["results"][0]["extensions"][0]["versions"][0]["version"]

    except Exception as e:
        print(f"Error fetching latest version for {extension_id}: {e}")

    return None


def main():
    """ Main function """
    # Load devcontainer.json
    file_path = ".devcontainer/devcontainer.json"

    try:
        print(f"Reading file: {file_path}")  # Add this line
        with open(file_path, "r") as f:
            content = f.read()
            print(f"File content: {content}")  # Add this line
            devcontainer = json.loads(content)
    except Exception as e:
        print(f"Error loading JSON file '{file_path}': {e}")
        return

    # Update extensions
    customizations = devcontainer.get("customizations", {})
    vscode = customizations.get("vscode", {})
    extensions = vscode.get("extensions", [])

    if extensions:
        for index, extension in enumerate(extensions):
            extension_id = extension.split("@")[0]
            if latest_version := get_latest_version(extension_id):
                extensions[index] = f"{extension_id}@{latest_version}"
                print(f"Updated {extension_id} to version {latest_version}")

    # Save updated devcontainer.json
    with open(file_path, "w") as f:
        json.dump(devcontainer, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
