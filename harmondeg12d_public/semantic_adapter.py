
from typing import Protocol, Any
class SemanticAdapter(Protocol):
    """Replaceable semantic-intelligence contract. It may deepen reconstruction but may not alter canonical Harmondeg rules."""
    name: str
    def reconstruct(self, text: str, *, target: str, scope: str) -> dict[str, Any]: ...
    def test_dimension(self, code: str, reconstruction: dict[str, Any], specification: dict[str, Any]) -> dict[str, Any]: ...
