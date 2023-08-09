// Nimarasibaghmishe_AD_Chap1_Project
#include <iostream>

using namespace std;

int s[1000];

void findMax(int low, int high, int &max) {
    if (low == high - 1 || low == high) {
        if (s[low] < s[high]) {
            max = s[high];
        } else {
            max = s[low];
        }
    } else {
        int mid = (low + high) / 2;
        int max1, max2;
        findMax(low, mid, max1);
        findMax(mid + 1, high, max2);
        if (max1 > max2) {
            max = max1;
        } else {
            max = max2;
        }
    }
}

int main() {
    int n;
    cout << "How many numbers you want to enter : " << endl;
    cin >> n;
    cout << "---- Please enter " << n << " numbers ---- \n";

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    int max;
    findMax(0, n - 1, max);

    cout << "\nmax = " << max << endl;
    return 0;
}
