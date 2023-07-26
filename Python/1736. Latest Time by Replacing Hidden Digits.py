class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        temp = ["0", "0", ":", "0", "0"]

        for i in range(23, -1, -1):
            for j in range(59, -1, -1):
                if i < 10: temp[0] = "0"; temp[1] = str(i)
                else: temp[0] = str(i)[0]; temp[1] = str(i)[1]
                if j < 10: temp[3] = "0"; temp[4] = str(j)
                else: temp[3] = str(j)[0]; temp[4] = str(j)[1]

                if time[0] != "?" and time[0] != temp[0]: continue
                if time[1] != "?" and time[1] != temp[1]: continue
                if time[3] != "?" and time[3] != temp[3]: continue
                if time[4] != "?" and time[4] != temp[4]: continue

                return "".join(temp)
