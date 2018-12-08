from abstract_day import AbstractDay


class Node:
    def __init__(self, header, children, metadata, value):
        self.header = header
        self.children = children
        self.metadata = metadata

        self.value = value

    def __repr__(self):
        return f"Node{self.header}|{len(self.children)}ch|{self.metadata}"


class Day08First(AbstractDay):

    def __init__(self, input_content):
        super().__init__(input_content)
        self.license_file = list(map(int, self.input_content.split()))
        self.nodes = list()

    def get_node(self, pos):
        header = tuple(self.license_file[pos:pos + 2])
        if header[0] == 0:
            children = list()
            metadata = self.license_file[pos + 2:pos + 2 + header[1]]
            node = Node(header, children, metadata, sum(metadata))
            pos += 2 + header[1]
        else:
            children = list()
            pos += 2
            for nb_child in range(header[0]):
                child, pos = self.get_node(pos)
                children.append(child)
            metadata = self.license_file[pos:pos + header[1]]
            value = sum(children[i-1].value for i in metadata if len(children) >= i)
            node = Node(header, children, metadata, value)
            pos += header[1]
        self.nodes.append(node)
        return node, pos

    def get_result(self):
        root, i = self.get_node(0)
        print("ROOT", root, i)
        return sum(iter(sum(node.metadata) for node in self.nodes))


class Day08Second(Day08First):

    def get_result(self):
        root, i = self.get_node(0)
        return root.value

