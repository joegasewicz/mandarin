from citrine.parser import Parser
from citrine.ast import Node


class TestParser:

    def test_parse(self):
        parser = Parser()

        node = Node(elem_name="div", value=None)
        element = parser.parse(node)
        assert element == ("<div>", "</div>")

        node = Node(elem_name="h1", value=None)
        element = parser.parse(node)
        assert element == ("<h1>", "</h1>")

        node = Node(elem_name=None, value="    'hello!'")
        element = parser.parse(node)
        assert element == "hello!"
