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