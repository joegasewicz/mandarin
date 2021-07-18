class Amber:
    """

    Abstract Syntax Tree
    """

    class TemplateResponse:
        pass

    def __init__(self, *, directory):
        self.directory = directory

    def render(self, *, template=None, status=None, data=None):
        return b"<div>Amber Template Engine</div>"
