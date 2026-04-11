class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> LHP(nums.size(), 1);
        vector<int> RHP(nums.size(), 1);
        for(int i = 1; i < nums.size(); i++){
            int curr_val = LHP[i-1]*nums[i-1];
            LHP[i] = curr_val;
        }
        for(int i = nums.size()-2; i >=0 ; i--){
            int curr_val = RHP[i+1]*nums[i+1];
            RHP[i] = curr_val;
        }
        vector<int> result(nums.size());
        for(int i =0; i <nums.size(); i++){
            result[i] = LHP[i]*RHP[i];
        }
        return result;
    }
};
