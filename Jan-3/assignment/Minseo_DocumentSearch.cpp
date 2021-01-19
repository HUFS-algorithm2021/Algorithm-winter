#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    string doc,word;//doc: "문서"에 해당하는 문자, word:"단어"에 해당하는 문자
    int count,index=0;//count:답 , index:겹치는 문자 삭제하기위한 변수
    getline(cin,doc);//공백이 있을경우대비하여 getline으로 입력받음
    getline(cin,word);
    
    while(1){
        if(doc.find(word)==-1)//만약 일치하지않으면 -1을 반환함
            break;
        else//일치한다면
        {
            index = doc.find(word);
            doc.erase(index,index+word.size());//해당하는 문자열을 지워줌
            count++;
         
        }

    }
   
    cout << count << endl;
    return 0;
}
 