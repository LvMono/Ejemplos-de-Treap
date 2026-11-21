package com.example.model;

public class Node {

    public int key;
    public int priority;

    public Node left;
    public Node right;

    public Node(int key, int priority) {
        this.key = key;
        this.priority = priority;
        this.left = null;
        this.right = null;
    }
}
