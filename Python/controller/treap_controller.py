
from model.treap import Treap
from view.treap_view import TreapView


class TreapController:

    def __init__(self):
        self.tree = Treap()
        self.view = TreapView()

        # Construir el Treap inicial
        self.tree.build([
            (50, 100),
            (30, 80),
            (70, 90),
            (20, 50),
            (40, 60),
            (60, 70),
            (80, 75)
        ])

    # EJECUTAR PROGRAMA
    def run(self):

        while True:

            option = self.view.menu()

            try:

                # Mostrar arbol
                if option == "1":
                    self.view.show_tree(self.tree.root)
                    self.view.show_pairs(self.tree.inorder())

                # Insertar elemento
                elif option == "2":
                    key = self.view.ask_int("Ingrese la clave: ")
                    priority = self.view.ask_int("Ingrese prioridad: ")

                    self.tree.insert(key, priority)

                    self.view.show_message("Elemento insertado correctamente.")

                # Buscar elemento
                elif option == "3":
                    key = self.view.ask_int("Clave a buscar: ")

                    result = self.tree.search(key)

                    if result is not None:
                        self.view.show_message(
                            f"Elemento encontrado: {result.key} "
                            f"| Prioridad: {result.priority}"
                        )
                    else:
                        self.view.show_message("Elemento no encontrado.")

                # Eliminar elemento
                elif option == "4":
                    key = self.view.ask_int("Clave a eliminar: ")

                    if self.tree.delete(key):
                        self.view.show_message("Elemento eliminado correctamente.")
                    else:
                        self.view.show_message("Elemento no encontrado.")

                # Validar propiedades
                elif option == "5":
                    valid = self.tree.validate()

                    self.view.show_message(
                        f"Propiedades BST y Heap: {valid}"
                    )

                    self.view.show_message(
                        f"Altura del arbol: {self.tree.height()}"
                    )

                    self.view.show_pairs(self.tree.inorder())

                # Demostrar Split y Merge
                elif option == "6":
                    key = self.view.ask_int("Clave para dividir: ")

                    left, right = self.tree.split(key)

                    self.view.show_tree(
                        left.root,
                        "ARBOL IZQUIERDO (< clave)"
                    )

                    self.view.show_tree(
                        right.root,
                        "ARBOL DERECHO (>= clave)"
                    )

                    # Reconstruir el Treap
                    self.tree = left.merge(right)

                    self.view.show_tree(
                        self.tree.root,
                        "ARBOL RECONSTRUIDO CON MERGE"
                    )

                    self.view.show_message(
                        f"Propiedades correctas: {self.tree.validate()}"
                    )

                # Salir
                elif option == "0":
                    self.view.show_message("Finalizando programa.")
                    break

                else:
                    self.view.show_message("Opcion no valida.")

            except ValueError as error:
                self.view.show_message(f"Error: {error}")
