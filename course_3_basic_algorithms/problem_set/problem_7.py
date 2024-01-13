
class RouteTrie:
    def __init__(self, root_path):
        self.root = RouteTrieNode(root_path)

    def insert(self, list_path, handler):
        node = self.root
        for path in list_path:
            if node.children.get(path):
                node = node.children[path]
            else:
                node.insert(path)
                node = node.children[path]
        node.handler = handler

    def find(self, list_path):
        if len(list_path) == 1 and list_path[0] == '':
            return self.root.handler
        node = self.root
        for path in list_path:
            if node.children.get(path) is None:
                return 'not found handler'
            node = node.children[path]
        return node.handler


class RouteTrieNode:
    def __init__(self, path="not found handler"):
        self.children = {}
        self.handler = path

    def insert(self, path_part):
        self.children[path_part] = RouteTrieNode()

# The Router class will wrap the Trie and handle


class Router:
    def __init__(self, root_path='root handler'):
        self.routes = RouteTrie(root_path)

    def add_handler(self, path, handler):
        path = self.split_path(path)
        self.routes.insert(path, handler)

    def lookup(self, path):
        path = self.split_path(path)
        return self.routes.find(path)

    def split_path(self, path):
        path = path.strip('/')
        path = path.split('/')
        return path


if __name__ == '__main__':
    router = Router("root handler")
    router.add_handler("/home/about", "about handler")
    print(router.lookup("/"))
    print(router.lookup("/home"))
    print(router.lookup("/home/about"))
    print(router.lookup("/home/about/"))
    print(router.lookup("/home/about/me"))
