import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

// Klasa abstrakcyjna Figura
abstract class Figura {
    protected String nazwa;
    protected double pole;
    protected double obwod;

    public Figura(String nazwa, double pole, double obwod) {
        this.nazwa = nazwa;
        this.pole = pole;
        this.obwod = obwod;
    }

    public String getNazwa() {
        return nazwa;
    }

    public void setNazwa(String nazwa) {
        this.nazwa = nazwa;
    }

    public double getPole() {
        return pole;
    }

    public void setPole(double pole) {
        this.pole = pole;
    }

    public double getObwod() {
        return obwod;
    }

    public void setObwod(double obwod) {
        this.obwod = obwod;
    }

    // Metoda toString() zwracająca informacje o figurze
    public String toString() {
        return nazwa + ": pole = " + pole + ", obwod = " + obwod;
    }
}

// Klasa Okrąg dziedzicząca po klasie Figura
class Okrag extends Figura {
    protected double promien;

    public Okrag(String nazwa, double pole, double obwod, double promien) {
        super(nazwa, pole, obwod);
        this.promien = promien;
    }

    public double getPromien() {
        return promien;
    }

    public void setPromien(double promien) {
        this.promien = promien;
    }

    // Przesłonięcie metody toString() z klasy Figura
    public String toString() {
        return super.toString() + ", promień = " + promien;
    }
}

// Klasa Trójkąt dziedzicząca po klasie Figura
class Trojkat extends Figura {
    protected double a;
    protected double b;
    protected double c;

    public Trojkat(String nazwa, double pole, double obwod, double a, double b, double c) {
        super(nazwa, pole, obwod);
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }

    public double getB() {
        return b;
    }

    public void setB(double b) {
        this.b = b;
    }

    public double getC() {
        return c;
    }

    public void setC(double c) {
        this.c = c;
    }

    // Przesłonięcie metody toString() z klasy Figura
    public String toString() {
        return super.toString() + ", a = " + a + ", b = " + b + ", c = " + c;
    }
}

// Klasa abstrakcyjna FiguraEditor dziedzicząca po klasie JComponent
abstract class FiguraEditor extends JComponent {
    // Deklaracja metody abstrakcyjnej updateFigura()
    abstract public void updateFigura();
}

// Klasa OkragEditor dziedzicząca po klasie FiguraEditor
class OkragEditor extends FiguraEditor {
    private Okrag okrag;
    private JTextField nazwaTextField;
    private JTextField promienTextField;
    public OkragEditor(Okrag okrag) {
        this.okrag = okrag;

        // Utworzenie etykiet i pól tekstowych
        JLabel nazwaLabel = new JLabel("Nazwa:");
        nazwaTextField = new JTextField(okrag.getNazwa());
        JLabel promienLabel = new JLabel("Promień:");
        promienTextField = new JTextField(Double.toString(okrag.getPromien()));

        // Utworzenie przycisku "Zapisz"
        JButton zapiszButton = new JButton("Zapisz");

        // Ustawienie rozmiaru i layoutu panelu
        setPreferredSize(new Dimension(250, 100));
        setLayout(new GridLayout(3, 2));

        // Dodanie komponentów do panelu
        add(nazwaLabel);
        add(nazwaTextField);
        add(promienLabel);
        add(promienTextField);
        add(new JPanel());
        add(zapiszButton);

        // Dodanie ActionListenera do przycisku "Zapisz"
        zapiszButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                updateFigura();
            }
        });
    }

    // Implementacja metody updateFigura() z klasy FiguraEditor
    public void updateFigura() {
        try {
            // Parsowanie wartości z pól tekstowych
            double promien = Double.parseDouble(promienTextField.getText());

            // Aktualizacja pól obiektu okrąg
            okrag.setNazwa(nazwaTextField.getText());
            okrag.setPromien(promien);
            okrag.setPole(Math.PI * promien * promien);
            okrag.setObwod(2 * Math.PI * promien);

            // Wyświetlenie komunikatu o pomyślnym zapisaniu zmian
            JOptionPane.showMessageDialog(null, "Zmiany zostały zapisane.");
        } catch (NumberFormatException ex) {
            // Wyświetlenie komunikatu o błędnych danych
            JOptionPane.showMessageDialog(null, "Nieprawidłowe dane.", "Błąd", JOptionPane.ERROR_MESSAGE);
        }
    }
}

