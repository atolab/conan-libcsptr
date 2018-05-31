#include <stdio.h>
#include <stdlib.h>

#include "csptr/smart_ptr.h"

static int result = EXIT_FAILURE;

static void
cleanup(void *ptr, void *meta)
{
    printf("cleanup\n");
    result = EXIT_SUCCESS;
}

static void
test(void)
{
    printf("test\n");
    smart int *i = unique_ptr(int, 42, cleanup);
}

int
main(int argc, char *argv[])
{
    printf("main\n");
    test();
    return result;
}
