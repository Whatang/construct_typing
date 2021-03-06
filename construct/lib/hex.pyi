from __future__ import annotations
from typing import List

class HexDisplayedInteger(int):
    def __str__(self) -> str: ...
    def new(intvalue, fmtstr) -> HexDisplayedInteger: ...

class HexDisplayedBytes(bytes):
    def __str__(self) -> str: ...

class HexDisplayedDict(dict):
    def __str__(self) -> str: ...

class HexDumpDisplayedBytes(bytes):
    def __str__(self) -> str: ...

class HexDumpDisplayedDict(dict):
    def __str__(self) -> str: ...

# Map an integer in the inclusive range 0-255 to its string byte representation
PRINTABLE = List[str]
HEXPRINT = List[str]

def hexdump(data: bytes, linesize: int) -> str: ...
def hexundump(data: str, linesize: int) -> bytes: ...
