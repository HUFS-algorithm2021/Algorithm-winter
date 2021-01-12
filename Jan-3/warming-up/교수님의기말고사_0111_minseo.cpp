//BOJ 20126
#include <iostream>
using namespace std;

int main(){
    int test_num,test_time,total_time;
    cin >> test_num >> test_time >> total_time;
    int x[test_num],y[test_num];
    int test[total_time+1]={0};
    for(int i=0;i<test_num;i++){
        cin>>x[i]>>y[i];
        for(int j=x[i];j<x[i]+y[i];j++)
            test[j]=-1;
        
    }

    int count = 0;
    int finish=0;
    int save;
    while(finish != -1){
        for(int i=0;i<total_time;i++){
            if(test[i]!=-1){
                save =i;
                break;
                
            }
            else{
                if(i==total_time-1){
                    cout<< -1 <<endl;
                    finish = -1;
            }
        }
        }
        for(int j=save;j<save+total_time;j++){
            if(test[j]==-1){
                cout<<-1<<endl;
                break;
                }
            if(j==save+test_time-1)
                cout<<save<<endl;
        
        }
        break;
    
}
    

    return 0;


    }
  
