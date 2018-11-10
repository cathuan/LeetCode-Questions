# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):

    def __init__(self):

        self.buf = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        while len(self.buf) < n:
            tmp_buf = [""]*4
            readLength = read4(tmp_buf)
            if readLength < 4:
                tmp_buf = tmp_buf[:readLength]
            if readLength == 0:
                break
            self.buf += tmp_buf

        index = 0
        while self.buf and n:
            buf[index] = self.buf.pop(0)
            index += 1
            n -= 1
        return index
