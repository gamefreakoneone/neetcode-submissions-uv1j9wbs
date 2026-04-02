class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int , int> test;
        for(int &i : nums){
            test[i]++;
            if(test[i] > 1){
                return true;
            }
        }
        return false;
    }
};