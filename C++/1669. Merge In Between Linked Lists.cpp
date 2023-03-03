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
    ListNode* combine(ListNode* list1, ListNode* list2) {
        if(!list1->next){
            list1->next = list2;
            return list1;
        }

        combine(list1->next, list2);

        return list1;
    }

    ListNode* cutting(ListNode* list, int a) {
        if(a == 0){
            list->next = nullptr;
            return list;
        }

        cutting(list->next, a - 1);

        return list;
    }

    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* temp = new ListNode();
        temp = list1;

        while(b >= 0){
            temp = temp->next;
            b--;
        } 

        list1 = cutting(list1, a - 1);
        list1 = combine(list1, list2);
        list1 = combine(list1, temp);

        return list1;
    }
};
