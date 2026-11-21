
package controller;

import model.Treap;
import view.TreapView;

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
}
