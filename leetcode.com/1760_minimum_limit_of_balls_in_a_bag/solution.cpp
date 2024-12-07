class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations)
    {
        auto lo = 1;
        auto hi = *std::max_element(nums.begin(), nums.end());

        while (lo <= hi) {
            auto mid = (lo + hi) / 2;

            // check is possible
            auto t = maxOperations;
            for (auto i = 0 ; i < nums.size(); i++) {
                t -= ceil((double)(nums[i] - mid) / mid);
            }

            if (t >= 0) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        return lo;
    }
};
