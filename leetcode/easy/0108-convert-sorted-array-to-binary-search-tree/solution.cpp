class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        return createBST(nums, 0, static_cast<int>(nums.size()) - 1);
    }

    TreeNode* createBST(vector<int>& nums, int low, int high) {
        if (low>high) return nullptr;

        int mid=(low+high)/2;
        TreeNode*root=new TreeNode(nums[mid]);

        root->left=createBST(nums,low,mid-1);
        root->right=createBST(nums,mid+1,high);

        return root;
    }
};