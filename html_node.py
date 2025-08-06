

class HtmlNode:

    def __init__(self, name, span):
        self.name = name
        self.span = span
        self.l = HtmlNode
        self.r = HtmlNode
