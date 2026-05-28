class Codec:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        i,j = 0, 0
        ans = []
        while j < len(s):
            if s[j] == '#':
                lenS = int(s[i:j])
                ans.append(s[j+1:j+lenS+1])
                j = j+lenS+1
                i = j
            j += 1
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))