class Node():
    def __init__(self):
        self._parent = None
        self._children = []

    @property
    def parent(self):
        return self._parent

    # Handle children
    def add_child(self, child):
        child._parent = self
        self._children.append(child)

    def remove_child(self, child):
        try:
            self._children.remove(child)
        except:
            pass