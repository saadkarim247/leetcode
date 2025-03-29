class Solution {
public:
    const int MOD = 1000000000;
    int maxProfit(vector<int>& A) {
        if (A.empty())
            return 0;

        int profit = 0;
        int lastBuy = A[0];
        if (A.size() == 1)
            return 0;
        bool increasing = true;

        for (int i = 1; i < A.size(); i++) {
            if (increasing) {
                if (A[i] < A[i - 1]) {
                    increasing = false;
                    profit += A[i - 1] - lastBuy;
                    profit %= MOD;
                }
            } else {
                if (A[i] > A[i - 1]) {
                    increasing = true;
                    lastBuy = A[i - 1];
                }
            }
        }
        if (increasing)
            profit += A[A.size() - 1] - lastBuy;
        profit %= MOD;
        return profit;
    }
};