class TrojkatEditor extends FiguraEditor {
    private Trojkat trojkat;
    private JTextField nazwaTextField;
    private JTextField aTextField;
    private JTextField bTextField;
    private JTextField cTextField;

    public TrojkatEditor(Trojkat trojkat) {
        this.trojkat = trojkat;

        // Utworzenie etykiet i pól tekstowych
        JLabel nazwaLabel = new JLabel("Nazwa:");
        nazwaTextField = new JTextField(trojkat.getNazwa());
        JLabel aLabel = new JLabel("Bok a:");
        aTextField = new JTextField(Double.toString(trojkat.getA()));
        JLabel bLabel = new JLabel("Bok b:");
        bTextField = new JTextField(Double.toString(trojkat.getB()));
        JLabel cLabel = new JLabel("Bok c:");
        cTextField = new JTextField(Double.toString(trojkat.getC()));

        // Utworzenie przycisku "Zapisz"
        JButton zapiszButton = new JButton("Zapisz");

        // Ustawienie rozmiaru i layoutu panelu
        setPreferredSize(new Dimension(250, 150));
        setLayout(new GridLayout(5, 2));

        // Dodanie komponentów do panelu
        add(nazwaLabel);
        add(nazwaTextField);
        add(aLabel);
        add(aTextField);
        add(bLabel);
        add(bTextField);
        add(cLabel);
        add(cTextField);
        add(new JPanel());
        add(zapiszButton);

        // Dodanie ActionListenera do przycisku "Zapisz"
        zapiszButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                updateFigura();
            }
        });
    }

    // Implementacja metody updateFigura() z klasy FiguraEditor
    public void updateFigura() {
        try {
            // Parsowanie wartości z pól tekstowych
            double a = Double.parseDouble(aTextField.getText());
            double b = Double.parseDouble(bTextField.getText());
            double c = Double.parseDouble(cTextField.getText());

            // Sprawdzenie warunku trójkąta
            if ((a + b > c) && (a + c > b) && (b + c > a)) {
                // Aktualizacja pól obiektu trójkąt
                trojkat.setNazwa(nazwaTextField.getText());
                trojkat.setA(a);
                trojkat.setB(b);
                trojkat.setC(c);
                double p = (a + b + c) / 2;
                trojkat.setPole(Math.sqrt(p * (p - a) * (p - b) * (p - c)));
                trojkat.setObwod(a + b + c);

                // Wyświetlenie komunikatu o pomyślnym zapisaniu zmian
                JOptionPane.showMessageDialog(null, "Zmiany zostały zapisane.");
            } else {
                // Wyświetlenie komunikatu o błędnych danych
                JOptionPane.showMessageDialog(null, "Nieprawidłowe długości boków trójkąta.", "Błąd",
                        JOptionPane.ERROR_MESSAGE);
            }
        } catch (NumberFormatException ex) {
            // Wyświetlenie komunikatu o błędnych danych
            JOptionPane.showMessageDialog(null, "Nieprawidłowe dane.", "Błąd", JOptionPane.ERROR_MESSAGE);
        }
    }
}

// Klasa Main
public class Main {
    public static void main(String[] args) {
        // Utworzenie obiektów figur i edytorów
        Okrag okrag = new Okrag("Okrag", 5);
        OkragEditor okragEditor = new OkragEditor(okrag);
        Trojkat trojkat = new Trojkat("Trojkat", 3, 4, 5);
        TrojkatEditor trojkatEditor = new TrojkatEditor(trojkat);

            // Utworzenie okna głównego
        JFrame frame = new JFrame("Figury");

        // Ustawienie rozmiaru i layoutu okna głównego
        frame.setSize(300, 300);
        frame.setLayout(new GridLayout(2, 1));

        // Dodanie edytorów do okna głównego
        frame.add(okragEditor);
        frame.add(trojkatEditor);

        // Ustawienie widoczności okna głównego
        frame.setVisible(true);
    }
}

