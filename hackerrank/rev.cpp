#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main()
{
	vector<int> Arr;

	int N, temp, index;
	cin >> N;

	while (index < N)
	{
		cin >> Arr[index];
		index++;
	};
	for (int i = 0; i < N / 2; i++)
	{
		temp = Arr[i];
		Arr[i] = Arr[N - 1 - i];
		Arr[N - 1 - i] = temp;
	}

	for (int i = 0; i < N; i++)
	{
		cout << Arr[i];
	}
	return 0;
}