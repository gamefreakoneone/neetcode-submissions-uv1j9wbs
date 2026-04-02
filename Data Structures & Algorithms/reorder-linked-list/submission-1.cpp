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
    void reorderList(ListNode* head) {
        ListNode* midPoint = head;
        ListNode* endPoint = head;
        int mid_length = 0;
        while(endPoint->next && endPoint->next->next){
            midPoint = midPoint->next;
            endPoint = endPoint->next->next;
        }
        // First half is till midPoint

        // Reverse the rest of the array
        ListNode* secondHalf = midPoint->next;
        midPoint->next = nullptr;

        ListNode* newHead = nullptr;
        while(secondHalf != nullptr){
            ListNode* next = secondHalf->next;
            secondHalf->next = newHead;
            newHead = secondHalf;
            secondHalf = next;
        }

        ListNode* first = head;
        ListNode* second = newHead;
        while(second){
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};
