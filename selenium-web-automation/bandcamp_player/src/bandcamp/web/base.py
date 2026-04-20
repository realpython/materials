"""
Base classes to implement the Page Object pattern. This module also includes
a custom descriptor that mimics Java's @FindBy annotation, leveraging type
hints to infer the elements to search for.
"""

import typing
from dataclasses import dataclass
from typing import Self

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

MAX_WAIT_SECONDS = 10.0


class WebPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._wait = WebDriverWait(driver, MAX_WAIT_SECONDS)


class WebComponent:
    def __init__(self, parent: WebElement, driver: WebDriver = None) -> None:
        self._parent = parent
        if driver:
            self._driver = driver
            self._wait = WebDriverWait(driver, MAX_WAIT_SECONDS)


@dataclass
class SearchMode:
    many: bool
    cast: type | None = None

    @classmethod
    def of(cls, owner: type, name: str) -> Self:
        if type_hint := owner.__annotations__.get(name):
            if origin := typing.get_origin(type_hint):
                arg, *_ = typing.get_args(type_hint)
                if issubclass(origin, typing.Sequence):
                    return cls(many=True, cast=arg)
                else:
                    raise TypeError("Can only use generic sequences")
            else:
                if issubclass(type_hint, typing.Sequence):
                    return cls(many=True)
                else:
                    return cls(many=False, cast=type_hint)
        else:
            return cls(many=False)


class FindBy:
    def __init__(self, by: str, value: str, cache: bool = True) -> None:
        self._by = by
        self._value = value
        self._cache = cache

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = name

    def __get__(
        self, instance: WebPage | WebComponent, owner: type
    ) -> WebElement | list[WebElement] | WebComponent | list[WebComponent]:
        match instance:
            case WebPage():
                root = instance._driver  # Search within the entire HTML body
            case WebComponent():
                root = instance._parent  # Narrow down the search to a DOM node
            case _:
                raise TypeError("FindBy must be in WebPage or WebComponent")
        mode = SearchMode.of(owner, self._name)
        if mode.many:
            value = root.find_elements(self._by, self._value)
            if mode.cast:
                value = [mode.cast(x, instance._driver) for x in value]
        else:
            value = root.find_element(self._by, self._value)
            if mode.cast:
                value = mode.cast(value, instance._driver)
        if self._cache:
            setattr(owner, self._name, value)
        return value
