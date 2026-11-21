package com.example.model;

public class Treap {

    private Node root;

    public Treap() {
        root = new Node(50, 40);

        root.left = new Node(30, 50);
        root.right = new Node(70, 60);
    }

    public Node getRoot() {
        return root;
    }

    // Metodo para insertar un nuevo nodo
    public void insertar(int key, int priority) {
        root = insertarRecursivo(root, key, priority);
    }

    private Node insertarRecursivo(
            Node actual, int key, int priority) {

        if (actual == null) {
            return new Node(key, priority);
        }

        if (key < actual.key) {

            actual.left = insertarRecursivo(
                    actual.left, key, priority);

            if (actual.left.priority < actual.priority) {
                actual = rotarDerecha(actual);
            }

        } else if (key > actual.key) {

            actual.right = insertarRecursivo(
                    actual.right, key, priority);

            if (actual.right.priority < actual.priority) {
                actual = rotarIzquierda(actual);
            }
        }

        return actual;
    }

    // Rotacion hacia la derecha
    private Node rotarDerecha(Node padre) {

        Node nuevoPadre = padre.left;
        padre.left = nuevoPadre.right;
        nuevoPadre.right = padre;

        return nuevoPadre;
    }

    // Rotacion hacia la izquierda
    private Node rotarIzquierda(Node padre) {

        Node nuevoPadre = padre.right;
        padre.right = nuevoPadre.left;
        nuevoPadre.left = padre;

        return nuevoPadre;
    }
}
