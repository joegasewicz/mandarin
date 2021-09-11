from typing import Tuple, Union, Dict, Optional
import re

from mandarin.core import ELEMENTS


class NodeHasNoValueError(Exception):
    pass


class Parser:

    def __init__(self):
        pass

    def parse(self, node: "Node") -> Union[Tuple[str, str], str]:
        if node.elem_name:
            for el in ELEMENTS:
                if el == node.elem_name:
                    attr_str = ""
                    if node.attr:
                        for k, v in node.attr.items():
                            if not attr_str:
                                # If this is the first attr then don't add white space
                                attr_str += f"{k}='{v}'"
                            else:
                                attr_str += f" {k}='{v}'"
                    if attr_str:
                        # white space added to first attr
                        return ("<%s %s>" % (el, attr_str)), ("</%s>" % el)
                    return "<%s>" % el, "</%s>" % el
        elif node.value:
            # handle logic
            # Remove leading spaces from value
            cleaned_val = node.value.lstrip()
            # TODO handle escaped strings
            if cleaned_val[0] == "'":
                cleaned_val = cleaned_val.split("'")[1]
            else:
                cleaned_val = cleaned_val.split('"')[1]
            return cleaned_val
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
        attrs = attr_str.split(", ")
        for attr in attrs:
            attr_name, attr_val = attr.split("=")
            attr_dict[attr_name] = attr_val.strip('""')
        return elem[0], attr_dict
