import typing as t


_Validator = t.Union[type, t.List[type], t.Callable[[t.Any], bool], "_Operater", None]

class _Operater:
    def __init__(self, *args: _Validator, **kwargs: t.Any) -> None:...

class And(_Operater):...

class Or(_Operater):...

class Use(_Operater):
    def __init__(self, transformer: t.Callable[[t.Any], t.Any]) -> None:...


class Optional:
    def __init__(self, key: str, *args: t.Any, **kwargs: t.Any) -> None:...


class Schema:
    def __init__(self,
        mapping: t.Dict[t.Union[Optional, str], t.Any],
    ) -> None:...

    def validate(self, data: t.Any) -> t.Any:...


class SchemaError(Exception):...


__all__ = ['And', 'Or', 'Schema', 'SchemaError', 'Use', 'Optional']