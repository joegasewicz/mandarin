from typing import Tuple, Union

from citrine.ast import Node, ELEMENTS


class NodeHasNoValueError(Exception):
    pass


class Parser:

    def __init__(self):
        pass

    def parse(self, node: Node) -> Union[Tuple[str, str], str]:
        if node.elem_name:
            for el in ELEMENTS:
                if el == node.elem_name:
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
