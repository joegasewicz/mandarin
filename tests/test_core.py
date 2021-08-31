import os

from citrine.core import Core
from citrine.elements import ELEMENTS


class TestCore:

    def test_get_template_path(self):
        core = Core(template_path="templates", elements=ELEMENTS)
        result = core.get_template_path("index.amber")
        assert result == os.path.abspath(".") + "/templates/index.amber"

    def test_get_template(self):
        core = Core(template_path="templates", elements=ELEMENTS)
        core.get_template("index.amber")
        expected = core.template_list
        assert expected == ["div.my-class:\n", '    h1 "hello!"\n']
