class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        return self.restorePartIpAddress(s, 4)

    def restorePartIpAddress(self, s, n):
        if len(s) < n:
            return []
        if n == 1:
            if s == "0":
                return ["0"]
            elif s[0] == "0":
                return []
            elif self.is_valid_sector(s):
                return [s]
            else:
                return []
        else:
            result = []
            if s[0] == "0":
                segment = "0"
                ip_segments = self.restorePartIpAddress(s[1:], n-1)
                result.extend([segment+"."+ip_segment for ip_segment in ip_segments])
            else:
                max_i = min(4, len(s))
                for i in range(1,max_i):
                    segment = s[:i]
                    if self.is_valid_sector(segment):
                        ip_segments = self.restorePartIpAddress(s[i:], n-1)
                        result.extend([segment+"."+ip_segment for ip_segment in ip_segments])
            return result

    def is_valid_sector(self, s):
        return 0 <= int(s) <= 255


if __name__ == "__main__":

    print Solution().restoreIpAddresses("")
