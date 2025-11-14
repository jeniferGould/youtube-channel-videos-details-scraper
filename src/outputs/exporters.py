thonimport json

def export_to_json(data, filename):
    """
    Export parsed data to a JSON file.
    :param data: Data to be exported.
    :param filename: The output filename (e.g., "output.json").
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data has been exported to {filename}")