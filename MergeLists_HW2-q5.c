/*
Question 5. You are given the heads of two sorted linked lists list1 and list2. Write a
solution that merges the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists. Your function should return the head of
the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]
*/

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

// standard array to a linked list
struct Node* buildList(int* arr, int size) {
    if (size == 0) return NULL;

    struct Node* head = malloc(sizeof(struct Node));
    head -> data = arr[0];
    head -> next = NULL;

    struct Node* currentNode = head;
    for (int i = 1; i < size; i++) {
        currentNode -> next = malloc(sizeof(struct Node));
        currentNode -> next -> data = arr[i];
        currentNode -> next -> next = NULL;
        currentNode = currentNode -> next;
    }
    return head;
}

// print list
void printList(struct Node* head) {
    printf("[");
    while (head != NULL) {
        printf("%d", head -> data);
        if (head->next != NULL) printf(",");
        head = head->next;
    }
    printf("]\n");
}

// free malloc
void freeList(struct Node* head) {
    while (head != NULL) {
        struct Node* temp = head;
        head = head -> next;
        free(temp);
    }
}

struct Node* mergeLists(struct Node* list1, struct Node* list2) {
    // temp "dummy" node so the real head does not need to be set
    // helps with edge cases
    struct Node tempHead;
    struct Node* currentNode = &tempHead;
    tempHead.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1 -> data <= list2 -> data) {
            currentNode -> next = list1; // splice in list1
            list1 = list1 -> next;
        } else {
            currentNode -> next = list2; // splice in list2
            list2 = list2 -> next;
        }
        currentNode = currentNode -> next;
    }

    // append remaining nodes (list 1 or list 2)
    currentNode -> next = (list1 != NULL) ? list1 : list2;

    return tempHead.next;
}

int main() {
    int arr1[] = {1, 2, 4};
    int arr2[] = {1, 3, 4};

    // create linked list from a standard array
    struct Node* list1 = buildList(arr1, 3);
    struct Node* list2 = buildList(arr2, 3);
    printf("List 1: "); printList(list1);
    printf("List 2: "); printList(list2);

    // merge lists
    struct Node* merged = mergeLists(list1, list2);
    printf("Merged: "); printList(merged);

    // free malloc and end
    freeList(merged);
    return 0;
}
