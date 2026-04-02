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
    ListNode* reverseList(ListNode* head) {
        if( head == nullptr){
            return head;
        }
        ListNode* newList = nullptr;
        ListNode* current = head;
        while(head!=nullptr){
            ListNode* next= head->next;
            current = head;
            current->next = newList;
            newList = current;
            head = next;
        }
        return newList;
    }
};
