#include <iostream>
#include <vector>
#include <utility> // Do funkcji make_pair

using namespace std;

const int MAX_F = 1e6 + 5; // Maksymalna możliwa waga pudełka
const int MAX_C = 100 + 5; // Maksymalna liczba dostępnych monet

int main() {
  // Pobranie danych wejściowych
  int F, C; // Waga pudełka (F) i liczba monet (C)
  cin >> F >> C;

  // Deklaracja wektora monet
  vector<pair<int, int>> coins(C); // Waga (w) i nominał (p) każdej monety

  // Wczytywanie danych o monetach
  for (int i = 0; i < C; ++i) {
    int w, p; // Waga i nominał aktualnej monety
    cin >> w >> p;
    coins[i] = make_pair(w, p); // Przechowywanie wagi i nominału w parze
  }

  // Tablice do przechowywania wartości i opisów monet
  vector<int> dp(F + 1, 0); // Maksymalna wartość monet o wadze nie większej niż i
  vector<vector<pair<int, int>>> coins_at(F + 1); // Opis monet dających wartość dp[i]

  // Algorytm programowania dynamicznego
  for (const auto& [w, p] : coins) { // Iteracja po wszystkich monetach
    for (int i = F; i >= w; --i) { // Iteracja po możliwych wagach pudełka
      if (dp[i - w] + p <= F) { // Sprawdzenie, czy można uzyskać wartość i za pomocą monety o wadze w
        dp[i] = max(dp[i], dp[i - w] + p); // Aktualizacja maksymalnej wartości
        coins_at[i].push_back(make_pair(w, p)); // Zapis opisu monet dających wartość i
      }
    }
  }

  // Sprawdzanie, czy masa F jest możliwa do uzyskania za pomocą dostępnych monet
  if (dp[F] == F) {
    // Obliczenia dla minimalnej wartości monet
    int Pmin = F; // Minimalna możliwa wartość monet
    vector<pair<int, int>> coins_min; // Opis monet dających wartość Pmin
    for (const auto& [w, p] : coins_at[F]) { // Iteracja po monetach dających wartość F
      if (Pmin >= p) { // Sprawdzenie, czy można dodać monetę do opisu bez przekroczenia Pmin
        coins_min.push_back(make_pair(w, p)); // Dodanie monety do opisu
        Pmin -= p; // Odjęcie nominału monety od Pmin
      }
    }

    // Obliczenia dla maksymalnej wartości monet
    int Pmax = F; // Maksymalna możliwa wartość monet
    vector<pair<int, int>> coins_max; // Opis monet dających wartość Pmax
    for (int i = F; i >= 0; --i) { // Iteracja po możliwych wagach pudełka
      for (const auto& [w, p] : coins_at[i]) { // Iteracja po monetach dających wartość i
        if (Pmax >= p) { // Sprawdzenie, czy można dodać monetę do opisu bez przekroczenia Pmax
          coins_max.push_back(make_pair(w, p)); // Dodanie monety do opisu
          Pmax -= p; // Odjęcie nominału monety od Pmax
          if (Pmax == 0) { // Sprawdzenie, czy znaleziono opis dający Pmax
            break; // Zakończenie iteracji, jeśli znaleziono opis
          }
        }
      }
    }

    // Wyświetlenie wyników
    cout << "TAK" << endl; // Możliwe uzyskanie masy F za pomocą dostępnych monet
    cout << Pmin << endl; // Minimalna możliwa wartość monet
    for (const auto& [w, p] : coins_min) { // Wyświetlenie opisu monet dających Pmin
      cout << w << " " << p << " ";
    }
    cout << endl;
  } else {
    cout << "NIE";
  }

  return 0;
}

