 function maxProfit(prices) {
    
    let minPrice = prices[0];
    let maxProfit = 0;
    for(let i=1; i<prices.length;i++){

    const profit = prices[i] - minPrice;
    maxProfit = Math.max(maxProfit , profit)
    minPrice = Math.min(minPrice , prices[i])
        }

        return maxProfit
};
