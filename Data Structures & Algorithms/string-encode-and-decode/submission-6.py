class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "0"
        if strs==[""]:
            return ""
        s = ""
        for i in strs:
            s = s+i+"|"
        return s

    def decode(self, s: str) -> List[str]:
        if s == "0":
            return []
        if s == "":
            return [""]
        k = s.split("|")
        k.pop()
        return k