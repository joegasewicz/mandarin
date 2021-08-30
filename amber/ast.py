from typing import List, Dict
from collections import namedtuple


Node = namedtuple(
    "Node",
    ["elem_name", "value"],
    defaults=[None, None],
)
NodeLine = namedtuple(
    "NodeLine",
    ["index", "elem_line", "nodes", "child"],
    defaults=[None, None, [], None],
)
SEPARATORS = (".", "#", " ")
ELEMENTS = ("div", "h1")


class AST:
    """
    - Each item in the template list gets assigned to a NodeLine
    """
    node_line_head: List[NodeLine]

    def __init__(self, template: List[str]):
        self.template = template

    def create_node(self, node_line: NodeLine):
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
            self.create_node(node_line.child)
        elif node_line.child:
            self.create_node(node_line.child)
        else:
            pass

    def create_node_line(self, parent_node: NodeLine, template, i: int):
        if len(template):
            elem_line = template.pop(0)
            nl = NodeLine(index=i, elem_line=elem_line, nodes=[], child=None)
            parent_node.child = nl
            i += 1
            self.create_node_line(nl, template, i)

    def build_tree(self):
        elem_name: str
        value: str
        operator: str
        children: List[Node]
        # Create NodeLines
        i = 1
        n = NodeLine(index=0)
        self.create_node_line(n, self.template, i)
        # Process Lines into nodes
        return n

    def walk(self):
        t = self.build_tree()

