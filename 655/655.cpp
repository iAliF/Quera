#include <iostream>

using namespace std;

char toLower(char c) {
	if (c >= 'A' && c <= 'Z')
		c += 32;
	return c;
}

char toUpper(char c) {
	if (c >= 'a' && c <= 'z')
		c -= 32;
	return c;
}

int main() {
	int n;
	cin >> n;
	cin.ignore();
	
	string strs[n];
	for (int i = 0; i < n; i++) {
		string s;
		getline(cin, s);
		int length = s.length();
		
		for (int k = 0; k < length; k++)
			if (k == 0 || s[k - 1] == ' ')
				s[k] = toUpper(s[k]);
			else
				s[k] = toLower(s[k]);
		
		strs[i] = s;
	}
	
	for (string s: strs)
		cout << s << endl;
	
	return 0;
}