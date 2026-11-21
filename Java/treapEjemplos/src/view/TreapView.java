
package view;

import model.Node;

public class TreapView {

    public void mostrarTreap(Node root) {

        System.out.println("===== TREAP =====");

        System.out.println("Raiz: " + root.getKey());

        System.out.println("Hijo izquierdo: "
                + root.getLeft().getKey());

        System.out.println("Hijo derecho: "
                + root.getRight().getKey());

        System.out.println("\nPrioridades:");

        System.out.println("Raiz: "
                + root.getPriority());

        System.out.println("Izquierdo: "
                + root.getLeft().getPriority());

        System.out.println("Derecho: "
                + root.getRight().getPriority());
    }
}
