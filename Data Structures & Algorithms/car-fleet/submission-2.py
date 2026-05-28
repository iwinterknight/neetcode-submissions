class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        util = list(zip(position, speed))
        util.sort()
        st = []
        for pos, spd in util:
            time = (target - pos) / spd
            while st and st[-1] <= time:
                st.pop()
            st.append(time)
        return len(st)