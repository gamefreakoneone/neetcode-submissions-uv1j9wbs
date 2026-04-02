class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1, mid = 0;
        while( l <= r){
            mid = (l+r)/2 ;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[l] <= nums[mid]){ // Indicating that left side is sorted
                if(target < nums[l] || target > nums[mid] ){
                    l = mid + 1;
                }else{
                    r = mid - 1;
                }
            }else { // Indicating the right side is sorted
                if(target < nums[mid] || target > nums[r] ){
                    r = mid - 1;
                }else{
                    l = mid + 1;
                }
            }
        }
        return - 1;
    }
};
