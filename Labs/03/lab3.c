#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

int main(void)
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    char *token;

    int fd;
    fd = open("lex.out", O_WRONLY | O_CREAT);

    if (fd == -1)
    {
        printf("No se pudo crear lex.out\n");
    }

    fp = fopen("lex.ac", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1)
    {
        token = strtok(line, " ");
        while (token != NULL)
        {
            if (strlen(token) >= 2 && token[0] == '/' && token[1] == '/')
            {
                
            }
            else if (strcmp(token, "p") == 0)
            {
                printf("printf ");
                write(fd, "printf ", 7);
            }
            else if (strcmp(token, "+") == 0)
            {
                printf("plus ");
                write(fd, "plus ", 5);
            }
            else if (strcmp(token, "*") == 0)
            {
                printf("times ");
                write(fd, "times ", 6);
            }
            else if (strcmp(token, "-") == 0)
            {
                printf("minus ");
                write(fd, "minus ", 6);
            }
            else if (strcmp(token, "f") == 0)
            {
                printf("floatdcl ");
                write(fd, "floatdcl ", 9);
            }
            else if (strcmp(token, "i") == 0)
            {
                printf("intdcl ");
                write(fd, "intdcl ", 7);
            }
            else if (strcmp(token, "=") == 0)
            {
                printf("assign ");
                write(fd, "assign ", 7);
            }
            else
            {
                printf("id ");
                +write(fd, "id ", 3);
            }
            token = strtok(NULL, " ");
        }
        printf("\n");
        write(fd, "\n", 1);
    }
    write(fd, '\0', 1);
    close(fd);
    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}