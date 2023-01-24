#include <stdio.h>
#include <stack>
#include <iostream>
using namespace std;

int T = 0;
int N;

int main() {
    cin >> T;
    for (int _=0; _<T; _++) {
        cin >> N;
        stack<int> mountain;
        stack<int> branch;
        for (int __=0; __<N; __++) {
            int n;
            cin >> n;
            mountain.push(n);
        }
        int n = 1;
        int status = 0;
        while (1) {
            if (mountain.size() > 0 && mountain.top() == n) {
                n++;
                mountain.pop();
            }
            else if (branch.size() > 0 && branch.top() == n) {
                n++;
                branch.pop();
            }
            else if (mountain.size() > 0 && branch.size() == 0) {
                branch.push(mountain.top());
                mountain.pop();
            }
            else if (mountain.size() == 0 && branch.size() > 0) {
                status = 1;
                break;
            }
            else if (mountain.size() > 0 && branch.size() > 0) {
                if (mountain.top() < branch.top()) {
                    branch.push(mountain.top());
                    mountain.pop();
                }
                else {
                    status = 1;
                    break;
                }
            }
            else {
                break;
            }
        }
        cout << (status ? "N" : "Y") << "\n";
    }

    return 0;
}