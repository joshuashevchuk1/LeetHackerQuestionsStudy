# this is a dp problem
#
# p_0,p_1,u_0,u_1 are all 1D dp arrays
#

class Solution:
    def numberOfWays(self, s: str) -> int:
        m = len(s)

        # Prefix and suffix counts
        p_0, p_1 = [0] * m, [0] * m
        u_0, u_1 = [0] * m, [0] * m

        # Helper function to compute prefix and suffix counts
        def getPS():
            for i in range(1, m):  # Start from 1 to avoid out-of-bounds for i-1
                if s[i - 1] == '0':  # p_0 count
                    p_0[i] = p_0[i - 1] + 1
                else:
                    p_0[i] = p_0[i - 1]

                if s[i - 1] == '1':  # p_1 count
                    p_1[i] = p_1[i - 1] + 1
                else:
                    p_1[i] = p_1[i - 1]

            for i in range(m - 2, -1, -1):  # Start from m-2 to avoid out-of-bounds for i+1
                if s[i + 1] == '0':  # u_0 count
                    u_0[i] = u_0[i + 1] + 1
                else:
                    u_0[i] = u_0[i + 1]

                if s[i + 1] == '1':  # u_1 count
                    u_1[i] = u_1[i + 1] + 1
                else:
                    u_1[i] = u_1[i + 1]

        # Helper function to calculate result
        def getR():
            r = 0
            for i in range(m):
                if s[i] == '0':  # Valid pattern: "101"
                    r += p_1[i] * u_1[i]
                elif s[i] == '1':  # Valid pattern: "010"
                    r += p_0[i] * u_0[i]
            return r

        getPS()  # Calculate prefix and suffix counts
        return getR()  # Return result directly

