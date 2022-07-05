from logger import Logger


class WebSource:
    """WebSource website object."""

    def __init__(self, name: str, log=Logger.custom_logger(__file__)):
        """Initialise WebSource."""
        self.name = name
