class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string , vector<string>> values;
        for(int i = 0; i < strs.size(); i++){
            string key = strs[i];
            sort(key.begin() , key.end());
            values[key].push_back(strs[i]);
        }
        vector<vector<string>> answer;
        for(const auto& pair : values){
            answer.push_back(pair.second);
        }
        return answer;
    }
};
