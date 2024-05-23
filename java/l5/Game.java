import java.util.*;
import java.util.logging.*;

/**
 * Klasa reprezentująca grę, w której gracz musi odgadnąć ukrytą permutację liczb.
 */
public class Game {
    private static final Logger logger = Logger.getLogger(Game.class.getName());
    private final List<Integer> hiddenPermutation;
    private final int maxAttempts;
    private int attemptCount;
    private final List<String> history;

    /**
     * Konstruktor klasy Game.
     * @param n rozmiar permutacji do odgadnięcia.
     */
    public Game(int n) {
        hiddenPermutation = generatePermutation(n);
        maxAttempts = n * n;
        attemptCount = 0;
        history = new ArrayList<>();
        logger.info("Gra rozpoczęta z permutacją o rozmiarze " + n);
    }

    /**
     * Generuje losową permutację liczb od 1 do n.
     * @param n rozmiar permutacji.
     * @return lista z losową permutacją liczb.
     */
    private List<Integer> generatePermutation(int n) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }
        Collections.shuffle(numbers);
        return numbers;
    }

    /**
     * Metoda do wykonania zgadywania permutacji.
     * @param guess lista z propozycją permutacji.
     * @return wynik zgadywania w postaci tekstowej.
     * @throws InvalidInputException jeśli wejście jest nieprawidłowe.
     */
    public String makeGuess(List<Integer> guess) throws InvalidInputException {
        validateInput(guess);
        attemptCount++;

        if (guess.equals(hiddenPermutation)) {
            String response = "Dobrze! Zgadłeś permutację w " + attemptCount + " próbach.";
            logger.info("Próba " + attemptCount + ": " + response);
            history.add(response);
            return response;
        }

        int incorrectPositions = countIncorrectPositions(guess);
        int incorrectIndex = findRandomIncorrectIndex(guess);
        String hint = generateHint(guess, incorrectIndex);

        String response = incorrectPositions + " niepoprawnych pozycji. " + hint;
        logger.info("Próba " + attemptCount + ": " + response);
        history.add(response);
        return response;
    }

    /**
     * Waliduje wejście użytkownika.
     * @param guess lista z propozycją permutacji.
     * @throws InvalidInputException jeśli wejście jest nieprawidłowe.
     */
    private void validateInput(List<Integer> guess) throws InvalidInputException {
        if (new HashSet<>(guess).size() != hiddenPermutation.size() || 
            !guess.stream().allMatch(x -> x >= 1 && x <= hiddenPermutation.size())) {
            throw new InvalidInputException("Nieprawidłowe wejście: wejście musi zawierać różne liczby od 1 do " + hiddenPermutation.size());
        }
    }

    /**
     * Liczy liczbę niepoprawnych pozycji w zgadywaniu.
     * @param guess lista z propozycją permutacji.
     * @return liczba niepoprawnych pozycji.
     */
    private int countIncorrectPositions(List<Integer> guess) {
        int count = 0;
        for (int i = 0; i < guess.size(); i++) {
            if (!guess.get(i).equals(hiddenPermutation.get(i))) {
                count++;
            }
        }
        return count;
    }

    /**
     * Znajduje losowy indeks niepoprawnej pozycji w zgadywaniu.
     * @param guess lista z propozycją permutacji.
     * @return indeks niepoprawnej pozycji.
     */
    private int findRandomIncorrectIndex(List<Integer> guess) {
        List<Integer> incorrectIndices = new ArrayList<>();
        for (int i = 0; i < guess.size(); i++) {
            if (!guess.get(i).equals(hiddenPermutation.get(i))) {
                incorrectIndices.add(i);
            }
        }
        Collections.shuffle(incorrectIndices);
        return incorrectIndices.get(0);
    }

    /**
     * Generuje podpowiedź dla użytkownika na podstawie niepoprawnej pozycji.
     * @param guess lista z propozycją permutacji.
     * @param index indeks niepoprawnej pozycji.
     * @return podpowiedź w postaci tekstowej.
     */
    private String generateHint(List<Integer> guess, int index) {
        int actualPosition = hiddenPermutation.indexOf(guess.get(index));
        if (actualPosition < index) {
            return "Liczba " + guess.get(index) + " powinna być przesunięta w lewo.";
        } else {
            return "Liczba " + guess.get(index) + " powinna być przesunięta w prawo.";
        }
    }

    /**
     * Sprawdza, czy gra się zakończyła.
     * @return true jeśli liczba prób przekroczyła maksymalną liczbę prób, w przeciwnym razie false.
     */
    public boolean isGameOver() {
        return attemptCount >= maxAttempts || history.stream().anyMatch(x -> x.contains("Dobrze"));
    }

    /**
     * Zwraca historię zgadywań.
     * @return lista z historią zgadywań.
     */
    public List<String> getHistory() {
        return history;
    }
}
