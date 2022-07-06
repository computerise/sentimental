from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


from sentimental.logger import Logger

WEBDRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
SEARCH_ENGINE_PATH = 'https://www.google.com'
log = Logger.custom_logger(__file__, 'DEBUG')


class ChromeDriver(webdriver.Chrome):
    """Base driver class for Google Chrome."""

    def __init__(self, webdriver_path=WEBDRIVER_PATH, search_engine_path=SEARCH_ENGINE_PATH):
        super().__init__(webdriver_path)
        self.get(search_engine_path)
        self.accept_cookies()

    # Refactor elementexists and elementinteractable into one decorator function
    def elementexists(fn):
        """Decorator function to check that a target element exists on the page"""
        def exists_check(*args):
            try:
                search = fn(*args)
            except NoSuchElementException as ex:
                log.critical(
                    f'{type(ex).__name__}: Element {args[1]} was not found')
                search = False
            return search
        return exists_check

    def elementinteractable(fn):
        """Decorator function to check that a target element is not interactable"""
        def interactable_check(*keys):
            try:
                search = fn(*keys)
            except ElementNotInteractableException as ex:
                log.critical(
                    f'{type(ex).__name}: Element is not interactable')
                search = False
            return search
        return interactable_check

    def accept_cookies(self, by=By.ID, cookies_identifier='L2AGLb'):
        """Accept cookies on the webpage. Default accepts cookies for Google."""
        self.find_element(by, cookies_identifier).click()

    @elementexists
    def get_element(self, by=By.NAME, element='q'):
        """Finds element in current page."""
        search_bar = self.find_element(by, element)
        return search_bar

    @elementinteractable
    def enter_keystrokes(self, search: WebElement, query: str, all_keystrokes=None):
        """Enters keystrokes into a given interactable element. By default, clear previous input, then add new input and enter it."""
        if all_keystrokes is None:
            all_keystrokes = [(Keys.CONTROL, 'a'), (query, Keys.RETURN)]
        for keystrokes in all_keystrokes:
            if search:
                search.send_keys(keystrokes)


class SearchDriver(ChromeDriver):
    """Specific ChromeDriver for searching."""

    def __init__(self):
        super().__init__()

    def new_search(self, query: str, identifier='q', by=By.NAME):
        """Get an interactable element on the page and enter a new search query."""
        search = self.get_element(identifier, by)
        self.enter_keystrokes(search, query)

    def get_element(self, identifier, by=By.CLASS_NAME, timeout=0.5):
        """Get the raw text from a specified element containing text."""
        try:
            element = WebDriverWait(self, timeout).until(
                EC.presence_of_element_located((by, identifier)))
        except TimeoutException as ex:
            print(ex)
            log.warning(
                f'{type(ex).__name__}: Waited {timeout}s for {identifier} but it was not located')
            return False
        return element

    def google_text_search(self, query: str, identifier='webanswers-webanswers_table__webanswers-table', by=By.CLASS_NAME) -> str:
        """Search Google and return matching raw text element."""
        self.new_search(query)
        element = self.get_element(identifier, by)
        if element:
            return element.text
        else:
            return False
