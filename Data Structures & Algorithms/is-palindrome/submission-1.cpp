class Solution {
public:
    bool isPalindrome(string s) {
        string filtered;
        for(char c : s) {
            if(isalnum(c)) {
                filtered += tolower(c);
            }
        }

        for(int i = 0; i < filtered.size() ; i++){
            if(filtered[i] != filtered[filtered.size()-1-i]) {
                return false;
            }
        }
        return true;
    }
};
