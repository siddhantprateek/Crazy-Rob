#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    long long int v[t];
    long long int input;
    while (t >= 0)
    {
        cin >> input;
        if (input >= 2)
            v[--t] = input;

        if (v[t] % 2 == 0)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }

    // for (int i = 0; i < t; i++)
    // {
    //     cin >> v[i];
    // }
    // for (int i = 0; i < t; i++)
    // {
    //     if (v[i] % 2 == 0 && v[i] >= 2)
    //         cout << "NO" << endl;
    //     else
    //         cout << "YES" << endl;
    // }
    return 0;
}