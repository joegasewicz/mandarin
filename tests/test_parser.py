from mandarin.parser import Parser
from mandarin.ast import Node


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

        node = Node(elem_name="h1", value="     'hello!'")
        element = parser.parse(node)
        assert element == ("<h1>", "hello!", "</h1>")

        node = Node(elem_name="div", value=None, attr={"class": "my-class", "id": "my-id"})
        element = parser.parse(node)
        assert element == ("<div class='my-class' id='my-id'>", "</div>")

    def test_parse_elem(self):
        parser = Parser()

        result = parser.parse_elem('div(class="my-class", id="my-id")')
        expected = ("div", {"class": "my-class", "id": "my-id"})
        assert result == expected
