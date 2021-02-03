#include <iostream>
using namespace std;
/*
어떤 사람보다 뒤쳐지면 안되므로,
입력받은 두개의 정보중에 최고점수를 뽑고 그 둘중에 하나라도 보유한사람을
정답(count에 더해주자)
*/
/*
python(list 하면 깔꼼할거같아서)
case_num = int(input())
for i in range(case_num):
    people_num = int(input())
    for j in range(people_num):
        people_num = map(int, input().split())

*/
int max_find(int array[],int size){
    int max=array[0];
    for(int i=0;i<size;i++){
        if(max < array[i])
            max = array[i];
    }
    return max;
}
int recruit_find(int array[],int max){

}
int main(){
    int case_num,people_num,paper_max,face_max;
    int paper[20],face[20];
    int count =0;
    cin >> case_num;
    for(int i=0;i<case_num;i++){
        cin>> people_num;
        for(int j=0;j<people_num;j++){
            cin >> paper[j] >> face[j];
        }
        //39,40중에 한줄 날리면됌
        count+=recruit_find(paper,max_find(paper,people_num));
        count+=recruit_find(face,max_find(face,people_num));
}
    cout << count <<endl;
    return 0;    
}