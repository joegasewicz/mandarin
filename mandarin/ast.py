from typing import List, Dict, Union, Optional
from collections import namedtuple
from mandarin.parser import Parser
from mandarin.core import ELEMENTS

Node = namedtuple("Node", ["elem_name", "value"], defaults=[None, None])


class NodeLine:

    def __init__(
            self,
            *,
            index: int = None,
            elem_line: str = None,
            nodes: List = [],
            child: "NodeLine" = None,
    ):
        self.index = index
        self.elem_line = elem_line
        self.nodes = nodes
        self.child = child


class AST:
    """
    - Each item in the template list gets assigned to a NodeLine
    """
    node_line_head: List[NodeLine]

    tree: NodeLine

    parser = Parser()

    _template_str: str = ""

    @property
    def template_str(self) -> str:
        return self._template_str

    @template_str.setter
    def template_str(self, value: str):
        self._template_str = value

    def __init__(self, template: List[str]):
        self.template = template

    def create_nodes(self, node_line: NodeLine):
        elem_line = ""
        if not node_line:
            pass
        elif node_line.elem_line:
            if ":\n" in node_line.elem_line:
                elem_line, _ = node_line.elem_line.split(":\n")
            elif "\n" in node_line.elem_line:
                elem_line, _ = node_line.elem_line.split("\n")
            # Check is elem_line is an element or a string
            if elem_line in ELEMENTS:
                n = Node(elem_name=elem_line)
            else:
                # Must be a string value
                n = Node(value=elem_line)
            node_line.nodes.append(n)
            self.create_nodes(node_line.child)
        elif node_line.child:
            self.create_nodes(node_line.child)
        else:
            pass

    def create_node_line(self, parent_node: NodeLine, template, i: int):
        if len(template):
            elem_line = template.pop(0)
            nl = NodeLine(index=i, elem_line=elem_line, nodes=[], child=None)
            parent_node.child = nl
            i += 1
            self.create_node_line(nl, template, i)

    def build_tree(self) -> NodeLine:
        elem_name: str
        value: str
        operator: str
        children: List[Node]
        # Create NodeLines
        i = 1
        nl = NodeLine(index=0)
        self.create_node_line(nl, self.template, i)
        # Process Lines into nodes
        self.create_nodes(nl)
        self.tree = nl
        return nl

    def walk(self):
        tree = self.build_tree()
        for node in tree.child.nodes:
            start, end = self.parser.parse(node)
            self.template_str += start
            next_node_line = self.visit_node_line(2)
            for next_node in next_node_line.nodes:
                if not next_node.elem_name:
                    value = self.parser.parse(next_node)
                    self.template_str += value
            self.template_str += end

    def visit_node_line(self, index: int) -> Optional[NodeLine]:
        _node_line: Optional[NodeLine] = None
        if index == 0:
            return self.tree
        for i in range(index):
            if i == index:
                break
            elif _node_line:
                _node_line = getattr(_node_line, "child", None)
            else:
                _node_line = getattr(self.tree, "child", None)
        return _node_line
