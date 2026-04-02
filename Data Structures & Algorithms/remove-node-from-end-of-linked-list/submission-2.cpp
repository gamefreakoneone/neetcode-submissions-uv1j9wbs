/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* current = head;
        int length= 0;
        while(current!=nullptr){
            current = current->next;
            length++;
        }
        int terminate = length - n;

        if (terminate == 0) {
        ListNode* newHead = head->next;
        delete head;
        return newHead;
    }

        current = head;
        int curr_len = 0;
        while(curr_len != terminate - 1){
            curr_len++;
            current = current->next;
        }
        
        ListNode* toDelete = current->next;
    current->next = current->next->next;
    delete toDelete;

    return head;

    }
};
