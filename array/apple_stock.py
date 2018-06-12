def maximum_profit(nums):
	
	max_profit = 0;
	
	if len(nums) == 0:
		return max_profit;
	
	if len(nums) == 1:
		return max_profit;
	
	lowest_price = nums[0];
	
	for idx in xrange(1, len(nums)):
		profit = nums[idx] - lowest_price; 
		if profit > max_profit:
			max_profit = profit;
			
		if nums[idx] < lowest_price:
			lowest_price = nums[idx];
	return max_profit

sequ = [10,7,5,8,11,9]
ans = maximum_profit(sequ);
print ans;