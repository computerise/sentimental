import csv
from sentimental.database_connector import Database

# CSV will be ported to postgresql


class DataObject:
    """Placeholder generic data object."""

    def __init__(self, id):
        self.id = id


class Company(DataObject):
    """Company stock ticker, name and sector."""

    def __init__(self, raw_data: list):
        self.ticker, self.name, self.sector = raw_data
        super().__init__(self.ticker)
        self.company_names = {self.ticker: self.name}
        self.sectors = {self.ticker: self.sector}


class Dataset:
    """A set of generic data."""

    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name
        self.entries = self.format_data(dataset_name)

    def import_data(self, path: str, data_object: DataObject, delimiter='\t'):
        """Import a CSV file and take the elements of each row as a data entry.
        Return a dictionary of the IDs and DataObjects."""
        imported_data: dict = {}
        with open(path) as file:
            data = csv.reader(file, delimiter=delimiter)
            for row in data:
                entry = data_object(row)
                imported_data.update({entry.id: entry})
        return imported_data

    def format_data(self, table_name, data_object=Company):
        """Format database output to currently used format. Improve this with SQL queries."""
        self.database = Database()
        formatted_data: dict = {}
        data = self.database.get_all(table_name)
        for item in data:
            formatted_data.update(
                {item.get('ticker'): data_object(item.values())})
        return formatted_data


class CompanyDataset(Dataset):
    """Placeholder Company data set."""

    def __init__(self, name: str):
        super().__init__(name)


class Exchange(CompanyDataset):
    """Placeholder Stock Exchange data set."""

    def __init__(self, name: str):
        super().__init__(name)
