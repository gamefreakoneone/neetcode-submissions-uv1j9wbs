class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int , int> duplicates;
        for(int &i : nums){
            duplicates[i]+=1;
            if(duplicates[i] > 1){
                return true;
            }
        }
        return false;
    }
};