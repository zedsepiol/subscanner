import requests

class DataFetcher:
    """
    The DataFetcher class allows making HTTP requests to fetch data.

    Methods:
        fetch_data(url): Fetches data from the provided URL.
    """

    def __init__(self):
        """
        Initializes the DataFetcher class.

        This constructor does not require any arguments as the base URL is provided when calling fetch_data.

        Attributes:
            None
        """
        self.__base_uri = "https://crt.sh/"


    def __repr__(self):
        """
        Returns a string representation of the DataFetcher class.

        Returns:
            str: A string representing the DataFetcher class.
        """
        return "DataFetcher"


    def fetch_data(self, url: str):
        """
        Fetches data from a specified URL and extracts common names from the JSON response.

        Args:
            url (str): The URL from which to fetch data.

        Returns:
            list: A list of common names from the JSON response.
        """

        query = f"?q={url.strip('https://')}&output=json"
        response = requests.get(self.__base_uri+query)
        response = response.json()

        if response == []:
            return False
        
        domains = []

        for item in response:
            common_name = item.get("common_name", "Not found!")

            if common_name and not common_name.startswith("*."):
                domains.append(common_name)
        
        return list(set(domains))
