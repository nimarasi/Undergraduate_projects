// Nimarasibaghmishe_AD_Chap1_Project
#include <iostream>

using namespace std;

int s[1000];

void findMinMax(int low, int high, int &min, int &max) {
    if (low == high - 1 || low == high) {
        if (s[low] < s[high]) {
            min = s[low];
            max = s[high];
        } else {
            min = s[high];
            max = s[low];
        }
    } else {
        int mid = (low + high) / 2;
        int min1, max1, min2, max2;
        findMinMax(low, mid, min1, max1);
        findMinMax(mid + 1, high, min2, max2);
        if (min1 < min2) {
            min = min1;
        } else {
            min = min2;
        }
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
    int max, min;
    findMinMax(0, n - 1, max, min);

    cout << "\nmax = " << max << endl;
    cout << "min : " << min << endl;
    return 0;
}
