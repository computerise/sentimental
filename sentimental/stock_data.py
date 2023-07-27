"""Stock data model."""

import csv
from typing import TextIO

from sentimental.database_connector import Database


class DataObject:
    """Generic data object."""

    def __init__(self, id: str) -> None:
        """Initialise DataObject."""
        self.id = id


class Company(DataObject):
    """Company stock ticker, name and sector."""

    def __init__(self, raw_data: list[str]) -> None:
        """Initialise Company."""
        self.ticker, self.name, self.sector = raw_data
        super().__init__(self.ticker)


class Dataset:
    """A set of generic data."""

    def __init__(self, data_object: type[DataObject] | type[Company], data: dict) -> None:
        """Initialise Dataset."""
        self.data_type = data_object
        self.__dict__.update(data)


class SQLDataset(Dataset):
    """Dataset class for SQL data."""

    def __init__(self, data_object: type[DataObject] | type[Company], database: Database, table_name: str) -> None:
        super().__init__(data_object, self.retrieve_data(database, table_name, data_object))

    def retrieve_data(
        self, database: Database, table_name: str, data_object: type[DataObject] | type[Company] = Company
    ) -> dict:
        """Format database output."""
        formatted_data: dict = {}
        data = database.get_all(table_name)
        for item in data:
            formatted_data.update({item.get("ticker"): data_object(item.values())})
        return formatted_data


class CSVDataset(Dataset):
    """Dataset class for local CSV data."""

    def __init__(self, data_object: type[DataObject] | type[Company], csv_file: TextIO, delimiter: str = "\t") -> None:
        """Initialise CSVDataset."""
        super().__init__(data_object, self.retrieve_data(data_object, csv_file, delimiter))

    def retrieve_data(self, data_object: DataObject | Company, csv_file: TextIO, delimiter: str) -> dict:
        """
        Import a CSV file and take the elements of each row as a data entry.

        Return a dictionary of the IDs and DataObjects.
        """
        imported_data: dict = {}
        data = csv.reader(csv_file, delimiter=delimiter)
        for row in data:
            entry = data_object(row)
            imported_data.update({entry.id: entry})
        return imported_data
