#include <string>
#include <vector>
#include <algorithm>//sort 함수
using namespace std;

bool Change(string arr1, string arr2)
{
    if (arr1 + arr2 > arr2 + arr1)//문자열이라 이어붙여진다
        return true;
    return false;
}
 
string solution(vector<int> numbers)
{
    
    vector<string> arr;//string 형 벡터 선언
    
    for (int i = 0; i < numbers.size(); i++)//
        arr.push_back(to_string(numbers[i]));//int -> string 형으로 변환후 arr에 대입

    sort(arr.begin(), arr.end(), Change);//배열 정리(가장 큰수 되게끔)
    string str_arr = "";
    for (int i = 0; i < arr.size(); i++)
        str_arr += arr[i];//문자열->문자로 정리

   return str_arr;
}