import java.util.*;
import java.util.logging.*;
import java.io.*;

/**
 * Główna klasa aplikacji.
 */
public class Main {
    private static final Logger logger = Logger.getLogger(Main.class.getName());

    /**
     * Główna metoda uruchamiająca aplikację.
     *
     * @param args argumenty wiersza poleceń
     */
    public static void main(String[] args) {
        try {
            LogManager.getLogManager().readConfiguration(new FileInputStream("logging.properties"));
        } catch (IOException e) {
            System.err.println("Nie można załadować konfiguracji logowania: " + e.getMessage());
        }

        Scanner scanner = new Scanner(System.in);
        boolean playAgain;

        do {
            System.out.println("Wybierz poziom trudności (3-9):");
            int n = scanner.nextInt();
            Game game = new Game(n);

            while (!game.isGameOver()) {
                try {
                    System.out.println("Wprowadź swój strzał (liczby oddzielone spacją):");
                    List<Integer> guess = new ArrayList<>();
                    for (int i = 0; i < n; i++) {
                        guess.add(scanner.nextInt());
                    }

                    String response = game.makeGuess(guess);
                    System.out.println(response);

                    if (response.startsWith("Dobrze")) {
                        break;
                    }

                } catch (InvalidInputException e) {
                    System.out.println("Błąd: " + e.getMessage());
                }

                if (game.isGameOver()) {
                    System.out.println("Koniec gry. Zbyt wiele prób!");
                    logger.warning("Koniec gry z powodu zbyt wielu prób.");
                }
            }

            System.out.println("Zagrać ponownie? (tak/nie):");
            playAgain = scanner.next().equalsIgnoreCase("tak");

        } while (playAgain);

        scanner.close();

        logger.info("Sesja gry zakończona.");
    }
}
