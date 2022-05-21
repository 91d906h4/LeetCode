class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_ = {}
        for i in cpdomains:
            temp = i.split(" ")
            domain = temp[1].split(".")
            for j in range(len(domain)):
                if ".".join(domain[j:]) not in dict_: dict_[".".join(domain[j:])] = int(temp[0])
                else: dict_[".".join(domain[j:])] += int(temp[0])
        return [str(b) + " " + str(a) for a, b in dict_.items()]
