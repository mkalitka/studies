#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Moneta {
    int nominal;
    int waga;
};

bool czyMozliwe(vector<int>& waga, vector<int>& nominal, int F) {
    int n = waga.size();
    vector<bool> dp(F + 1, false);
    dp[0] = true;

    for (int i = 0; i < n; ++i) {
        for (int j = F; j >= 0; --j) {
            if (j >= waga[i] && dp[j - waga[i]]) {
                dp[j] = true;
            }
        }
    }

    return dp[F];
}

void znajdzWartosci(vector<int>& waga, vector<int>& nominal, int F) {
    int n = waga.size();
    vector<vector<int> > dp(F + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= F; ++i) {
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = dp[i][j - 1];
            if (i >= waga[j - 1]) {
                dp[i][j] = max(dp[i][j], dp[i - waga[j - 1]][j - 1] + nominal[j - 1]);
            }
        }
    }

    int Pmin = dp[F][n];
    cout << "TAK" << endl;
    cout << Pmin << endl;

    vector<int> ilosc(n, 0);
    int reszta = F;
    for (int i = n; i > 0; --i) {
        while (i > 0 && dp[reszta][i] == dp[reszta][i - 1]) {
            --i;
        }
        if (i > 0 && dp[reszta][i] != dp[reszta][i - 1]) {
            ilosc[i - 1] = 1;
            reszta -= waga[i - 1];
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << ilosc[i] << " ";
    }
    cout << endl;

    int Pmax = F;
    cout << Pmax << endl;
    for (int i = 0; i < n; ++i) {
        cout << Pmax / waga[i] << " ";
    }
    cout << endl;
}

int main() {
    int F, C;
    cin >> F >> C;

    vector<int> waga(C);
    vector<int> nominal(C);

    for (int i = 0; i < C; ++i) {
        cin >> nominal[i] >> waga[i];
    }

    // if (czyMozliwe(waga, nominal, F)) {
        // znajdzWartosci(waga, nominal, F);
    // }
    cout << "NIE" << endl;

    return 0;
}

