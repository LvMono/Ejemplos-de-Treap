
package model;

public class Node {

    int key;
    int priority;

    Node left;
    Node right;

    public Node(int key, int priority) {
        this.key = key;
        this.priority = priority;
        this.left = null;
        this.right = null;
    }

    public int getKey() {
        return key;
    }

    public int getPriority() {
        return priority;
    }

    public Node getLeft() {
        return left;
    }

    public Node getRight() {
        return right;
    }
}
