// Mikołaj Kalitka
// 337362
// LJE

#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    for (int i = ((a + 2023) / 2024) * 2024; i <= b; i += 2024)
        cout << i << " ";
    return 0;
}
