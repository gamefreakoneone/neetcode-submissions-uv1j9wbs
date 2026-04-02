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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr){
            return list2;
        } else if(list2 == nullptr){
            return list1;
        }
        ListNode* currNode1 = list1;
        ListNode* currNode2 = list2;
        ListNode* newHead = nullptr ;
        if(currNode1->val <= currNode2->val){
            newHead = currNode1;
            currNode1 = currNode1->next;
        }else{
            newHead = currNode2;
            currNode2 = currNode2->next;
        }
        ListNode* currNewNode = newHead;
        while(currNode1 != nullptr && currNode2 != nullptr){
            if(currNode1->val <= currNode2->val){
            currNewNode->next = currNode1;
            currNode1 = currNode1->next;
        }else{
            currNewNode->next = currNode2;
            currNode2 = currNode2->next;
        }
            currNewNode = currNewNode->next;
        }

        while(currNode1 != nullptr){
            currNewNode->next = currNode1;
            currNode1 = currNode1->next;
            currNewNode = currNewNode->next;
        }
        while(currNode2 != nullptr){
            currNewNode->next = currNode2;
            currNode2 = currNode2->next;
            currNewNode = currNewNode->next;
        }

        return newHead;
    }
};
