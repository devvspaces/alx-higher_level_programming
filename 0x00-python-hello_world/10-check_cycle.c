#include "lists.h"

/**
 * check_cycle - check if list is cycle
 *
 * @list: type listint_t
 *
 * Return: always int
 * case: 1 true, 0 false
 */
int check_cycle(listint_t *list)
{
    listint_t *fly = list, *spider = list;

    while (fly != NULL && spider != NULL && spider->next != NULL)
    {
        fly = fly->next;
        spider = spider->next->next;
        if (fly == spider)
            return (1);
    }
    return (0);
}
