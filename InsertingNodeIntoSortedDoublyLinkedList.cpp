"""
Given a reference to the head of a doubly-linked list and an integer,data , create a new
DoublyLinkedListNode object having data value data and insert it into a sorted linked list.
Complete the DoublyLinkedListNode SortedInsert(DoublyLinkedListNode head, int data) method in the
editor below. It has two parameters:
1.head : A reference to the head of a doubly-linked list of Node objects.
2. data : An integer denoting the value of the data field for the Node you must insert into the list.
The method must insert a new Node into the sorted (in ascending order) doubly-linked list whose data
value isdata  without breaking any of the list's double links or causing it to become unsorted.
Note: Recall that an empty list (i.e., where head== null) and a list with one element are sorted lists.
Input Format
The first line contains an integer t, the number of test cases.
Each of the test case is in the following format:
The first line contains an integer n, the number of elements in the linked list.
Each of the n  next lines contains an integer, the data for each node of the linked list.
The last line contains an integer data  which needs to be inserted into the sorted doubly-linked list.
Output Format
Do not print anything to stdout. Your method must return a reference to the head  of the same list
that was passed to it as a parameter.
The ouput is handled by the code in the editor and is as follows:
For each test case, print the elements of the sorted doubly-linked list separated by spaces on a new line.
Sample Input
1
4
1
3
4
10
5
Sample Output
1 3 4 5 10
"""
#include <bits/stdc++.h>

using namespace std;

class DoublyLinkedListNode {
    public:
        int data;
        DoublyLinkedListNode *next;
        DoublyLinkedListNode *prev;

        DoublyLinkedListNode(int node_data) {
            this->data = node_data;
            this->next = nullptr;
            this->prev = nullptr;
        }
};

class DoublyLinkedList {
    public:
        DoublyLinkedListNode *head;
        DoublyLinkedListNode *tail;

        DoublyLinkedList() {
            this->head = nullptr;
            this->tail = nullptr;
        }

        void insert_node(int node_data) {
            DoublyLinkedListNode* node = new DoublyLinkedListNode(node_data);

            if (!this->head) {
                this->head = node;
            } else {
                this->tail->next = node;
                node->prev = this->tail;
            }

            this->tail = node;
        }
};

void print_doubly_linked_list(DoublyLinkedListNode* node, string sep, ofstream& fout) {
    while (node) {
        fout << node->data;

        node = node->next;

        if (node) {
            fout << sep;
        }
    }
}

void free_doubly_linked_list(DoublyLinkedListNode* node) {
    while (node) {
        DoublyLinkedListNode* temp = node;
        node = node->next;

        free(temp);
    }
}

// Complete the sortedInsert function below.

/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode* next;
 *     DoublyLinkedListNode* prev;
 * };
 *
 */
DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* head, int data) {
    DoublyLinkedListNode *new_node = new DoublyLinkedListNode(data);
    if (head == NULL)
    {
        return new_node;
    }
    else if (data <= head->data)
    {
        new_node->next = head;
        head->prev = new_node;
        return new_node;
    }
    else
    {
        DoublyLinkedListNode *temp = sortedInsert(head->next, data);
        head->next = temp;
        temp->prev = head;
        return head;
    }


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        DoublyLinkedList* llist = new DoublyLinkedList();

        int llist_count;
        cin >> llist_count;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        for (int i = 0; i < llist_count; i++) {
            int llist_item;
            cin >> llist_item;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

            llist->insert_node(llist_item);
        }

        int data;
        cin >> data;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        DoublyLinkedListNode* llist1 = sortedInsert(llist->head, data);

        print_doubly_linked_list(llist1, " ", fout);
        fout << "\n";

        free_doubly_linked_list(llist1);
    }

    fout.close();

    return 0;
}

