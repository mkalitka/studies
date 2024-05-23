/**
 * Wyjątek sygnalizujący nieprawidłowe dane wejściowe.
 */
public class InvalidInputException extends Exception {
    /**
     * Konstruktor tworzący wyjątek z podaną wiadomością.
     *
     * @param message wiadomość opisująca szczegóły wyjątku
     */
    public InvalidInputException(String message) {
        super(message);
    }
}
