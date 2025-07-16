"""Script to check discrepancies within tool descriptions comparing RSQkit and TechRadar tools"""
import os
import json
import yaml
import requests
import json
import pprint
from glob import glob
from deepdiff import DeepDiff
from rich.table import Table
from rich.console import Console

TECHRADAR_GITHUB_API_URL = "https://api.github.com/repos/EVERSE-ResearchSoftware/TechRadar/contents/data/software-tools"

def load_yaml_tools_from_rsqkit():
    YAML_MATCH_FIELD = "description"
    tools = {}
    path = os.path.join("_data", "tool_and_resource_list.yml")
    matched_files = glob(path)
    with open(matched_files[0], "r") as f:
        data = yaml.safe_load(f)
        if isinstance(data, list):
            for item in data:
                if YAML_MATCH_FIELD in item:
                    tools[item["name"]]= item
        else:
            print("YAML content is not a list")
    return tools

def load_jsonld_tools_from_techradar():
    tools = {}
    JSON_MATCH_FIELD = "schema:description" 
    response = requests.get(TECHRADAR_GITHUB_API_URL)
    response.raise_for_status()
    files = response.json()

    for file in files:
        if file["name"].endswith(".json"):
            raw_url = file["download_url"]
            file_response = requests.get(raw_url)
            file_response.raise_for_status()
            data = json.loads(file_response.text)
            if JSON_MATCH_FIELD in data:
                tools[data["schema:name"]] = data
            else:
                print(f"'{JSON_MATCH_FIELD}' not found in {file['name']}")
    return tools

def compare_tool_definitions(yaml_tool, jsonld_tool, fields_to_compare, field_mapping):
    discrepancies = {}
    tool_name = yaml_tool.get("name")

    for yaml_field in fields_to_compare:
        jsonld_field = field_mapping.get(yaml_field, yaml_field)
        yaml_val = yaml_tool.get(yaml_field)
        json_val = jsonld_tool.get(jsonld_field)
        print(f"Comparing '{yaml_field}' → '{jsonld_field}' for tool: {tool_name}")

        if yaml_val is None or json_val is None:
            print("One of the values is None — check your keys and mappings")
            continue

        diff = DeepDiff(yaml_val, json_val, ignore_order=True)
        if diff:
            discrepancies[yaml_field] = diff
            print(f" Description in RSQkit for tool {tool_name} :: {yaml_val}")
            print(f" Description in TechRadar for tool {tool_name} :: {json_val}")
        else:
            print(f"No difference found for '{yaml_field}' in tool: {tool_name}")
    return discrepancies


def summarize_discrepancies(discrepancy_dict):
    console = Console()

    if not discrepancy_dict:
        console.print("[bold green]No discrepancies found across tools.[/bold green]")
        return

    table = Table(title="Summary of Tools with Discrepancies")

    table.add_column("Tool", style="cyan", no_wrap=True)
    table.add_column("Field", style="magenta")
    table.add_column("RSQkit Description", style="yellow")
    table.add_column("TechRadar Description", style="green")

    for tool, diffs in discrepancy_dict.items():
        for field, diff in diffs.items():
            values_changed = diff.get('values_changed', {})
            for path, changes in values_changed.items():
                rsqkit_description = str(changes.get('old_value', 'N/A'))
                techradar_description = str(changes.get('new_value', 'N/A'))
                table.add_row(tool, field, rsqkit_description, techradar_description)

    console.print(table)

def main():
    rsqkit_tools = load_yaml_tools_from_rsqkit()
    techradar_tools = load_jsonld_tools_from_techradar()

    FIELDS_TO_COMPARE = ["description"]
    FIELD_MAPPING = {
        "description": "schema:description"  # multiple fields to compare can be added
    }

    all_discrepancies = {}

    for tool_name in rsqkit_tools:
        if tool_name in techradar_tools:
            rsqkit_tool = rsqkit_tools[tool_name]
            techradar_tool = techradar_tools[tool_name]

            discrepancies = compare_tool_definitions(
                rsqkit_tool, techradar_tool,
                FIELDS_TO_COMPARE, FIELD_MAPPING 
            )

            if discrepancies:
                all_discrepancies[tool_name] = discrepancies
                print(f"Discrepancies found for tool '{tool_name}':")
                pprint.pprint(discrepancies, indent=4, width=120)
    summarize_discrepancies(all_discrepancies)

if __name__ == "__main__":
    main()
