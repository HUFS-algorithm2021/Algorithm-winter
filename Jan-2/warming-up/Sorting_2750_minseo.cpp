//BoJ 2750
#include <iostream>
using namespace std;

int main(){
int N;
int change;
cin >> N;//입력
int num_list[N];
for(int i=0;i<N;i++){
    cin >> num_list[i];
}

for(int j=0;j<N-1;j++){
    for(int i=0;i<N-1;i++){
        if(num_list[i]>num_list[i+1]){
            change =num_list[i];
            num_list[i]=num_list[i+1];
            num_list[i+1] = change;
    }

}
}

for(int i=0;i<N;i++){
    cout << num_list[i]<<endl;
}

    return 0;
}