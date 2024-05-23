import java.util.Arrays;

public class RozkladLiczby {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Użycie: java RozkladLiczby <liczba1> <liczba2> ... <liczbaN>");
            return;
        }

        for (String arg : args) {
            try {
                long liczba = Long.parseLong(arg);
                long[] czynniki = LiczbyPierwsze.naCzynnikiPierwsze(liczba);
                System.out.println(liczba + " = " + Arrays.toString(czynniki).replaceAll("[\\[\\],]", "").replace(" ", "*"));
            } catch (NumberFormatException e) {
                System.err.println("Błąd: '" + arg + "' nie jest poprawną liczbą typu long.");
            }
        }
    }
}

