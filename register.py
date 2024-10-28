import json

class Register:
    def _init_(self):
        pass

    def save_data(self, data):
        with open("./data/all_rounds.json", "w") as f:
            json_data = json.dumps(data)
            f.write(json_data)
