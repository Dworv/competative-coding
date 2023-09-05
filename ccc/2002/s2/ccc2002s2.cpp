#include <stdio.h>
#include <iostream>
#include <math.h>
#include <list>
using namespace std;

int main() {
    int n, d;
    cin >> n;
    cin >> d;

    if (n == 0) {
        cout << 0 << "\n";
        exit(0);
    }

    list<int> nfactors;

    for (int i=1; i<sqrt(n + 1); i++) {
        if (n%i == 0) {
            nfactors.push_back(i);
            nfactors.push_back(n/i);
        }
    }

    list<int> dfactors;

    for (int i=1; i<sqrt(d + 1); i++) {
        if (d%i == 0) {
            dfactors.push_back(i);
            dfactors.push_back(d/i);
        }
    }

    int gcf = 1;

    for (auto df : dfactors) {
        for (auto nf : nfactors) {
            if (nf == df && nf > gcf) {
                gcf = nf;
            }
        }
    }

    n /= gcf;
    d /= gcf;

    int w = 0;
    while (n>=d) {
        w++;
        n-=d;
    }

    if (w && n) {
        cout << w << " " << n << "/" << d << "\n";
    }
    else if (w) {
        cout << w << "\n";
    }
    else {
        cout << n << "/" << d << "\n";
    }
}