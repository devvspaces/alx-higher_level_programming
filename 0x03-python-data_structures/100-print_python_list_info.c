#include <python3.4/Python.h>

/**
 * print_python_list_info - prints some
 * basic info about Python lists.
 *
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t len;
    int idx;
    PyTypeObject *temp;

    len = PyList_Size(p);
    printf("[*] Size of the Python List = %lu\n", len);
    printf("[*] Allocated = %lu\n", _PyList_CAST(p)->allocated);

    for (idx = 0; (Py_ssize_t)idx < len; idx++)
    {
        temp = Py_TYPE(PyList_GetItem(p, idx));
        printf("Element %d: %s\n", idx, temp->tp_name);
    }
}
