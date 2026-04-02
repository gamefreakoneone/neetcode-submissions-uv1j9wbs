class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> lastSeen;
        int maxLen = 0;
        int i = 0;
        for(int j = 0 ; j < s.size() ; j++){
            if(lastSeen.count(s[j]) && lastSeen[s[j]] >=i){
                i = lastSeen[s[j]]+1;
            }
            lastSeen[s[j]] = j;
            maxLen = max(maxLen , j -i +1);
        }
        return maxLen;
    }
};
