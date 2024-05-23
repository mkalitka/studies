import java.util.List;
import java.util.ArrayList;

public final class LiczbyPierwsze {
    private static final int POTEGA2 = 21;
    private static final int MAX_SITO = 1 << POTEGA2;
    private static final int[] SITO = new int[MAX_SITO];

    static {
        for (int i = 0; i < MAX_SITO; i++) {
            SITO[i] = i;
            for (int j = 2; j * j <= i; j++) {
                if (SITO[i] % SITO[j] == 0) {
                    SITO[i] = SITO[j];
                    break;
                }
            }
        }
    }

    public static boolean czyPierwsza(long n) {
        if (n < 2) return false;
        if (n < MAX_SITO) return SITO[(int) n] == n;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static long[] naCzynnikiPierwsze(long n) {
        if (n == 0 || n == 1 || n == -1) return new long[] {n};
        if (n < 0) {
            long[] czynniki = naCzynnikiPierwsze(-n);
            long[] wynik = new long[czynniki.length + 1];
            wynik[0] = -1;
            System.arraycopy(czynniki, 0, wynik, 1, czynniki.length);
            return wynik;
        }
        List<Long> czynniki = new ArrayList<>();
        outerloop:
        while (n > 1) {
            for (long i = 2; i < MAX_SITO; i++) {
                if (SITO[(int) i] == i && n % i == 0) {
                    czynniki.add(i);
                    n /= i;
                    continue outerloop;
                }
            }
            for (long i = MAX_SITO; i * i <= n; i++) {
                if (n % i == 0) {
                    czynniki.add(i);
                }
            }
            break;
        }
        return czynniki.stream().mapToLong(Long::longValue).toArray();
    }
}

