all:
	lex compiler.l
	gcc lex.yy.c -o compiler -ll
	./compiler lex.ac

clean:
	rm -rf *.c
	rm -rf example0
	rm -rf example1
	rm -rf example2
	rm -rf example3
