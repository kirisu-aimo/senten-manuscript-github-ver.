from __future__ import annotations
from enum import StrEnum, auto
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


class Emoji(StrEnum):
    BOOK = ":open_book:"
    PAGE = ":page_facing_up:"

def markdown_link(title:str, link:str):
    return f"[{title}]({link})"


class NestingMeta(metaclass=ABCMeta):
    @property
    @abstractmethod
    def nesting_count(self) -> int:
        pass
    @abstractmethod
    def set_child(self, child: Header) -> None:
        pass
    @property
    @abstractmethod
    def children(self) -> list[Header]:
        pass
    @property
    @abstractmethod
    def link(self) -> str:
        pass
    @property
    @abstractmethod
    def top(self) -> Page:
        pass
    @property
    @abstractmethod
    def formatted_for_tb_row(self) -> str:
        pass

class Nesting:
    def __init__(self) -> None:
        self.title:str

class Page(NestingMeta):
    max_nesting_count: int = 0
    def __init__(
            self,
            title:str,
            date:str,
            link:str,
            ) -> None:
        self.title:str = title
        self.date:str = date
        self._link:str = link
        self._children: list[Header] = []
    @property
    def nesting_count(self) -> int:
        return 0
    def set_child(self, child: Header) -> None:
        self.children.append(child)
    @property
    def children(self) -> list[Header]:
        return self._children
    @property
    def link(self) -> str:
        return self._link
    @property
    def top(self) -> Page:
        return self


def format_header_to_link(title:str) -> str:
    return "#" + title

class Header(NestingMeta):
    def __init__(
            self,
            title:str,
            date:str,
            parent:NestingMeta,
            ) -> None:
        self.title:str = title
        self.date: str = date
        parent.set_child(self)
        self.parent: NestingMeta = parent
        self.number: int = len(self.parent.children) - 1
        self._children:list[Header] = []
    @property
    def nesting_count(self) -> int:
        count:int = self.parent.nesting_count + 1
        if count > Page.max_nesting_count:
            Page.max_nesting_count = count
        return count
    def set_child(self, child: Header) -> None:
        self.children.append(child)        
    @property
    def children(self) -> list[Header]:
        return self._children
    @property
    def link(self) -> str:
        return self.top.link + format_header_to_link(self.title)
    @property
    def top(self) -> Page:
        return self.parent.top
    

# ┬──
# ├─┬
# │ └