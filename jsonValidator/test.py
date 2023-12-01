import json

def compare_json_files(xs, local):
    try:
        with open(xs, 'r') as xsFile, open(local, 'r') as localFile:
            xsData = json.load(xsFile)
            localData = json.load(localFile)

            def sort_json(obj):
                if isinstance(obj, dict):
                    return sorted((key, sort_json(value)) for key, value in obj.items())
                elif isinstance(obj, list):
                    return sorted(sort_json(element) for element in obj)
                else:
                    return obj

            return sort_json(xsData['data']) == sort_json(localData['data'])

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error: {e}")
        return False

def main():
    xs = './xs.json'
    local = './local.json'

    if compare_json_files(xs, local):
        print("JSON files are identical.")
    else:
        print("JSON files are different.")

if __name__ == "__main__":
    main()
