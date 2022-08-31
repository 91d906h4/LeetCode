class Solution:
    def reformatNumber(self, number: str) -> str:
        number = "".join([x for x in number if x != " " and x != "-"])
        if len(number) % 3 != 1: return "-".join(re.findall("...?", number))
        else: return "-".join(re.findall("...", number[:-4])) + ("-" if len(number) > 4 else "") + number[-4:-2] + "-" + number[-2:]
