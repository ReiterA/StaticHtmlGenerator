class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html():
        raise NotImplementedError("to_html method must be implemented by subclasses")

    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        return " " + ' '.join(f'{key}="{value}"' for key, value in self.props.items())