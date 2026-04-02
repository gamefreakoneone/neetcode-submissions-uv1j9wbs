class Solution {
public:
    int maxArea(vector<int>& heights) {
        if(heights.size()==0){
            return 0;
        }
        int i =0 , j = heights.size()-1;
        int max_area = -1;
        while( i < j){
            int distance = abs(j-i);
            int height = min(heights[i] , heights[j]);
            int area = distance * height;
            if(area > max_area){
                max_area = area;
            }
            if(heights[i] < heights[j]){
                i++;
            }else{
                j--;
            }
        }
        return max_area;
    }
};
