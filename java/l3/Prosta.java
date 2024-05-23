package figury;

public class Prosta {
    public final double a;
    public final double b;
    public final double c;

    public Prosta(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public static boolean czyRownolegle(Prosta p1, Prosta p2) {
        return p1.a * p2.b == p1.b * p2.a;
    }

    public static boolean czyProstopadle(Prosta p1, Prosta p2) {
        return p1.a * p2.a + p1.b * p2.b == 0;
    }

    public static Punkt punktPrzeciecia(Prosta p1, Prosta p2) {
        if (czyRownolegle(p1, p2)) {
            throw new IllegalArgumentException("Proste są równoległe, nie mają punktu przecięcia.");
        }
        double wyznacznik = p1.a * p2.b - p2.a * p1.b;
        double x = (p2.c * p1.b - p1.c * p2.b) / wyznacznik;
        double y = (p1.c * p2.a - p2.c * p1.a) / wyznacznik;
        return new Punkt(x, y);
    }

    public Prosta przesun(Wektor v) {
        return new Prosta(this.a, this.b, this.c - (this.a * v.dx + this.b * v.dy));
    }
}

