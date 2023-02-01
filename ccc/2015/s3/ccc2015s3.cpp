#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    int gates[100005];
    int G;
    int P;

    cin >> G;
    for (int i=0; i<G; i++) {
        gates[i] = i;
    }
    cin >> P;

    int total = 0;
    for (int i=0; i<P; i++) {
        int current;
        cin >> current;
        current--;
        vector<int> visited;
        int valid = 1;
        while (1) {
            visited.push_back(current);
            if (gates[current] == current) {
                for (int j=0; j<visited.size(); j++) {
                    gates[visited[j]] = current - 1;
                }
                break;
            }
            if (gates[current] == -1) {
                valid = 0;
                break; 
            }
            current = gates[current];
        }
        if (valid) {
            total += 1;
        }
        else {
            break;
        }
    }
    
    cout << total;
    return 0;
}