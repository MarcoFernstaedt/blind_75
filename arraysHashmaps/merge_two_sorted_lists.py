class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


# Helpers
def from_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


# Cases
tests = [
    ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([], [], []),
    ([], [0, 1], [0, 1]),
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),
    ([5], [], [5]),
]

for a, b, expect in tests:
    l1 = from_list(a)
    l2 = from_list(b)
    merged = mergeTwoLists(l1, l2)
    got = to_list(merged)
    print(f"{a} + {b} -> {got}  {'OK' if got==expect else 'FAIL, expect '+str(expect)}")
