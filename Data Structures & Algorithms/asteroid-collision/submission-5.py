class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            # print(f"\nfor : {st}")
            if asteroid > 0:
                st.append(asteroid)
            else:
                insert = True
                while st and st[-1] > 0 and st[-1] <= abs(asteroid):
                    # print(f"\twhile : {st}")
                    popped = st.pop()
                    if popped == abs(asteroid):
                        insert = False
                        break
                if insert and (not st or st[-1] < 0):
                    st.append(asteroid)
        return st