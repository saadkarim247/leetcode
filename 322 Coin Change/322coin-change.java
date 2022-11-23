class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0){
            return 0;
        }

        int [] dp = new int[amount+1];

        for (int currAmount=1; currAmount<=amount; currAmount++){
            int minCoins = -1;
            boolean firstCoin = true;

            for (int coin: coins){
                int difference = currAmount - coin;
                boolean coinBiggerthanCurrAmount = coin > currAmount;

                if (!coinBiggerthanCurrAmount && dp[difference] != -1){
                    int minForCurrentCoin = dp[difference] + 1;

                    if (firstCoin || minForCurrentCoin < minCoins) { 
                    firstCoin = false;
                    minCoins = minForCurrentCoin;
                    }   
                
                }

            }
            dp[currAmount] = minCoins;
        }
        System.out.println(Arrays.toString(dp));
    return dp[amount];
    }
}