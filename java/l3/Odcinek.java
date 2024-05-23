package figury;

public class Odcinek {
    private final Punkt p1;
    private final Punkt p2;

    public Odcinek(Punkt p1, Punkt p2) {
        if (p1.getX() == p2.getX() && p1.getY() == p2.getY()) {
            throw new IllegalArgumentException("Punkty p1 i p2 muszą być różne.");
        }
        this.p1 = p1;
        this.p2 = p2;
    }

    public Odcinek przesun(Wektor v) {
        return new Odcinek(p1.przesun(v), p2.przesun(v));
    }

    public Odcinek obroc(Punkt p, double kat) {
        return new Odcinek(p1.obroc(p, kat), p2.obroc(p, kat));
    }

    public Odcinek odbij(Prosta p) {
        return new Odcinek(p1.odbij(p), p2.odbij(p));
    }

    public Punkt getP1() {
        return p1;
    }

    public Punkt getP2() {
        return p2;
    }
}
