from typing import Tuple, Union, Dict, Optional, Any
import re

from mandarin.core import ELEMENTS


class NodeHasNoValueError(Exception):
    pass


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def remove_white_space(value: str) -> str:
        cleaned_val = value.lstrip()
        # TODO handle escaped strings
        if cleaned_val[0] == "'":
            cleaned_val = cleaned_val.split("'")[1]
        else:
            cleaned_val = cleaned_val.split('"')[1]
        return cleaned_val

    @staticmethod
    def aggregate_into_tuple(*, elem_name: str, content: Any, attr_str: str):
        if not content and attr_str:
            return ("<%s %s>" % (elem_name, attr_str)), "</%s>" % elem_name
        elif content and attr_str:
            return ("<%s %s>" % (elem_name, attr_str)), Parser.remove_white_space(content), "</%s>" % elem_name
        elif content and not attr_str:
            return "<%s>" % elem_name, content, "</%s>" % elem_name
        else:
            return "<%s>" % elem_name, "</%s>" % elem_name

    def parse(self, node: "Node") -> Union[Tuple[str, str, str], Tuple[str, str], str]:
        el = node.elem_name
        attr_str = ""
        if node.elem_name:
            if node.attr:
                for k, v in node.attr.items():
                    if not attr_str:
                        # If this is the first attr then don't add white space
                        attr_str += f"{k}='{v}'"
                    else:
                        attr_str += f" {k}='{v}'"

            return Parser.aggregate_into_tuple(elem_name=el, content=node.value, attr_str=attr_str)
        elif node.value:
            return Parser.remove_white_space(node.value)
        else:
            raise NodeHasNoValueError("Node did not have any values to parse.")

    def add_attrs_to_elem(self):
        pass

    def parse_elem(self, element: str) -> Tuple[str, Optional[Dict[str, str]]]:
        elem = re.split("\(|\)", element)
        if len(elem) == 1:
            return elem, None
        attr_dict = {}
        attr_str = elem[1]
        attrs = attr_str.split(" ")
        for attr in attrs:
            attr_name, attr_val = attr.split("=")
            attr_dict[attr_name] = attr_val.strip('""')
        return elem[0], attr_dict
