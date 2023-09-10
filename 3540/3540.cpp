#include <iostream>

using namespace std;

int main () {
	int n, x, y;
	cin >> n >> x >> y;
	
	if (n % x == 0) {
		cout << n / x << " 0";
		return 0;
	}
	if (n % y == 0) {
		cout << "0 " << n / y;
		return 0;
	}
	
	int sum = 0;
	while (sum < n) {
		sum += x;
		
		int t = n - sum;
		
		if (t % y == 0) {
			cout << sum / x << " " << t / y;
			return 0;
		}
	}
	
	cout << -1;
	
	return 0;
}