from model.node import Node
class Treap:

    def __init__(self):
        self.root = None

    # ROTACION DERECHA
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    # ROTACION IZQUIERDA
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    # INSERCION
    def _insert(self, root, key, priority):

        if root is None:
            return Node(key, priority)

        if key < root.key:

            root.left = self._insert(
                root.left, key, priority
            )

            if root.left.priority > root.priority:
                root = self.rotate_right(root)

        elif key > root.key:

            root.right = self._insert(
                root.right, key, priority
            )

            if root.right.priority > root.priority:
                root = self.rotate_left(root)

        else:
            raise ValueError("La clave ya existe")

        return root

    def insert(self, key, priority):
        self.root = self._insert(
            self.root, key, priority
        )

    # CONSTRUCCION A PARTIR DE PARES
    def build(self, pairs):
        self.root = None

        for key, priority in pairs:
            self.insert(key, priority)

    # BUSQUEDA
    def search(self, key):

        current = self.root

        while current is not None:

            if key < current.key:
                current = current.left

            elif key > current.key:
                current = current.right

            else:
                return current

        return None

    # MERGE INTERNO
    def _merge(self, left, right):

        if left is None:
            return right

        if right is None:
            return left

        if left.priority > right.priority:

            left.right = self._merge(
                left.right, right
            )

            return left

        else:

            right.left = self._merge(
                left, right.left
            )

            return right

    # ELIMINACION
    def _delete(self, root, key):

        if root is None:
            return None

        if key < root.key:

            root.left = self._delete(
                root.left, key
            )

        elif key > root.key:

            root.right = self._delete(
                root.right, key
            )

        else:
            return self._merge(
                root.left, root.right
            )

        return root

    def delete(self, key):

        if self.search(key) is None:
            return False

        self.root = self._delete(
            self.root, key
        )

        return True

    # SPLIT
    def _split(self, root, key):

        if root is None:
            return None, None

        if root.key < key:

            root.right, right = self._split(
                root.right, key
            )

            return root, right

        else:

            left, root.left = self._split(
                root.left, key
            )

            return left, root

    def split(self, key):

        left_root, right_root = self._split(
            self.root, key
        )

        left_tree = Treap()
        right_tree = Treap()

        left_tree.root = left_root
        right_tree.root = right_root

        self.root = None

        return left_tree, right_tree

    # MERGE PUBLICO
    def merge(self, other):

        result = Treap()

        result.root = self._merge(
            self.root, other.root
        )

        self.root = None
        other.root = None

        return result

    # RECORRIDO INORDEN
    def inorder(self):

        result = []

        def traverse(node):

            if node is None:
                return

            traverse(node.left)

            result.append(
                (node.key, node.priority)
            )

            traverse(node.right)

        traverse(self.root)

        return result

    # ALTURA DEL ARBOL
    def height(self):

        def calculate(node):

            if node is None:
                return 0

            return 1 + max(
                calculate(node.left),
                calculate(node.right)
            )

        return calculate(self.root)

    # VALIDACION DE PROPIEDADES
    def validate(self):

        pairs = self.inorder()

        # Verificar propiedad BST
        for i in range(1, len(pairs)):

            if not pairs[i - 1][0] < pairs[i][0]:
                return False

        # Verificar propiedad Heap
        def check_heap(node):

            if node is None:
                return True

            if node.left:
                if node.left.priority > node.priority:
                    return False

            if node.right:
                if node.right.priority > node.priority:
                    return False

            return (
                check_heap(node.left)
                and check_heap(node.right)
            )

        return check_heap(self.root)
