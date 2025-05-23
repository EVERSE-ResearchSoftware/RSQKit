#!/usr/bin/env python

import json
import yaml
import os
import base64
import requests

def get_github_repo_contents(repo_owner, repo_name, path=""):
    """
    Fetches the contents of a directory within a GitHub repository.

    Args:
        repo_owner (str): The owner of the GitHub repository.
        repo_name (str): The name of the GitHub repository.
        path (str, optional): The path to the directory within the repository. Defaults to "".

    Returns:
        list: A list of dictionaries, each representing a file or directory in the specified path.
              Returns an empty list if the request fails or the path doesn't exist.
    """
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repository contents from {api_url}: {e}")
        return []


def get_github_file_content(repo_owner, repo_name, file_path):
    """
    Fetches the content of a specific file from a GitHub repository.

    Args:
        repo_owner (str): The owner of the GitHub repository.
        repo_name (str): The name of the GitHub repository.
        file_path (str): The path to the file within the repository.

    Returns:
        str: The decoded content of the file. Returns None if the request fails or the file content cannot be decoded.
    """
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        content_encoded = response.json().get("content")
        if content_encoded:
            content_decoded = base64.b64decode(content_encoded).decode("utf-8")
            return content_decoded
        else:
            print(f"Error: No content found for file {file_path} in {repo_owner}/{repo_name}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file content from {api_url}: {e}")
        return None
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        print(f"Error decoding file content for {file_path}: {e}")
        return None


def generate_rsqkit_data_from_github(repo_owner, repo_name, repo_path, output_file="data.yaml", filter_keys=False):
    contents = get_github_repo_contents(repo_owner, repo_name, repo_path)
    json_files = [item for item in contents if item.get("type") == "file" and item.get("name", "").endswith(".json")]

    if not json_files:
        print(f"No json files found in {repo_owner}/{repo_name}/{repo_path} directory.")
        # Create an empty file if no JSON files are found to avoid errors in downstream processes
        if not os.path.exists(os.path.dirname(output_file)):
             os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as outfile:
            yaml.dump([], outfile)
        print(f"Created empty output file: {output_file}")
        return

    _data = []

    for file_info in json_files:
        file_path = file_info["path"]
        # print(f"Processing {file_path}...")
        try:
            file_content = get_github_file_content(repo_owner, repo_name, file_path)
            if file_content:
                instance = json.loads(file_content)
                if filter_keys:
                    instance = dict(filter(lambda item: "@" not in item[0], instance.items()))
                _data.append(instance)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_path}: {e}")
        except Exception as e:
            error_message = f"{file_path}: Unexpected error - {e}"
            print(f"Error: {error_message}")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)


    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            yaml.dump(
                _data,
                outfile,
                default_flow_style=False,
                allow_unicode=True, # Changed to True to support unicode characters
                indent=4,
            )
        print(f"The data of {len(_data)} files from {repo_owner}/{repo_name}/{repo_path} was saved as {output_file}")
    except IOError as e:
        print(f"Error writing to output file {output_file}: {e}")
    except Exception as e:
        print(f"Unexpected error writing YAML file: {e}")


# Generate data for indicators
generate_rsqkit_data_from_github(
    repo_owner="EVERSE-ResearchSoftware",
    repo_name="indicators",
    repo_path="indicators",
    output_file="_data/quality_indicators.yml",
    filter_keys=True
)

# Generate data for dimensions
generate_rsqkit_data_from_github(
    repo_owner="EVERSE-ResearchSoftware",
    repo_name="indicators",
    repo_path="dimensions",
    output_file="_data/quality_dimensions.yml",
    filter_keys=True
)

# # Generate data for dimensions
# generate_rsqkit_data_from_github(
#     repo_owner="EVERSE-ResearchSoftware",
#     repo_name="TechRadar",
#     repo_path="data/software-tools",
#     output_file="_data/tool_and_resource_list.yml",
#     filter_keys=True
# )
