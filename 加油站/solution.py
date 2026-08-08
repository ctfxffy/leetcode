class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_sum = 0
        cur_sum = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_sum += diff
            cur_sum += diff

            if cur_sum < 0:
                start = i + 1
                cur_sum = 0

        if total_sum < 0:
            return -1

        return start
