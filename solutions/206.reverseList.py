"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return "{}{}".format(self.val, ", " + str(self.next) if self.next else "")

    def __repr__(self) -> str:
        return "ListNode[{}]".format(str(self))


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prehead = ListNode()

        while head:
            prev = ListNode(head.val, prehead.next)
            prehead.next = prev
            head = head.next

        return prehead.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Input: head =", head)
    print("Output:", Solution().reverseList(head))
