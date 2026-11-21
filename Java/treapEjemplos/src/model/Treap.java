
package model;

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
}
