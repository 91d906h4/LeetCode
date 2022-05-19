class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = {}
        for i in emails:
            i = i.split("@")
            temp1 = i[0].replace(".", "")
            if "+" in temp1: temp1 = temp1[:temp1.find("+")]
            temp2 = i[1]
            result[temp1 + "@" + temp2] = 1
        return len(result)
