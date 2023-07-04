#include "Python.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * print_python_string - prints information
 * about a python string
 *
 * @p: pointer to the string object,
 * checks to see it is string
 */
void print_python_string(PyObject *p)
{
    char *unicode_type = "compact unicode object";
    char *ascii_type = "compact ascii";
    char *str = NULL, *encoding_type = NULL;
    ssize_t str_len = 0;
    int i;
    PyObject *str_ob = NULL;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    str_len = (ssize_t)PyUnicode_GET_LENGTH(p);

    str_ob = PyUnicode_AsUTF8String(p);
    str = PyBytes_AsString(str_ob);

    for (i = 0; i < str_len; i++)
        if (str[i] < 0)
        {
            encoding_type = unicode_type;
            break;
        }

    if (encoding_type == NULL)
        encoding_type = ascii_type;

    printf("  type: %s\n", encoding_type);
    printf("  length: %ld\n", str_len);
    printf("  value: %s\n", str);
}
