import os

from mandarin.core import Core
from mandarin.elements import ELEMENTS


class TestCore:

    def test_get_template_path(self):
        core = Core(template_path="templates", elements=ELEMENTS)
        result = core.get_template_path("index.mandarin")
        assert result == os.path.abspath(".") + "/templates/index.mandarin"

    def test_get_template(self):
        core = Core(template_path="templates", elements=ELEMENTS)
        core.get_template("index.mandarin")
        expected = core.template_list
        assert expected == ["div:\n", '    "hello"\n']
