class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> indexes;

        for( int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if ( map.contains(num) ) {
                indexes = { map[num], i};
                break;
            } else {
                map.insert({ target - num, i});
            }
        }

        return indexes;
    }
};
