class Solution {
public:
    string minWindow(string s, string t) {
        if(t.size()==0){
            return "";
        }

        unordered_map<char , int> count_t, window;
        int have = 0;
        pair<int , int> substring = {-1,-1};
        for(char c: t){
            count_t[c]++;
        }
        int need = count_t.size();
        int resLen = INT_MAX;
        int l = 0;

        for(int r =0; r < s.size() ; r++){
            char c = s[r];
            window[s[r]]++;
            if(count_t.count(c) && window[c]==count_t[c]){
                have++;
            }

            while(have == need){
                if((r-l+1) < resLen){
                    resLen = r - l + 1;
                    substring = {l , r};
                }

                window[s[l]]--;
                if(count_t.count(s[l]) && window[s[l]] < count_t[s[l]]){
                    have--;
                }
                l++;
            }
        }
        return resLen == INT_MAX ? "" : s.substr(substring.first , resLen);
    }
};
