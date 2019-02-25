#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <fcntl.h>
#include <string.h>

int MAXSIZE = 50;
int stack[50];
int top = -1;

int isempty()
{

    if (top == -1)
        return 1;
    else
        return 0;
}

int isfull()
{

    if (top == MAXSIZE)
        return 1;
    else
        return 0;
}

int peek()
{
    return stack[top];
}

int pop()
{
    int data;

    if (!isempty())
    {
        data = stack[top];
        top = top - 1;
        return data;
    }
    else
    {
        printf("Could not retrieve data, Stack is empty.\n");
    }
}

int push(int data)
{

    if (!isfull())
    {
        top = top + 1;
        stack[top] = data;
    }
    else
    {
        printf("Could not insert data, Stack is full.\n");
    }
}

int main()
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    char lastChar = '0';
    bool longComment = false;
    bool fail = false;
    bool singleQuote = false;
    bool doubleQuote = false;

    fp = fopen("hello.c", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1)
    {
        if (fail == false)
        {
            for (int i = 0; i < strlen(line); i++)
            {
                //printf("char: %c\n", line[i]);
                if (longComment == false && singleQuote == false && doubleQuote == false)
                {
                    if (line[i] == '(')
                    {
                        //printf("push (\n");
                        push(1);
                    }
                    else if (line[i] == '[')
                    {
                        //printf("push [\n");
                        push(3);
                    }
                    else if (line[i] == '{')
                    {
                        //printf("push {\n");
                        push(5);
                    }
                    else if (line[i] == ')')
                    {
                        //printf("pop )\n");
                        if (pop() != 1)
                        {
                            //printf("pop 1 false\n");
                            fail = true;
                        }
                    }
                    else if (line[i] == ']')
                    {
                        //printf("pop ]");
                        if (pop() != 3)
                        {
                            //printf("pop 3 false");
                            fail = true;
                        }
                    }
                    else if (line[i] == '}')
                    {
                        //printf("pop }");
                        if (pop() != 5)
                        {
                            //printf("pop 5 false");
                            fail = true;
                        }
                    }
                    else if (line[i] == '/')
                    { //detects line comments
                        if (lastChar == '/')
                        {
                            lastChar == '0';
                            break;
                        }
                        else
                        {
                            lastChar = '/';
                        }
                    }
                    else if (line[i] == '*')
                    { // Detects start of long comment
                        if (lastChar == '/')
                        {
                            //printf("Start Long Comment\n");
                            longComment = true;
                            lastChar = '0';
                        }
                    }
                    else if (line[i] == '\'')
                    { // detects single quotes
                        //printf("Start singleQuote\n");
                        singleQuote = true;
                    }
                    else if (line[i] == '\"')
                    { // Detects double quotes
                        //printf("Start doubleQuote\n");
                        doubleQuote = true;
                    }
                }
                else if (longComment == true)
                {
                    if (line[i] == '*')
                    { // Detects end of long comment
                        lastChar = '*';
                    }
                    else if (line[i] == '/' && lastChar == '*')
                    {
                        lastChar = '0';
                        longComment = false;
                        //printf("End long comment\n");
                    }
                }
                else if (singleQuote == true)
                {
                    if (line[i] == '\'')
                    {
                        singleQuote = false;
                        //printf("End single quote\n");
                    }
                }
                else if (doubleQuote == true)
                {
                    if (line[i] == '\"')
                    {
                        //printf("End double quote\n");
                        doubleQuote = false;
                    }
                }
            }
        }
    }

    if (longComment == true)
    {
        printf("Long Comment never ended\n");
    }
    if (singleQuote == true)
    {
        printf("SingleQuote never ended\n");
    }
    if (doubleQuote == true)
    {
        printf("DoubleQuote never ender\n");
    }

    if (fail == false)
    {
        printf("No errores de (), [] o {} desbalanceados\n");
    }
    else
    {
        printf("Parentesis irregulares\n");
    }

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);

    return 0;
}