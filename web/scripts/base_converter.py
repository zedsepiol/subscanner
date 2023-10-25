class DataConverter(object):
    """
    Base class for data conversion.

    Attributes:
        data (list): The data to be converted.
    """

    def __init__(self, data):
        """
        Initialize the DataConverter class.

        Args:
            data (list): The data to be converted.
        """
        self.data = data


    def convert_data(self):
        pass


    def clear_data(self):
        """
        Clear the data.

        This method can be overridden in subclasses to add custom clearing logic.
        """
        self.data = []