#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    int root = 1;

    int graph[n + 1];
    graph[0] = 0;
    graph[1] = 1;
    int children[n + 1];
    int childrenStartIndex[n + 1];

    for (int i = 0; i <= n; i++) {
        children[i] = 0;
    }

    pair<int, int> pairs[n - 1];
    for (int i = 0; i < n - 1; i++) {
        int p;
        cin >> p;
        pairs[i] = make_pair(p, i + 2);
        children[p]++;
    }

    int index = 1;
    for (int i = 1; i <= n; i++) {
        childrenStartIndex[i] = index;
        index += children[i];
    }

    sort(pairs, pairs + n - 1);

    for (int i = 2; i <= n; i++) {
        graph[i] = pairs[i - 2].second;
    }

    int counter_in[n + 1];
    int counter_out[n + 1];
    for (int i = 0; i <= n; i++) {
        counter_in[i] = 0;
        counter_out[i] = 0;
    }
    int counter = 1;

    stack<int> s2;
    s2.push(root);
    while (!s2.empty()) {
        int node = s2.top();
        if (counter_in[node] == 0) {
            counter_in[node] = counter;
            counter++;
        } else {
            counter_out[node] = counter;
            counter++;
            s2.pop();
            continue;
        }
        for (int i = childrenStartIndex[node] + 1; i <= childrenStartIndex[node] + children[node]; i++) {
            s2.push(graph[i]);
        }
    }

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        if (counter_in[a] < counter_in[b] && counter_out[a] > counter_out[b]) {
            cout << "TAK" << endl;
        } else {
            cout << "NIE" << endl;
        }
    }
    
    return 0;
}
