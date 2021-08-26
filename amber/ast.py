from typing import List, Dict
from collections import namedtuple

Node = namedtuple("Node", ["value", "operator"], defaults=[None, None])

SEPARATORS = (".", "#", " ")

class AST:

    _node_tree = []

    def __init__(self, template: List[str]):
        self.template = template

    @property
    def node_tree(self):
        return self._node_tree

    def create_node(self, chunk: str, separator: str):
        if separator in chunk:
            nodes = chunk.split(separator)
            for n in nodes:
                if n:
                    node = Node(value=n)
                    self.node_tree.append(node)

    def build_tree(self, prev_node: Dict = None):
        for t in reversed(self.template):
            for separator in SEPARATORS:
                if separator in t:
                    for elem in t.split(separator):
                        if elem:
                            n = Node(value=elem)
                            node = {
                                "node": n,
                                "children": prev_node,
                            }
                            self.build_tree(node)
                else:
                    pass




    def walk(self):
        t = self.build_tree()

