import re
import requests


class URLValidator(object):
    """
    URLValidator validates whether a given URL conforms to a specific regex pattern.
    
    Args:
        pattern (str): The regex pattern that the URL should conform to.

    Attributes:
        pattern (re.Pattern): The regex pattern used to check URL conformity.

    Methods:
        is_valid_url(url: str) -> bool: Checks if the provided URL conforms to the pattern.
    """

    def __init__(self):
        """
        Initializes the URLValidator class.
        """
        self.pattern = re.compile(r"^(http|https|)://(?!.*\.\.)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})(/.*)?$")


    def __repr__(self) -> str:
        """
        Returns a string representation of the URLValidator object.

        Returns:
            str: A string representation of the URLValidator, including its regex pattern.
        """
            
        return f"URLValidator(pattern={self.pattern.pattern})"


    def is_valid_url(self, url: str) -> bool:
        """
        Checks if the provided URL conforms to the specified pattern.

        Args:
            url (str): The URL to be checked.

        Returns:
            bool: True if the URL conforms to the pattern, False otherwise.
        """
        return bool(self.pattern.match(url))


class HTTPValidator(object):
    """
    The HTTPValidator class sends an HTTP request to a given URL and checks the response status code.

    Returns:
        bool: True if the URL's response status is 200 OK, False otherwise.
    """

    def __init__(self):
        """
        Initializes the HTTPValidator class.
        """
        pass


    def __repr__(self):
        """
        Returns a string representation of the HTTPValidator object.
        """
        return "HTTPValidator"


    def is_valid_http_status(self, url):
        """
        Checks the response status of the given URL.

        Args:
            url (str): The URL to be checked.

        Returns:
            bool: True if the URL's response status is 200 OK, False otherwise.
        """
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
