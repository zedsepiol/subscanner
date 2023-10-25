from web.scripts.base_converter import *


class TXTConverter(DataConverter):
    """
    Subclass for converting data to TXT format.

    This class inherits from DataConverter and provides the capability to convert data
    to plain text format.

    Methods:
        convert_data(): Converts the data to a plain text format.
    """

    def convert_data(self):
        """
        Convert data to plain text format.

        Returns:
            str: The data in plain text format.
        """

        self.data = "\n".join(item.__str__() for item in self.data)

        return self.data