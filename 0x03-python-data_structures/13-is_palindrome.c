#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * add_nodeint - adds a new node to a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;
    return (new);
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
    listint_t *head2, *current, *p1, *p2;

    head2 = NULL;
    current = *head;

    if (*head == NULL)
        return (1);

    while (current->next != NULL)
    {
        add_nodeint(&head2, current->n);
        current = current->next;
    }
    add_nodeint(&head2, current->n);

    p1 = *head, p2 = head2;

    while (p1 != NULL)
    {
        if (p1->n != p2->n)
            return (free_listint(head2), 0);
        p1 = p1->next, p2 = p2->next;
    }

    return (free_listint(head2), 1);
}