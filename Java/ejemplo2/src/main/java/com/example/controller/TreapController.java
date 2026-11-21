
package com.example.controller;

import com.example.model.Treap;
import com.example.view.TreapView;

public class TreapController {

    private Treap model;
    private TreapView view;

    public TreapController(Treap model, TreapView view) {
        this.model = model;
        this.view = view;
    }

    public void mostrar() {
        view.mostrarTreap(model.getRoot());
    }

    public void insertar(int key, int priority) {

        model.insertar(key, priority);

        mostrar();
    }
}
