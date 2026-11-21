
import model.Treap;
import view.TreapView;
import controller.TreapController;

public class Main {

    public static void main(String[] args) {

        Treap modelo = new Treap();

        TreapView vista = new TreapView();

        TreapController controlador =
                new TreapController(modelo, vista);

        controlador.mostrar();
    }
}
