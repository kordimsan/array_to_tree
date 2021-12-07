from typing import Any, List
from pydantic import BaseModel


class Node(BaseModel):
    id: Any
    pid: Any


class NodeArray(BaseModel):
    nodes: List[Node]


def validate_tree(tree):
    return [Node(**node) for node in tree]
