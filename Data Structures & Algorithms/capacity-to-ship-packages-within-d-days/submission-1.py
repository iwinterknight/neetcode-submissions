class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculate_days_to_ship(capacity):
            days_to_ship = 0
            residual_capacity = capacity
            i = 0
            while i < len(weights):
                # print(days, i, weights[i], residual_capacity)
                if weights[i] <= residual_capacity:
                    residual_capacity -= weights[i]
                    i += 1
                else:
                    days_to_ship += 1
                    residual_capacity = capacity
            return days_to_ship + 1

        def bisect_right():
            # greatest element lte
            l, r = max(weights), sum(weights)
            while l <= r:
                mid = l + (r-l) // 2
                days_to_ship = calculate_days_to_ship(mid)
                if days_to_ship <= days:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def bisect_right_recursive(l, r):
            if l == r:
                return l  # l-1 generally
            mid = l + (r-l) // 2
            days_to_ship = calculate_days_to_ship(mid)
            if days_to_ship > days:
                return bisect_right_recursive(mid+1, r)
            else:
                return bisect_right_recursive(l, mid)

        # return bisect_right()
        return bisect_right_recursive(max(weights), sum(weights))

                
