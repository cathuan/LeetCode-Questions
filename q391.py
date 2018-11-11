class Solution(object):

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        # left-bottom point: (x1, y1)
        # right-top point: (x2, y2)
        x1 = float("inf")
        y1 = float("inf")
        x2 = float("-inf")
        y2 = float("-inf")

        vertices = set()
        area = 0

        # rect = (x1, y1, x2, y2)
        for rect in rectangles:
            rect_x1, rect_y1, rect_x2, rect_y2 = rect
            rect_vertices = [(rect_x1, rect_y1), (rect_x1, rect_y2),
                             (rect_x2, rect_y1), (rect_x2, rect_y2)]
            for p in rect_vertices:
                if p in vertices:
                    vertices.remove(p)
                else:
                    vertices.add(p)

            x1 = min(rect_x1, x1)
            y1 = min(rect_y1, y1)
            x2 = max(rect_x2, x2)
            y2 = max(rect_y2, y2)

            area += (rect_y2-rect_y1) * (rect_x2-rect_x1)

        if (x1, y1) not in vertices or (x1, y2) not in vertices or (x2, y1) not in vertices or (x2, y2) not in vertices or len(vertices) != 4:
            return False
        if area != (y2-y1) * (x2-x1):
            return False
        return True


if __name__ == "__main__":

    print Solution().isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
