import yaml
from collections import OrderedDict
"""
This script reads from YAML file "input.yaml", reorders the keys of each dictionary according to a specified order,
and prints the result to stdout in proper YAML format.
"""

# Desired key order for tools data
KEY_ORDER = ["id", "name", "description", "url", "catalog"]

def reorder_dict(d):
    """Reorder dictionary keys according to KEY_ORDER, keeping extra keys at the end."""
    ordered = OrderedDict()
    # Add keys in the desired order
    for key in KEY_ORDER:
        if key in d:
            ordered[key] = d[key]
    # Add any remaining keys not in KEY_ORDER
    for key in d:
        if key not in ordered:
            ordered[key] = d[key]
    return ordered

# Custom representer to print OrderedDict as normal YAML mapping
def represent_ordereddict(dumper, data):
    return dumper.represent_dict(data.items())

yaml.add_representer(OrderedDict, represent_ordereddict)

# Read the YAML file
with open("input.yaml", "r") as f:
    data = yaml.safe_load(f)

# Reorder keys
if isinstance(data, list):
    data = [reorder_dict(item) if isinstance(item, dict) else item for item in data]
elif isinstance(data, dict):
    data = reorder_dict(data)

# Print reordered YAML to stdout
print(yaml.dump(data, sort_keys=False, allow_unicode=True))