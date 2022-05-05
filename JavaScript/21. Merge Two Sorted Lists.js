/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if(!list1 && !list2) return null;
    if(!list1) return list2;
    if(!list2) return list1;
    var a = null;
    if(list1.val < list2.val){
        a = new ListNode(list1.val);
        a.next = mergeTwoLists(list1.next, list2);
    }
    else{
        a = new ListNode(list2.val);
        a.next = mergeTwoLists(list2.next, list1);
    }
    return a;
};
