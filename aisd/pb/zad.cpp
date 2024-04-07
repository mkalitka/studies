#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <limits>

using namespace std;

struct Point {
    int x;
    int y;
};

bool compareX(Point a, Point b) {
    return a.x < b.x;
}

bool compareY(Point a, Point b) {
    return a.y < b.y;
}

int distance(Point a, Point b) {
    return pow(a.x - b.x, 2) + pow(a.y - b.y, 2);
}

int perimeter(Point a, Point b, Point c) {
    return distance(a, b) + distance(b, c) + distance(c, a);
}

Point tri0, tri1, tri2;

void smallestTriangleHelper(Point px[], Point py[], int n) {
    if (n == 3) {
        tri0 = px[0];
        tri1 = px[1];
        tri2 = px[2];
    }
    if (n <= 5) {
        int min = numeric_limits<int>::max();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    int p = perimeter(px[i], px[j], px[k]);
                    if (p < min) {
                        min = p;
                        tri0 = px[i];
                        tri1 = px[j];
                        tri2 = px[k];
                    }
                }
            }
        }
    }
    
    int mid = n / 2;
    Point midPoint = px[mid];
    Point pyl[mid];
    Point pyr[n - mid];
    int li = 0, ri = 0;
    for (int i = 0; i < n; i++) {
        if (py[i].x <= midPoint.x) {
            pyl[li++] = py[i];
        } else {
            pyr[ri++] = py[i];
        }
    }
    
    int dl = smallestTriangleHelper(px, pyl, mid);
    Point triL0 = tri0;
    Point triL1 = tri1;
    Point triL2 = tri2;
    int dr = smallestTriangleHelper(px + mid, pyr, n - mid);
    Point triR0 = tri0;
    Point triR1 = tri1;
    Point triR2 = tri2;
    int d;
    if (dl < dr) {
        d = dl;
        tri0 = triL0;
        tri1 = triL1;
        tri2 = triL2;
    } else {
        d = dr;
        tri0 = triR0;
        tri1 = triR1;
        tri2 = triR2;
    }

    Point strip[n];
    int index = 0;
    for (int i = 0; i < n; i++) {
        if (abs(py[i].x - midPoint.x) < d) {
            strip[index++] = py[i];
        }
    }

    int min = d;
    for (int i = 0; i < index; i++) {
        for (int j = i + 1; j < index && (strip[j].y - strip[i].y) < d; j++) {
            for (int k = j + 1; k < index && (strip[k].y - strip[j].y) < d; k++) {
                int p = perimeter(strip[i], strip[j], strip[k]);
                if (p < min) {
                    min = p;
                    tri0 = strip[i];
                    tri1 = strip[j];
                    tri2 = strip[k];
                }
            }
        }
    }

    return min;
}

void smallestTriangle(Point points[], int n) {
    Point px[n];
    Point py[n];
    for (int i = 0; i < n; i++) {
        px[i] = points[i];
        py[i] = points[i];
    }
    sort(px, px + n, compareX);
    sort(py, py + n, compareY);
    smallestTriangleHelper(px, py, n);
}

int main() {
    int n;
    cin >> n;
    Point points[n];
    for (int i = 0; i < n; i++) {
        Point p;
        cin >> p.x >> p.y;
        points[i] = p;
    }
    smallestTriangle(points, n);
    cout << tri0.x << " " << tri0.y << endl;
    cout << tri1.x << " " << tri1.y << endl;
    cout << tri2.x << " " << tri2.y << endl;
    return 0;
}


