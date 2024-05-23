package figury;

public class Punkt {
    private final double x;
    private final double y;

    public Punkt(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Punkt przesun(Wektor v) {
        return new Punkt(this.x + v.dx, this.y + v.dy);
    }

    public Punkt obroc(Punkt p, double kat) {
        double radiany = Math.toRadians(kat);
        double sin = Math.sin(radiany);
        double cos = Math.cos(radiany);
        double dx = this.x - p.x;
        double dy = this.y - p.y;

        double noweX = cos * dx - sin * dy + p.x;
        double noweY = sin * dx + cos * dy + p.y;

        return new Punkt(noweX, noweY);
    }

    public Punkt odbij(Prosta p) {
        double d = (p.a * this.x + p.b * this.y + p.c) / (p.a * p.a + p.b * p.b);
        double noweX = this.x - 2 * p.a * d;
        double noweY = this.y - 2 * p.b * d;

        return new Punkt(noweX, noweY);
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }
}
