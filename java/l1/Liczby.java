public class Liczby {

    static String[] jednosci = {
        "", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem",
        "osiem", "dziewięć"
    };

    static String[] nastki = {
        "dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście",
        "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"
    };

    static String[] dziesiatki = {
        "", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt",
        "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"
    };

    static String[] setki = {
        "", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset",
        "siedemset", "osiemset", "dziewięćset"
    };

    static String[] tysiace = {
        "", "tysiąc", "tysiące", "tysięcy"
    };

    static String[] miliony = {
        "", "milion", "miliony", "milionów"
    };

    static String[] miliardy = {
        "", "miliard", "miliardy", "miliardów"
    };


    public static void main(String[] args) {
        for (String arg : args) {
            try {
                int liczba = Integer.parseInt(arg);
                System.out.println(konwertujNaSlowa(liczba));
            } catch (NumberFormatException e) {
                System.out.println("Argument " + arg + " nie jest liczbą całkowitą");
                continue;
            }
        }
    };


    public static String konwertujNaSlowa(int liczba) {
        if (liczba == 0) {
            return "zero";
        }
        String wynik = "";
        if (liczba < 0) {
            wynik += "minus ";
            liczba = -liczba;
        }
        int miliardy = liczba / 1000000000;
        int miliony = (liczba - miliardy * 1000000000) / 1000000;
        int tysiace = (liczba - miliardy * 1000000000 - miliony * 1000000) / 1000;
        int reszta = liczba - miliardy * 1000000000 - miliony * 1000000 - tysiace * 1000;
        if (miliardy > 0) {
            if (miliardy > 1) {
                wynik += konwertujLiczbe(miliardy) + " ";
            }
            wynik += Liczby.miliardy[odmiana(miliardy)] + " ";
        }
        if (miliony > 0) {
            if (miliony > 1) {
                wynik += konwertujLiczbe(miliony) + " ";
            }
            wynik += Liczby.miliony[odmiana(miliony)] + " ";
        }
        if (tysiace > 0) {
            if (tysiace > 1) {
                wynik += konwertujLiczbe(tysiace) + " ";
            }
            wynik += Liczby.tysiace[odmiana(tysiace)] + " ";
        }
        if (reszta > 0) {
            wynik += konwertujLiczbe(reszta);
        }
        return wynik.strip();
    }


    public static String konwertujLiczbe(int liczba) {
        int setki = liczba / 100;
        int dziesiatki = (liczba - setki * 100) / 10;
        int jednosci = liczba - setki * 100 - dziesiatki * 10;
        String wynik = "";
        if (setki > 0) {
            wynik += Liczby.setki[setki] + " ";
        }
        if (dziesiatki > 0) {
            if (dziesiatki == 1) {
                wynik += Liczby.nastki[jednosci];
                return wynik.strip();
            } else {
                wynik += Liczby.dziesiatki[dziesiatki] + " ";
            }
        }
        if (jednosci > 0) {
            wynik += Liczby.jednosci[jednosci];
        }
        return wynik.strip();
    }


    public static int odmiana(int liczba) {
        if (liczba == 1) {
            return 1;
        } else if (liczba % 10 >= 2 && liczba % 10 <= 4 && (liczba % 100 < 10 || liczba % 100 >= 20)) {
            return 2;
        } else {
            return 3;
        }
    }

}
