
class TreapView:

    # MENU PRINCIPAL
    def menu(self):
        print("\n========== TREAP ==========")
        print("1. Mostrar arbol")
        print("2. Insertar elemento")
        print("3. Buscar elemento")
        print("4. Eliminar elemento")
        print("5. Validar propiedades")
        print("6. Demostrar Split y Merge")
        print("0. Salir")
        print("===========================")

        return input("Seleccione una opcion: ")

    # SOLICITAR DATOS
    def ask_int(self, message):
        return int(input(message))

    # MOSTRAR ARBOL
    def show_tree(self, root, title="TREAP"):
        print("\n========== " + title + " ==========")

        if root is None:
            print("Arbol vacio")
            return

        self._print_tree(root, 0)

    def _print_tree(self, node, level):

        if node is None:
            return

        # Mostrar primero el hijo derecho
        self._print_tree(node.right, level + 1)

        print(
            "   " * level +
            f"{node.key} (P:{node.priority})"
        )

        # Mostrar despues el hijo izquierdo
        self._print_tree(node.left, level + 1)

    # MOSTRAR MENSAJES
    def show_message(self, message):
        print("\n" + message)

    # MOSTRAR RECORRIDO
    def show_pairs(self, pairs):
        print("\n========== RECORRIDO INORDEN ==========")

        for key, priority in pairs:
            print(f"Clave: {key} | Prioridad: {priority}")
