# Data Generation Script (`generate_data.py`)

This script fetches quality indicator and dimension data from the `EVERSE-ResearchSoftware/indicators` GitHub repository, processes it, and saves the results as YAML files in the `_data/` directory of this repository.

## How it works

1.  **Fetches Repository Contents**: It uses the GitHub API to list the files within specified directories (`indicators` and `dimensions`) in the `EVERSE-ResearchSoftware/indicators` repository.
1.  **Reads JSON Files**: For each JSON file found in the specified directories, it fetches the file content using the GitHub API.
1.  **Decodes and Parses**: The base64 encoded content received from the API is decoded, and the JSON data is parsed.
1.  **Filters Data (Optional)**: If the `filter_keys` argument is set to `True`, it removes any key-value pairs from the JSON objects where the key contains an "@" symbol. This is used to exclude schema-related keys.
1.  **Aggregates Data**: The processed data from all JSON files in a directory is collected into a list.
1.  **Writes YAML Output**: The aggregated list of data is written to a specified YAML output file (`_data/filtered_quality_indicators.yml` and `_data/filtered_quality_dimensions.yml`). The script ensures the `_data` directory exists before writing.
1.  **Handles Errors**: Includes error handling for network issues, file decoding errors, JSON parsing errors, and file writing errors. If no JSON files are found in a remote directory, it creates an empty YAML file to prevent downstream errors.

## How to Use

The script is designed to be run directly from the command line within the root directory of the `RSQKit` repository.

```bash
python -m pip install requests pyyaml
python scripts/generate_data.py
```

This command will:
- Fetch indicator data from `https://github.com/EVERSE-ResearchSoftware/indicators/tree/main/indicators`, filter it, and save it to `_data/filtered_quality_indicators.yml`.
- Fetch dimension data from `https://github.com/EVERSE-ResearchSoftware/indicators/tree/main/dimensions`, filter it, and save it to `_data/filtered_quality_dimensions.yml`.
