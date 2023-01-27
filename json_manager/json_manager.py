import os
import json


class JsonManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def check_file(self):
        return os.path.exists(self.json_file_path)

    def create_file(self):
        with open(self.json_file_path, 'w') as f:
            pass

    def write_json(self, new_data):
        try:
            with open(self.json_file_path, 'r') as f:
                loaded_data = json.load(f)
        except json.decoder.JSONDecodeError:
            loaded_data = []
        finally:
            with open(self.json_file_path, 'w') as f:
                loaded_data.append(new_data)
                json.dump(loaded_data, f, indent=4)


