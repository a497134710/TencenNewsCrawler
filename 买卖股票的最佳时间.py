'''如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。注意你不能在买入股票前卖出股票。'''class Solution:    def maxProfit(self, List):        if len(List) < 2:            return 0        price = []        for i in range(1, len(List)):          if List[i] - List[i - 1] > 0:            #                List[i],List[i - 1] = List[i-1],List[i] - List[i - 1]                price.append(List[i - 1])        return max(price) if len(price) > 0 else 0