#include <Python.h>

#define GET_TYPE(ob) (((PyObject *)(ob))->ob_type)
#define GET_ALLOCATED(ob) (((PyListObject *)(ob))->allocated)
#define Bytes_AS_STRING(op) (((PyBytesObject *)(op))->ob_sval)
#define GET_SIZE(ob) (((PyVarObject*)(ob))->ob_size)
#define GET_ITEM(op, i) (((PyListObject *)(op))->ob_item[i])
#define IS_BYTES(ob) (strcmp(GET_TYPE(ob)->tp_name, "bytes") == 0)

/**
 * print_python_bytes - prints some
 * basic info about Python bytes.
 *
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
    int min = 10, idx;

    printf("[.] bytes object info\n");

    if (IS_BYTES(p) != 1)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %lu\n", (GET_SIZE(p)));
    printf("  trying string: %s\n", Bytes_AS_STRING(p));

    if ((int)(GET_SIZE(p)) < min)
        min = ((int)(GET_SIZE(p))) + 1;
    
    printf("  first %d bytes:", min);
    for (idx = 0; idx < min; idx++)
        printf(" %02x", (unsigned char)(Bytes_AS_STRING(p))[idx]);
    printf("\n");
}

/**
 * print_python_list - prints some
 * basic info about Python lists.
 *
 * @p: python object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t len;
    int idx;
    PyTypeObject *temp;

    len = GET_SIZE(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %lu\n", len);
    printf("[*] Allocated = %lu\n", GET_ALLOCATED(p));

    for (idx = 0; (Py_ssize_t)idx < len; idx++)
    {
        temp = GET_TYPE(GET_ITEM(p, idx));
        printf("Element %d: %s\n", idx, temp->tp_name);

        if (IS_BYTES(GET_ITEM(p, idx)) == 1)
            print_python_bytes(GET_ITEM(p, idx));
    }
}
