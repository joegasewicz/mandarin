from amber.core import Core
from amber.ast import AST, Node, NodeLine
from amber.elements import ELEMENTS


class TestAST:

    def test_build_tree(self):
        core = Core(elements=ELEMENTS, template_path="templates")
        core.get_template("index.amber")
        template = core.template_list

        assert template == ["div:\n", '    "hello"\n']

        ast = AST(template)
        result = ast.build_tree()

        expected = NodeLine(index=0, elem_line=None, nodes=[], child=NodeLine(
            index=1, elem_line="div:\n", nodes=[Node(elem_name="div", value=None)], child=NodeLine(
                index=2, elem_line='    "hello"\n', nodes=[Node(elem_name=None, value='    "hello"')], child=None),
            ),
        )

        assert result == expected


    def test_create_nodes(self):
        core = Core(elements=ELEMENTS, template_path="templates")
        core.get_template("index.amber")
        template = core.template_list

        assert template == ["div:\n", '    "hello"\n']

        nl = NodeLine(index=0, elem_line=None, nodes=[], child=NodeLine(
            index=1, elem_line="div:\n", nodes=[], child=NodeLine(
                index=2, elem_line='    "hello"\n', nodes=[], child=None),
            ),
        )

        ast = AST(template)
        ast.create_nodes(nl)

        expected = NodeLine(index=0, elem_line=None, nodes=[], child=NodeLine(
            index=1, elem_line="div:\n", nodes=[Node(elem_name="div", value=None)], child=NodeLine(
                index=2, elem_line='    "hello"\n', nodes=[Node(elem_name=None, value='    "hello"')], child=None),
            ),
        )
        assert nl == expected

    def test_create_node_line(self):
        core = Core(elements=ELEMENTS, template_path="templates")
        core.get_template("index.amber")
        template = core.template_list

        assert template == ["div:\n", '    "hello"\n']

        i = 1
        node_line = NodeLine(index=0)
        ast = AST(template)
        ast.create_node_line(node_line, ast.template, i)

        expected = NodeLine(index=0, elem_line=None, nodes=[], child=NodeLine(
            index=1, elem_line="div:\n", nodes=[], child=NodeLine(
                index=2, elem_line='    "hello"\n', nodes=[], child=None),
            ),
        )
        assert expected.index == node_line.index
        assert expected.child.index == node_line.child.index
        assert expected.child.child.index == node_line.child.child.index
        assert not hasattr(node_line.child.child.index, "child")
        assert expected.child.elem_line == node_line.child.elem_line
        assert expected.child.child.elem_line == node_line.child.child.elem_line
