from __future__ import annotations
from enum import StrEnum, auto
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
import pyperclip


def markdown_link(title:str, link:str):
    return f"[{title}]({link})"


class Nested(metaclass=ABCMeta):
    def __init__(
            self,
            title:str,
            date:str,
            ) -> None:
        self.title:str = title
        self.date:str = date
        
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
    def formated_for_tb_row(self) -> str:
        _hash = '#' + ' > #' * self.nesting_count
        _title = markdown_link(_hash, self.link) + ' - ' + self.title
        _date = self.date
        return f'|{'|'.join((_title, _date))}|'


class Page(Nested):
    max_nesting_count: int = 0
    def __init__(
            self,
            title:str,
            date:str,
            filename:str,
            ) -> None:
        super().__init__(title, date)
        self._filename:str = filename
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
        return self._filename
    @property
    def top(self) -> Page:
        return self


def format_header_to_link(title:str) -> str:
    title = title.replace('，', '')
    title = title.replace('．', '')
    title = title.replace('？', '')
    title = title.replace('/', '')
    title = title.replace('@', '')
    title = title.replace('"', '')
    title = title.replace(' ', '-')
    return "#" + title

class Header(Nested):
    def __init__(
            self,
            title:str,
            date:str,
            parent:Nested,
            ) -> None:
        super().__init__(title, date)
        parent.set_child(self)
        self.parent: Nested = parent
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

if __name__ == '__main__':
    pass
    contents: list[Nested] = []


    # 表記法の役割
    contents.append(Page(
        title='『表記法の役割』',
        date='25/08/13',
        filename='role_of_notations.md'
        ))
    page = contents[-1]
    contents.append(Header(
        title='伝わらない表記法をなぜ生み出したのか，みなさんは理解不能だろうか？',
        date='25/08/13',
        parent=page
        ))
    contents.append(Header(
        title='"サピア・ウォーフの仮説" @ 旋転界',
        date='25/08/14',
        parent=page
        ))
    contents.append(Header(
        title='表記法である必要はない，理論は感覚を超えられないから',
        date='25/08/16',
        parent=page
        ))
    contents.append(Header(
        title='慣用-理論のグラデーション',
        date='25/08/18',
        parent=page
        ))
    contents.append(Header(
        title='表記法の一般かと特殊化',
        date='25/08/19',
        parent=page
        ))
    contents.append(Header(
        title='表記法すなわち"世界"の創り方',
        date='25/08/20',
        parent=page
        ))
    
    
    # 表記法入門
    contents.append(Page(
        title='『表記法入門』',
        date='25/08/20 ~',
        filename='an_introduction_of_notation.md',
        ))
    page = contents[-1]
    contents.append(Header(
        title='慣用表現が抱える課題',
        date='25/08/20 ~',
        parent=page,
        ))
    section = contents[-1]
    contents.append(Header(
        title='単体技のフィンガースイッチの回数が不定である',
        date='25/08/20',
        parent=section,
        ))
    contents.append(Header(
        title='回転についての記述に規則性がない',
        date='25/08/21',
        parent=section,
        ))
    contents.append(Header(
        title='接辞の整理が不十分である',
        date='25/08/22',
        parent=section,
        ))
    contents.append(Header(
        title='理論表記法による課題解決',
        date='25/08/24 ~',
        parent=page,
        ))
    section = contents[-1]
    contents.append(Header(
        title='新しい接辞はどのようなものか',
        date='25/08/24',
        parent=section,
        ))
    contents.append(Header(
        title='単位表記法とはなにか',
        date='25/08/25',
        parent=section,
        ))
    contents.append(Header(
        title='接とはなにか',
        date='25/08/26',
        parent=section,
        ))
    
    # 反転操作・並進操作・回転操作
    contents.append(Page(
        title='『反転操作・並進操作・回転操作』',
        date='25/08/17 ~ ',
        filename='expansion_of_operations.md',
        ))
    page = contents[-1]
    contents.append(Header(
        title='操作の拡張',
        date='25/08/17',
        parent=page,
        ))
    contents.append(Header(
        title='操作の合成と比較',
        date='25/08/17',
        parent=page,
        ))
    
    # フィンガースイッチの図解分析
    contents.append(Page(
        title='『フィンガースイッチの図解分析』',
        date='25/08/24 ~',
        filename='expansion_of_operation.md',
        ))
    page = contents[-1]
    contents.append(Header(
        title='スロットに関する数的表現',
        date='25/08/24',
        parent=page,
        ))
    contents.append(Header(
        title='フィンガースイッチの数的表現',
        date='未定',
        parent=page,
        ))

    # 表作成
    textline: list[str] = [
        '|Title|Date|',
        '|:-|:-|'
    ]
    for c in contents:
        print(c.formated_for_tb_row)
        textline.append(c.formated_for_tb_row)
    pyperclip.copy('\n'.join(textline))


    