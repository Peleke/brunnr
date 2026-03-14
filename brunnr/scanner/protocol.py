"""Rule protocol — structural type for scanner rules.

Any class with a `name: str` attribute and a `scan(ctx) -> list[Finding]`
method satisfies this protocol. No inheritance required.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from brunnr.scanner.context import ScanContext
from brunnr.scanner.types import Finding


@runtime_checkable
class Rule(Protocol):
    """A single scanner rule."""

    name: str

    def scan(self, ctx: ScanContext) -> list[Finding]: ...
