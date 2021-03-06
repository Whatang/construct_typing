from __future__ import annotations
from typing import (
    Any,
    Hashable,
    List,
    KeysView,
    ValuesView,
    ItemsView,
    Iterator,
    Mapping as TypingMapping,
    Union as TypingUnion,
    Tuple as TypingTuple,
    Pattern,
    Iterable,
)

globalPrintFullStrings: bool
globalPrintFalseFlags: bool
globalPrintPrivateEntries: bool

def setGlobalPrintFullStrings(enabled: bool = ...) -> None: ...
def setGlobalPrintFalseFlags(enabled: bool = ...) -> None: ...
def setGlobalPrintPrivateEntries(enabled: bool = ...) -> None: ...
def recursion_lock(retval: str = ..., lock_name: str = ...): ...

class Container(dict):
    __slots__: List[str] = ...
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value: Any): ...
    def __delattr__(self, name: str): ...
    def __setitem__(self, key: Hashable, value: Any) -> None: ...
    def __delitem__(self, key: Hashable) -> None: ...
    __keys_order__: List[str] = ...
    def __init__(
        self,
        *args: Iterable[TypingUnion[dict, Iterable[TypingTuple[str, Any]]]],
        **entrieskw: TypingMapping[str, Any]
    ) -> None: ...
    def __call__(self, **entrieskw: TypingMapping[str, Any]): ...
    def keys(self) -> KeysView[str]: ...
    def values(self) -> ValuesView: ...
    def items(self) -> ItemsView[str, Any]: ...
    def __iter__(self) -> Iterator[str]: ...
    def clear(self) -> None: ...
    def pop(self, key: str): ...  # type: ignore
    def popitem(self): ...
    def update(  # type: ignore
        self,
        seqordict: TypingUnion[
            TypingMapping[str, Any], Iterable[TypingTuple[str, Any]]
        ],
    ) -> None: ...
    def __getstate__(self) -> List[str]: ...
    def __setstate__(self, state: List[str]) -> None: ...
    def copy(self) -> Container: ...
    def __dir__(self) -> List[str]: ...
    def __eq__(self, other: TypingUnion[Container, TypingMapping]) -> bool: ...  # type: ignore
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _search(self, compiled_pattern: Pattern, search_all: bool) -> List[Any]: ...
    def search(self, pattern: str) -> List[Any]: ...
    def search_all(self, pattern: str) -> List[Any]: ...

class ListContainer(list):
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _search(self, compiled_pattern: Pattern, search_all: bool) -> List[Any]: ...
    def search(self, pattern: str) -> List[Any]: ...
    def search_all(self, pattern: str) -> List[Any]: ...
