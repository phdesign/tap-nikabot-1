from logging import Logger
from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

# Ignore other attributes, we just want to fix the decorator
def __getattr__(attr: str) -> Any: ...
def handle_top_exception(logger: Logger) -> Callable[[F], F]: ...