all:
	gcc simple_foo.c -o simple_foo
	./simple_foo
	objdump -d ./simple_foo | less > logs

clean:
	rm -rf simple_foo
