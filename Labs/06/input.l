%{
#include <stdio.h>
%}

%%
\/\/.*                  /* ignore comments */ ;
f                       printf("floatdcl ");
i                       printf("intdcl ");
p                       printf("printf ");
=                       printf("assign ");
-                       printf("minus ");
\*                       printf("times ");
\/                       printf("divided by ");
\+                       printf("plus ");
[0-9]+                  printf("inum ");
[0-9]+\.[0-9]*          printf("fnum ");
[a-z]+                  printf("id");
\n                      printf("\n"); 
%%

int main(int argc, char **argv) {
    FILE    *fd;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyset_in(fd);
        yylex();
        fclose(fd);
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}

