"""Selenium web driver implementations."""

from typing import Callable

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException


class LinuxChromeDriver(webdriver.Chrome):
    """Base driver class for Google Chrome."""

    def __init__(self, search_engine_url: str = "https://www.google.com") -> None:
        """Initialise LinuxChromeDriver."""
        options = Options()
        options.add_argument("--headless")  # Ensure GUI is off
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service("drivers/chromedriver_linux64/chromedriver")
        super().__init__(service=service, options=options)
        self.get(search_engine_url)
        self.accept_cookies()

    # Refactor elementexists and elementinteractable into one decorator function
    def elementexists(fn: Callable) -> Callable:
        """Check that a target element exists on the page."""

        def exists_check(*args: tuple):
            """Wrapper function."""
            try:
                search = fn(*args)
            except NoSuchElementException as ex:
                print(f"{type(ex).__name__}: Element {args[1]} was not found")
                raise NoSuchElementException
            return search

        return exists_check

    def elementinteractable(fn: Callable) -> Callable:
        """Check that a target element is not interactable."""

        def interactable_check(*keys: tuple):
            """Wrapper function."""
            try:
                search = fn(*keys)
            except ElementNotInteractableException as ex:
                print(f"{type(ex).__name}: Element is not interactable")
                raise ElementNotInteractableException
            return search

        return interactable_check

    @elementinteractable
    def accept_cookies(self, by: str = By.ID, cookies_identifier: str = "L2AGLb") -> WebElement:
        """Accept cookies on the web page by cookies element identifier - defaults to Google."""
        self.find_element(by, cookies_identifier).click()

    @elementexists
    def get_element(self, by: str = By.NAME, element: str = "q"):
        """Find element in current page - defaults to Google search bar."""
        return self.find_element(by, element)

    @elementinteractable
    def enter_keystrokes(self, search: WebElement, query: str, all_keystrokes: list[tuple[str, str]] | None = None) -> None:
        """
        Enter keystrokes into a given interactable element.

        By default, clear previous input, then add new input and enter it.
        """
        if all_keystrokes is None:
            all_keystrokes = [(Keys.CONTROL, "a"), (query, Keys.RETURN)]
        for keystrokes in all_keystrokes:
            if search:
                search.send_keys(keystrokes)


class SearchDriver(LinuxChromeDriver):
    """Specific ChromeDriver for searching."""

    def __init__(self) -> None:
        """Initialise SearchDriver."""
        super().__init__()

    def new_search(self, query: str, identifier: str = "q", by: str = By.NAME) -> None:
        """Get an interactable element on the page and enter a new search query."""
        search = self.get_element(identifier, by)
        self.enter_keystrokes(search, query)

    def get_element(self, identifier: str, by: str = By.CLASS_NAME, timeout: float = 0.5) -> WebElement | bool:
        """Get the raw text from a specified element containing text."""
        try:
            element = WebDriverWait(self, timeout).until(EC.presence_of_element_located((by, identifier)))
        except TimeoutException as ex:
            print(ex)
            print(f"{type(ex).__name__}: Waited {timeout}s for {identifier} but it was not located")
            return False
        return element

    def google_text_search(
        self, query: str, identifier: str = "webanswers-webanswers_table__webanswers-table", by: str = By.CLASS_NAME
    ) -> str | bool:
        """Search Google and return matching raw text element."""
        self.new_search(query)
        element = self.get_element(identifier, by)
        if element:
            return element.text
        else:
            return False
