class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> freq(nums.size()+1, vector<int>{});
        unordered_map<int, int> count;
        for(int i = 0; i<nums.size(); i++){
            if(count.find(nums[i]) == count.end()){
                count[nums[i]] = 1;
            }
            else count[nums[i]]++;
        } 
        for(auto &ind: count){
            freq[ind.second].push_back(ind.first);
        }
        vector<int> ans;
        int curr = freq.size()-1;
        while(ans.size()<k){
            for(int i = 0; i<freq[curr].size(); i++){
                ans.push_back(freq[curr][i]);
            }
            curr--;
        }
        return ans;
    }
};