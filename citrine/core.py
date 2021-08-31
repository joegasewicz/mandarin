import os
from typing import List

from citrine.elements import ELEMENTS


TEMPLATE_PATH = "templates"


class Core:

    _template_list: List[str] = []

    template_path: str

    def __init__(self, *args, **kwargs):
        self.template_path = kwargs["template_path"]
        self.elements = kwargs["elements"]

    @property
    def template_list(self) -> List[str]:
        """
        :return:
        """
        return self._template_list

    def get_template_path(self, template_name: str) -> str:
        """
        :param template_name:
        :return:
        """
        abs_path = os.path.abspath(self.template_path)
        return abs_path + f"/{template_name}"

    def get_template(self, template_name: str) -> None:
        """
        :param template_name:
        :return:
        """
        with open(self.get_template_path(template_name), "r") as reader:
            for line in reader:
                self.template_list.append(line)
