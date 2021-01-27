#include <iostream>
#include <math.h>
using namespace std;
 
int N, r, c, position;//main문외에도 사용할수있도록 밖에 선언

 
void Nmaze(int x, int y, int size) {//x,y=0,size=2^N
   if (y == r && x == c) {         
      cout << position << endl;
      return;
   }
   if (size == 1) {               
      position++; return;
   }
   if (!(y <= r && r<y + size && x <= c && c<x + size)) { 
      position += size * size;
      return;
   }
   Nmaze(x, y, size / 2);
   Nmaze(x + size / 2, y, size / 2);
   Nmaze(x, y  + size / 2, size / 2);
   Nmaze(x + size / 2, y + size / 2, size / 2);
}
 
int main() {
   cin>>N>>r>>c;          
   Nmaze(0, 0, pow(2, N)); 
   return 0;
}