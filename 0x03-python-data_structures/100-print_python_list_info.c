#include <Python.h>

/**
  * print_python_list_info - prints basic info about Python lists
  * @p: PyObject list
*/
void print_python_list_info(PyObject *p)
{
    // declare variables to store list size, index, and memory allocated
    int size, index, allocated_memory;
    PyObject *element;

    // get the size and allocated memory of the Python list
    size = Py_SIZE(p);
    allocated_memory = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated_memory);

    // loop through each element in the list and print its type
    for (index = 0; index < size; index++)
    {
        printf("Element %d: ", index);

        // get the Python object at the specified index
        element = PyList_GetItem(p, index);

        printf("%s\n", Py_TYPE(element)->tp_name);
    }
}
