class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> values;
        for(int i = 0 ; i < nums.size() ; i++){
            if(!values.count(target - nums[i])){
                values[nums[i]] = i;
            }else{
                vector<int> answer = {values[target - nums[i]] , i};
                return answer;
            }
        }
        vector<int> answer = {0,0};
        return answer;
    }
};
