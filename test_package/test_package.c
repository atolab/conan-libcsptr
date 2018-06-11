#include <stdio.h>
#include <stdlib.h>

#include "csptr/smalloc.h"

static int result = EXIT_FAILURE;

static void
destructor(void *ptr, void *meta)
{
    (void)ptr;
    (void)meta;

    result = EXIT_SUCCESS;
}

int
main(int argc, char *argv[])
{
    int *foobar = smalloc(.size = sizeof(int), .dtor = &destructor);
    sfree(foobar);
    return result;
}
