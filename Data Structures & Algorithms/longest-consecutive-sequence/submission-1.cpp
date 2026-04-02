class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        unordered_map<int, bool> avail_num;
        int largest_num= -10^9;
        int smallest_num = 10^9;
        for(int i = 0; i < nums.size(); i++){
            avail_num[nums[i]]= true;
            if(nums[i]>largest_num){
                largest_num = nums[i];
            }else if(nums[i]<smallest_num){
                smallest_num = nums[i];
            }
        }
        int largest_cons = 1;
        int cons = 1;
        for(int i = smallest_num; i <= largest_num ; i++){
            if(avail_num[i] && avail_num[i-1]){
                cons+=1;
            }else{
                if(cons > largest_cons){
                    largest_cons = cons;
                }
                cons = 1;
            }
        }
        if(cons > largest_cons){
                    largest_cons = cons;
                }
         return largest_cons;
    }
};
