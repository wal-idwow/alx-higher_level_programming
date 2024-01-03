#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *rapide, *douce;

    if (list == NULL || list->next == NULL)
        return (0); /* No cycle if the list is empty or has only one node*/

    rapide = list;
    douce = list;

    while (douce != NULL && douce->next != NULL)
    {
        rapide = rapide->next;
        douce = douce->next->next;

        if (rapide == douce)
            return (1); /* Cycle detected*/
    }

    return (0); /* No cycle */
}
