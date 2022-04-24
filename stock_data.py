import csv

# CSV will be ported to postgresql


class Company:
    """Company stock ticker, name and sector."""

    def __init__(self, ticker: str, name: str, sector: str):
        self.ticker, self.name, self.sector = ticker, name, sector
        self.set_company_names(self.ticker, self.name)

    def set_company_names(self, ticker: str, name: str):
        """Set the company ticker and name as a key value pair."""
        self.company_names = {ticker: name}

    def get_company_names(self, ticker: str):
        """Get the company ticker and name as a key value pair."""
        return self.company_names


class CompanyDataset:
    """A set of company data."""

    def __init__(self, name: str, path: str = None):
        self.name, self.path = name, path
        if self.path != None:
            self.set_companies(self.import_stock_data(self.path))

    def set_companies(self, companies):
        self.companies = companies

    def get_companies(self):
        return self.companies

    def import_stock_data(self, path: str, delimiter='\t'):
        """Import a csv file and take the first 3 elements of each row as ticker, name, and sector.
        Return a dictionary of the company tickers and names."""
        companies: dict = {}
        with open(path) as file:
            data = csv.reader(file, delimiter=delimiter)
            for row in data:
                company = Company(row[0], row[1], row[2])
                companies.update({company.ticker: company})
        return companies


class Exchange(CompanyDataset):
    """Stock Exchange data set."""

    def __init__(self, name: str, path: str = None):
        super().__init__(name, path)
