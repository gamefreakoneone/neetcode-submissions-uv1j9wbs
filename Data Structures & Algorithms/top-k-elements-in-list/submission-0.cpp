class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int , int> mapping;
        for(int i =0; i < nums.size(); i++){
            mapping[nums[i]]++;
        }

        vector<vector<int>> freq(nums.size()+1);
        for(auto &pair: mapping){
            freq[pair.second].push_back(pair.first);
        }

        vector<int> result;
        for(int i = freq.size()- 1; i>=0 ; i--){
            for(int num : freq[i]){
                result.push_back(num);
            }
            if(result.size()==k){
                return result;
            }
        } 
        return result;
    }
};
