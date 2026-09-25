class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0;
        int r=height.size()-1;
        int max_water=0;
        
        while (l<r){
            int c=std::min(height[l], height[r]) * (r - l);
            max_water=std::max(max_water,c);
            if (height[l]<height[r]){
                l++;
            } else {
                r--;
            }
        }
        return max_water;   
    }
};