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

