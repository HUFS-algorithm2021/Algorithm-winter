#include <iostream>
using namespace std;

int main() {
	int N;
	int count = 1;
	int cycle[100] = { 0 };
	cin >> N;
	cycle[0] = N;
	
	while(1){
		cycle[count] = (cycle[count-1] % 10 + (cycle[count - 1] / 10))%10 + (cycle[count - 1] % 10)*10;
        
		if (cycle[count] == N) {
			cout << count << endl;
			break;
		}
		else
			count++;
	}


	return 0;

}