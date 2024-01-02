#include "lists.h"

/**
 * check_cycle - checks if a linkead list has a cycle
 * @list: pointer to the head of the linked liste
 * Return: 1 if there is a cycle, 0 otherewise
 */
int check_cycle(listint_t *list)
{
    /*traverse the list and check if the 
    'next' points to the head of the list*/
    listint_t *current = list;

    if (list == NULL)
        return (0); /*No cycle if the list is empty*/

    while (current->next != NULL)
    {
        if (current->next == list)
            return (1); /*Cycle detected*/

        current = current->next;
    }

    return (0); /* No cycle*/
}
