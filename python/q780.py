class Solution(object):

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        #print sx, sy, tx, ty
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx = tx % ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty = ty % tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


if __name__ == "__main__":

    print Solution().reachingPoints(1,1,10000000,1)