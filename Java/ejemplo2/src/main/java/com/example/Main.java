
package com.example;

import com.example.controller.TreapController;
import com.example.model.Treap;
import com.example.view.TreapView;

public class Main {

    public static void main(String[] args) {

        Treap modelo = new Treap();

        TreapView vista = new TreapView();

        TreapController controlador =
                new TreapController(modelo, vista);

        System.out.println("ARBOL INICIAL:");
        controlador.mostrar();

        System.out.println("\nINSERTANDO NODO 20...");

        controlador.insertar(20, 10);
    }
}
