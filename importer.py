import requests

class Importer:
    base_uri = "https://api.cartolafc.globo.com"

    def __init__(self):
        pass

    def get_rounds(self):
        try:
            response = requests.get(f"{self.base_uri}/rodadas")
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Create an instance of Importer
importer = Importer()

# Call the get_rounds method
rounds_data = importer.get_rounds()
print(rounds_data)