#include <stdio.h>
#include <iostream>
#include <math.h>
#include <list>
using namespace std;


int main() {
    int grid[375][70];
    int R, C, M;

    cin >> R;
    cin >> C;
    for (int i=0; i<R; i++) {
        getchar();
        for (int j=0; j<C; j++) {
            if (getchar() == 'X') {
                grid[i][j] = 0;
            }
            else {
                grid[i][j] = 1;
            }
        }
    }

    cin >> M;
    list<int> moves;
    getchar();
    for (int i=0; i<M; i++) {
        char c = getchar();
        if (c == 'F') {
            moves.push_back(1);
        }
        else if (c == 'R') {
            moves.push_back(2);
        }
        else if (c == 'L') {
            moves.push_back(3);
        }
        getchar();
    }

    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            if (grid[i][j] == 0) {
                continue;
            }
            for (int d=0; d<4; d++) {
                int dir=d;
                int r = i;
                int c = j;
                int done = true;
                for (auto m : moves) {
                    if (m == 1) {
                        if (dir == 0) {
                            r -= 1;
                        }
                        else if (dir == 1) {
                            c += 1;
                        }
                        else if (dir == 2) {
                            r += 1;
                        }
                        else if (dir == 3) {
                            c -= 1;
                        }
                        if (r < 0 || r > R || c < 0 || c > C || (grid[r][c] == 0)) {
                            done = false;
                            break;
                        }
                    }
                    else if (m == 2) {
                        dir++;
                        dir%=4;
                    }
                    else if (m == 3) {
                        dir--;
                        dir%=4;
                    }
                }
                if (done == true) {
                    grid[r][c] = 2;
                }
            }
        }
    }

    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            if (grid[i][j] == 0) {
                cout << "X";
            }
            else if (grid[i][j] == 1) {
                cout << ".";
            }
            else {
                cout << "*";
            }
        }
        cout << "\n";
    }
}