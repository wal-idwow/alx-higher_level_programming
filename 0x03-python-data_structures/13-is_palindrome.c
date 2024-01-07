#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of the list
 * Return: 1 if the list is a palindrome, 0 if not
*/
// check if the list is empty or has only element
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    // declare pointers for traversting the list
    listint_t *onestp = *head, *twostps = *head, *bfrone = NULL, *midl = NULL;
    int is_palindrome = 1;

    // move twostps twice as fast as onestp to find the middle of the list
    while (twostps != NULL && onestp->next != NULL)
    {
        twostps = twostps->next->next;

        bfrone = onestp;
        onestp = onestp->next;
    }

    if (twostps != NULL)
    {
        midl = onestp;
        onestp = onestp->next;
    }

    // reverse the second half of the list
    listint_t *second_half = reverse_list(onestp);
    listint_t *first_half = *head;

    // compare elements of the first and second halves
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }

        first_half = first_half->next;
        second_half = second_half->next;
    }

    // reverse the second half back to its original order
    reverse_list(midl);
    // connect the reversed second half to the first half
    bfrone->next = midl;

    return is_palindrome;
       
}

/**
 * reverse_list - reverse a linked list
 * @head: pointer to the head of the list
 * Return: pointer to new head of the reversed list
*/

listint_t *reverse_list(listint_t *head)
{
    listint_t *prv = NULL, *current = head, *next;

    // reverse the list by changing the dirction of pointers
    while (current != NULL)
    {
        next = current->next;
        current->next = prv;
        prv = current;
        current = next;
    }
    return prv;
}