#include <iostream>
using namespace std;
/*
다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.
 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
 => paper끼리 비교 & face끼리 비교x
 => 지원자끼리 비교*/
int recruit_find(int paper[], int face[],int size){
    int count=0;
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if(paper[i]>paper[j] && face[i]>face[j]){
                count++;
                break;
            }
        }

    }

    return size-count;
}
int main(){
    int case_num,people_num,paper_max,face_max;
    int paper[20],face[20];
    
    cin >> case_num;
    for(int i=0;i<case_num;i++){
        cin>> people_num;
        for(int j=0;j<people_num;j++){
            cin >> paper[j] >> face[j];//굳이 2차배열혹은 다른배열로 두가지 테케를 동시에 저장할필요는 x
        }
        cout << recruit_find(paper,face,people_num) <<endl;
}
   
    return 0;    
}