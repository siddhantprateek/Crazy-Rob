#include <bits/stdc++.h>
using namespace std;
int main()
{
    random();
    int PICKER;
    PICKER = 1 + rand(3);
    char COLOR[][6] = {"BLUE", "PINK", "GREEN", "RED"};
    for (int i = 0; i < PICKER; i++)
    {
        for (int j = 0; j < i; j++)
            cout << COLOR[j];
        cout << endl;
    }
    return 0;
}