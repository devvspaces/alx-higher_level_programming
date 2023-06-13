#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_linkedlist - reverse a linked list
 *
 * @head: head
 *
 * Return: head of the reversed linked list
 */
listint_t *reverse_linkedlist(listint_t *head)
{
    listint_t *prev, *node, *next;

    if (head == NULL)
        return (head);

    prev = NULL;
    node = head;
    next = head->next;
    while (next != NULL)
    {
        node->next = prev;
        prev = node;
        node = next;
        next = node->next;
    }
    node->next = prev;
    return (node);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    fast = *head, slow = *head;
    while (fast->next != NULL && fast->next->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    fast = reverse_linkedlist(slow->next), slow = *head;

    while (fast->next != NULL)
    {
        if (slow->n != fast->n)
            return (0);
        slow = slow->next;
        fast = fast->next;
    }

    if (slow->n != fast->n)
        return (0);

    return (1);
}
