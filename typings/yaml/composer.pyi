"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, Optional

from yaml.error import MarkedYAMLError
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

"""
This type stub file was generated by pyright.
"""

class ComposerError(MarkedYAMLError): ...

class Composer:
    anchors: Dict[Any, Node]
    def __init__(self) -> None: ...
    def check_node(self) -> bool: ...
    def get_node(self) -> Optional[Node]: ...
    def get_single_node(self) -> Optional[Node]: ...
    def compose_document(self) -> Optional[Node]: ...
    def compose_node(self, parent: Optional[Node], index: int) -> Optional[Node]: ...
    def compose_scalar_node(self, anchor: Dict[Any, Node]) -> ScalarNode: ...
    def compose_sequence_node(self, anchor: Dict[Any, Node]) -> SequenceNode: ...
    def compose_mapping_node(self, anchor: Dict[Any, Node]) -> MappingNode: ...