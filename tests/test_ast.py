from amber.core import Core
from amber.ast import AST, Node
from amber.elements import ELEMENTS


class TestAST:

    def test_build_tree(self):
        core = Core(elements=ELEMENTS, template_path="templates")
        core.get_template("index.amber")
        template = core.template_list
        assert template == ["div.my-class:\n", '    h1 "hello!"\n']

        ast = AST(template)
        ast.build_tree()
        result = ast.node_tree
        expected = [
            {
                "node": Node(value="div", operator=None),
                "children": [
                    {
                        "node": Node(value="class", operator="="),
                        "children": [
                            {
                                "node": Node(value="my-class", operator=None),
                                "children": [
                                    {
                                        "node": Node(value="h1", operator=None),
                                        "children": [
                                            {
                                                "node": Node(value="hello!", operator=None),
                                                "children": None,
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                ]
            }
        ]
        assert result == expected
