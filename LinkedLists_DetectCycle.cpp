"""
Function Description

Complete the function has_cycle in the editor below. It must return a boolean true if the graph contains a cycle, or false.

has_cycle has the following parameter(s):

head: a pointer to a Node object that points to the head of a linked list.
Note: If the list is empty,head  will be null.

Input Format

There is no input for this challenge. A random linked list is generated at runtime and passed to your function.
"""
/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.
A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node *head)
{
    if (head == nullptr)
        return 0;
    Node *second = head;
    Node *first= head ->next;
    while (first != second)
    {
        if (first == nullptr || first->next == nullptr)
            return 0;
        first=first->next->next;
        second =second->next;
    }
    return 1;
}