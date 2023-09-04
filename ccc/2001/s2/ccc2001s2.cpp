#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int count_digit(int number) {
    if (number == 0) {
        return 0;
    }
    int count = 0;
    while(number != 0) {
        number = number / 10;
        count++;
   }
   return count;
}

int getx(int dir, int startx, int prog) {
    if (dir == 0 || dir == 2) {
        return startx;
    }
    if (dir == 1) {
        return startx + prog;
    }
    if (dir == 3) {
        return startx - prog;
    }
}

int gety(int dir, int starty, int prog) {
    if (dir == 1 || dir == 3) {
        return starty;
    }
    if (dir == 0) {
        return starty + prog;
    }
    if (dir == 2) {
        return starty - prog;
    }
}

int main() {
    int S, E;
    cin >> S;
    cin >> E;

    int R[10][10];
    for (int i=0; i<10; i++) {
        for (int j=0; j<10; j++) {
            R[i][j] = 0;
        }
    }
    R[4][4] = S;

    int xbegin = 4;
    int xend = 5;
    int ybegin = 4;
    int yend = 5;

    int startx = 4;
    int starty = 4;
    int line = 0;
    int dir = 0;
    int prog = 1;
    for (int i=1; i<=E-S; i++) {
        R[gety(dir, starty, prog)][getx(dir, startx, prog)] = i + S;;
        prog += 1;
        if (prog > line / 2 + 1) {
            startx = getx(dir, startx, prog - 1);
            starty = gety(dir, starty, prog - 1);
            prog = 1;
            if (dir == 0) {
                yend += 1;
            }
            if (dir == 1) {
                xend += 1;
            }
            if (dir == 2) {
                ybegin -= 1;
            }
            if (dir == 3) {
                xbegin -= 1;
            }
            dir = (dir + 1) % 4;
            line += 1;
        }
    }

    int digits = count_digit(E);

    for (int i=ybegin; i<yend; i++) {
        for (int j=xbegin; j<xend; j++) {
            int missing = digits - count_digit(R[i][j]);
            for (int i=0; i<missing; i++) {
                cout << " ";
            }
            if (R[i][j] > 0) {
                cout << R[i][j];
            }
            cout << " ";
        }
        cout << "\n";
    }

    return 0;
}