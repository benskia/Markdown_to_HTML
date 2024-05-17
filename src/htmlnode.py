class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented for this object")

    def props_to_html(self):
        if self.props == None:
            return ""
        presented_props = [f'{k}="{v}"' for k, v in self.props.items()]
        return " ".join(presented_props)

    def __repr__(self):
        return f"""Tag: {self.tag}\n
                Value: {self.value}\n
                Children: {self.children}\n
                Props: {self.props}"""


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("This LeafNode has no value.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("This ParentNode has no tag.")
        if self.children == None:
            raise ValueError("This ParentNode has no children.")
        child_node_values = ""
        for child_node in self.children:
            child_node_values += child_node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_node_values}</{self.tag}>"
