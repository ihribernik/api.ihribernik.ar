from typing import Any


class Service:
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
