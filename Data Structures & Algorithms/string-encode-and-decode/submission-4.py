class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return None
        encoded_str = "\t".join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        if len(s) == 0:
            return [""]
        return s.split("\t")