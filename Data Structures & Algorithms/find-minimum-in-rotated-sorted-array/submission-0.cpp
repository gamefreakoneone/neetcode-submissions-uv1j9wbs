class Solution {
public:
    int findMin(vector<int> &nums) {
        int lowest = nums[0];
        int l =0 , r = nums.size() -1  , mid  = 0;
        while( l < r){
            mid = (l + r) / 2;
            if(nums[mid] > nums[r]){  // I think this indicates that mid is still in the higher end of the sorted array. trnasfer l to mid
                l = mid + 1;
            }else{
            r = mid;
        }
        }
        return nums[l];
    }
};
