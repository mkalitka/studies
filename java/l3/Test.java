import figury.*;

public class Test {
    public static void main(String[] args) {
        testPunkt();
        testOdcinek();
        testTrojkat();
        testWektor();
        testProsta();
    }

    public static void testPunkt() {
        System.out.println("=== Testowanie klasy Punkt ===");

        Punkt p1 = new Punkt(1, 2);
        Punkt p2 = new Punkt(3, 4);
        Wektor v = new Wektor(2, 3);
        Prosta prosta = new Prosta(1, -1, 0);

        Punkt pPrzesuniety = p1.przesun(v);
        System.out.println("Punkt <1, 2> przesunięty o wektor [2, 3]: <" + pPrzesuniety.getX() + ", " + pPrzesuniety.getY() + ">");

        Punkt pObrocony = p1.obroc(p2, 90);
        System.out.println("Punkt <1, 2> obrócony o 90 stopni wokół punktu <3, 4>: <" + pObrocony.getX() + ", " + pObrocony.getY() + ">");

        Punkt pOdbity = p1.odbij(prosta);
        System.out.println("Punkt <1, 2> odbity względem prostej x = y: <" + pOdbity.getX() + ", " + pOdbity.getY() + ">");
    }

    public static void testOdcinek() {
        System.out.println("=== Testowanie klasy Odcinek ===");

        Punkt p1 = new Punkt(1, 0);
        Punkt p2 = new Punkt(4, 3);
        Wektor v = new Wektor(1, 2);
        Prosta prosta = new Prosta(1, 0, -2);

        Odcinek odcinek = new Odcinek(p1, p2);

        Odcinek przesunietyOdcinek = odcinek.przesun(v);
        System.out.println("Odcinek (<1, 0>, <4, 3>) przesunięty o wektor [1, 2]: <" + przesunietyOdcinek.getP1().getX() + ", " + przesunietyOdcinek.getP1().getY() + 
                           ">, <" + przesunietyOdcinek.getP2().getX() + ", " + przesunietyOdcinek.getP2().getY() + ">");

        Odcinek obroconyOdcinek = odcinek.obroc(new Punkt(2, 0), 90);
        System.out.println("Odcinek (<1, 0>, <4, 3>) obrócony o 90 stopni wokół punktu <2, 0>: <" + obroconyOdcinek.getP1().getX() + ", " + obroconyOdcinek.getP1().getY() +
                           ">, <" + obroconyOdcinek.getP2().getX() + ", " + obroconyOdcinek.getP2().getY() + ">");

        Odcinek odbityOdcinek = odcinek.odbij(prosta);
        System.out.println("Odcinek (<1, 0>, <4, 3>) odbity względem prostej x = 2: <" + odbityOdcinek.getP1().getX() + ", " + odbityOdcinek.getP1().getY() +
                           ">, <" + odbityOdcinek.getP2().getX() + ", " + odbityOdcinek.getP2().getY() + ">");

        System.out.println("Test odcinka (<0, 0>, <0, 0>):");
        Punkt p3 = new Punkt(0, 0);
        Punkt p4 = new Punkt(0, 0);
        try {
            Odcinek odcinek2 = new Odcinek(p3, p4);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void testTrojkat() {
        System.out.println("=== Testowanie klasy Trojkat ===");

        Punkt p1 = new Punkt(0, 0);
        Punkt p2 = new Punkt(4, 1);
        Punkt p3 = new Punkt(2, 3);
        Wektor v = new Wektor(1, 1);
        Prosta prosta = new Prosta(0, 1, -1);

        Trojkat trojkat = new Trojkat(p1, p2, p3);

        Trojkat przesunietyTrojkat = trojkat.przesun(v);
        System.out.println("Trójkąt (<0, 0>, <4, 1>, <2, 3>) przesunięty o wektor [1, 1]: <" + przesunietyTrojkat.getP1().getX() + ", " + przesunietyTrojkat.getP1().getY() + 
                           ">, <" + przesunietyTrojkat.getP2().getX() + ", " + przesunietyTrojkat.getP2().getY() + 
                           ">, <" + przesunietyTrojkat.getP3().getX() + ", " + przesunietyTrojkat.getP3().getY() + ">");

        Trojkat obroconyTrojkat = trojkat.obroc(new Punkt(1, 4), 90);
        System.out.println("Trójkąt (<0, 0>, <4, 1>, <2, 3>) obrócony o 90 stopni wokół punktu <1, 4>: <" + obroconyTrojkat.getP1().getX() + ", " + obroconyTrojkat.getP1().getY() + 
                           ">, <" + obroconyTrojkat.getP2().getX() + ", " + obroconyTrojkat.getP2().getY() + 
                           ">, <" + obroconyTrojkat.getP3().getX() + ", " + obroconyTrojkat.getP3().getY() + ">");

        Trojkat odbityTrojkat = trojkat.odbij(prosta);
        System.out.println("Trójkąt (<0, 0>, <4, 1>, <2, 3>) odbity względem prostej y = 1: <" + odbityTrojkat.getP1().getX() + ", " + odbityTrojkat.getP1().getY() + 
                           ">, <" + odbityTrojkat.getP2().getX() + ", " + odbityTrojkat.getP2().getY() + 
                           ">, <" + odbityTrojkat.getP3().getX() + ", " + odbityTrojkat.getP3().getY() + ">");

        System.out.println("Test trójkąta (<0, 0>, <1, 1>, <3, 3>):");
        Punkt p4 = new Punkt(0, 0);
        Punkt p5 = new Punkt(1, 1);
        Punkt p6 = new Punkt(3, 3);
        try {
            Trojkat trojkat2 = new Trojkat(p4, p5, p6);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void testWektor() {
        System.out.println("=== Testowanie klasy Wektor ===");

        Wektor v1 = new Wektor(1, 2);
        Wektor v2 = new Wektor(3, 4);

        Wektor zlozonyWektor = Wektor.zloz(v1, v2);
        System.out.println("Złożone wektory (1, 2) i (3, 4): (" + zlozonyWektor.dx + ", " + zlozonyWektor.dy + ")");
    }

    public static void testProsta() {
        System.out.println("=== Testowanie klasy Prosta ===");

        Prosta p1 = new Prosta(1, -1, 0);
        Prosta p2 = new Prosta(1, 1, -4);
        Prosta p3 = new Prosta(2, -2, 4);
        Wektor v = new Wektor(2, 3);

        Prosta przesunietaProsta = p1.przesun(v);
        System.out.println("Prosta x=y przesunięta o wektor (2, 3): " + przesunietaProsta.a + "x + " + przesunietaProsta.b + "y + " + przesunietaProsta.c + " = 0");

        boolean czyRownolegle = Prosta.czyRownolegle(p1, new Prosta(2, -2, 5));
        System.out.println("Czy proste x=y i 2x=2y+5 są równoległe? " + (czyRownolegle ? "Tak" : "Nie"));

        boolean czyProstopadle = Prosta.czyProstopadle(p1, new Prosta(1, 2, 0)); // x=y oraz x=-y są prostopadłe
        System.out.println("Czy proste x=y i x+2y=0 są prostopadłe? " + (czyProstopadle ? "Tak" : "Nie"));

        Punkt punktPrzeciecia = null;
        try {
            punktPrzeciecia = Prosta.punktPrzeciecia(p1, p2);
        } catch (IllegalArgumentException e) {}
        System.out.println("Punkt przecięcia się prostych x=y i x+y=4: <" + (punktPrzeciecia != null ? (punktPrzeciecia.getX() + ", " + punktPrzeciecia.getY()) : "null") + ">");

        Punkt punktPrzeciecia2 = null;
        try {
            punktPrzeciecia2 = Prosta.punktPrzeciecia(p1, p3);
        } catch (IllegalArgumentException e) {}
        System.out.println("Punkt przecięcia się prostych x=y i 2x-2y=4: <" + (punktPrzeciecia2 != null ? (punktPrzeciecia2.getX() + ", " + punktPrzeciecia2.getY()) : "null") + ">");
            
    }
}

