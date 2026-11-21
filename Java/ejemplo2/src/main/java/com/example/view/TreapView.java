
package com.example.view;

import com.example.model.Node;

public class TreapView {

    public void mostrarTreap(Node root) {

        System.out.println("\n===== ESTRUCTURA DEL TREAP =====");

        mostrarRecursivo(root, "", "Raiz");
    }

    private void mostrarRecursivo(
            Node nodo, String espacio, String posicion) {

        if (nodo == null) {
            return;
        }

        System.out.println(
                espacio + posicion + ": "
                + nodo.key + " (Prioridad: "
                + nodo.priority + ")"
        );

        mostrarRecursivo(
                nodo.left, espacio + "   ", "Izquierdo");

        mostrarRecursivo(
                nodo.right, espacio + "   ", "Derecho");
    }
}
