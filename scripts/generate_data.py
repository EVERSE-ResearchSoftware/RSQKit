#!/usr/bin/env python

import yaml
import os
import requests
import csv
import io
import sys

def fetch_json_from_api(url):
    """
    Standard HTTP GET request to fetch JSON data from a public endpoint.
    Crashes safely if the server is down or returns an error status code.
    
    Args:
        url (str): The target API endpoint URL.
        
    Returns:
        dict: The parsed JSON payload from the API response.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"CRITICAL ERROR fetching API data from {url}: {e}")
        sys.exit(1)


def get_consensus_summary_from_github():
    """
    Downloads and parses the consensus summary CSV file from GitHub.
    
    Returns:
        dict: A dictionary indexed by indicator URI containing tier relevance metadata.
    """
    url = "https://api.github.com/repos/EVERSE-ResearchSoftware/indicators/contents/docs/consensus_summary.csv"
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_encoded = response.json().get("content")
        if not content_encoded:
            print("CRITICAL ERROR: No content found for consensus_summary.csv")
            sys.exit(1)
            
        import base64
        content = base64.b64decode(content_encoded).decode("utf-8")
    except Exception as e:
        print(f"CRITICAL ERROR fetching consensus CSV: {e}")
        sys.exit(1)

    consensus = {}
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        indicator_uri = row.get("Indicator (to get more info)", "").strip()
        if not indicator_uri:
            continue

        consensus[indicator_uri] = {
            "Relevant for Analysis Code": row.get("Relevant for Analysis Code"),
            "Relevant for Prototype tool": row.get("Relevant for Prototype tool"),
            "Relevant for RS infrastructure": row.get("Relevant for RS infrastructure"),
        }
    return consensus


def generate_rsqkit_data_from_api(api_url, data_type, output_file, clean_internal_keys=True):
    """
    Retrieves data from the public API wrapper, extracts the targeted array,
    injects GitHub consensus information, and writes the structured result into a YAML file.
    
    Args:
        api_url (str): The public wrapper URL containing the graph database collection.
        data_type (str): The node collection key to extract (either 'indicators' or 'dimensions').
        output_file (str): Target path for the output YAML file.
        clean_internal_keys (bool): If True, filters out backend metadata properties like '_filename'.
    """
    raw_payload = fetch_json_from_api(api_url)
    
    if isinstance(raw_payload, dict) and data_type in raw_payload:
        data_list = raw_payload[data_type]
    else:
        print(f"CRITICAL ERROR: Expected a dictionary containing the key '{data_type}' from {api_url}")
        sys.exit(1)
        
    if not isinstance(data_list, list):
        print(f"CRITICAL ERROR: The key property '{data_type}' is not a list. Got: {type(data_list)}")
        sys.exit(1)
        
    consensus_data = get_consensus_summary_from_github() if data_type == "indicators" else {}
    processed_data = []

    for instance in data_list:
        try:
            if clean_internal_keys:
                instance = dict(filter(lambda item: not item[0].startswith('_'), instance.items()))
                
            indicator_uri = None

            if data_type == "indicators":
                identifier = instance.get("identifier")
                if isinstance(identifier, dict):
                    indicator_uri = identifier.get("@id")
                    
                if indicator_uri and indicator_uri in consensus_data:
                    instance["relevant in tiers"] = consensus_data[indicator_uri]

            elif data_type == "dimensions":
                identifier = instance.get("identifier")
                if isinstance(identifier, str):
                    indicator_uri = identifier
                    
            processed_data.append(instance)
            
        except Exception as e:
            print(f"CRITICAL ERROR processing an item from {data_type}: {e}")
            sys.exit(1)

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            yaml.dump(
                processed_data,
                outfile,
                default_flow_style=False,
                allow_unicode=True,
                indent=4,
            )
        print(f"Successfully processed {len(processed_data)} {data_type} into {output_file}")
    except Exception as e:
        print(f"CRITICAL ERROR writing YAML file {output_file}: {e}")
        sys.exit(1)


if __name__ == "__main__":

    generate_rsqkit_data_from_api(
        api_url="https://everse.software/indicators/api/indicators.json",
        data_type="indicators",
        output_file="_data/quality_indicators.yml",
        clean_internal_keys=True
    )

    generate_rsqkit_data_from_api(
        api_url="https://everse.software/indicators/api/dimensions.json",
        data_type="dimensions",
        output_file="_data/quality_dimensions.yml",
        clean_internal_keys=True
    )