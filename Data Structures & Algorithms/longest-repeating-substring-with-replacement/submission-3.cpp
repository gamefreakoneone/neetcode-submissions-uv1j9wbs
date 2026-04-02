class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int result = 0;
        int maxFreq = 0;
        int l= 0, r= 0;
        while (r < s.size()){
            count[s[r]]++;
            maxFreq = max(maxFreq , count[s[r]]);
            if((r-l +1) - maxFreq > k){
                count[s[l]]--;
                l++;
            }
            result = max(r-l+1 , result);
            r++;
            
        }
        return result;
        
    }
};
