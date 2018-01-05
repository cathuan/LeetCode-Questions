class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def construct_list(l):

    if len(l) == 0:
        return None

    head = ListNode(l[0])
    current_node = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        current_node.next = node
        current_node = node
    return head

def print_list(head):

    if head is None:
        return

    current_node = head
    while current_node is not None:
        print current_node.val,
        current_node = current_node.next
    print
