#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list head
 * Return: 0 if it is a palindrome
 * 1 if it is a palidrome
*/

/*check if the list is empty or has only element*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (find_palindrome(head, *head));
}

/**
 * find_palindrome - check if is it a palindrome
 * @head: pointer to the head of the list
 * @end: list end
 * Return: pointer to new head of the reversed list
*/

listint_t find_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (find_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
}
