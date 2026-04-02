class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()==0){
            return 0;
        }
        int i = 0;
        int j = 1;
        int max_profit = 0;
        while(i < j && j < prices.size()){
            int profit = prices[j]-prices[i];
            if(profit<=0){
                i =j ;
                j=i+1;
            }else if(profit>0){
                if(profit>max_profit){
                    max_profit = profit;
                }
                j++;
            }
        }
        return max_profit;
    }
};
