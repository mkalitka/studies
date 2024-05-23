package figury;

public class Trojkat {
    private final Punkt p1;
    private final Punkt p2;
    private final Punkt p3;

    public Trojkat(Punkt p1, Punkt p2, Punkt p3) {
        if (czyWspolliniowe(p1, p2, p3)) {
            throw new IllegalArgumentException("Punkty muszą być niewspółliniowe.");
        }
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }

    private boolean czyWspolliniowe(Punkt p1, Punkt p2, Punkt p3) {
        return (p2.getY() - p1.getY()) * (p3.getX() - p1.getX()) == 
               (p3.getY() - p1.getY()) * (p2.getX() - p1.getX());
    }

    public Trojkat przesun(Wektor v) {
        return new Trojkat(p1.przesun(v), p2.przesun(v), p3.przesun(v));
    }

    public Trojkat obroc(Punkt p, double kat) {
        return new Trojkat(p1.obroc(p, kat), p2.obroc(p, kat), p3.obroc(p, kat));
    }

    public Trojkat odbij(Prosta p) {
        return new Trojkat(p1.odbij(p), p2.odbij(p), p3.odbij(p));
    }

    public Punkt getP1() {
        return p1;
    }

    public Punkt getP2() {
        return p2;
    }

    public Punkt getP3() {
        return p3;
    }
}

