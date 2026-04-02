class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char , int> dict1;
        map<char , int> dict2;
        for( char i : s){
            dict1[i]++;
        }
        for( char i : t){
            dict2[i]++;
        }

        if(dict1 == dict2){
            return true;
        }
        return false;
    }
};
