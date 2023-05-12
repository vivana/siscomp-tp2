make: 
	nasm -f elf main.asm -o main.o
	gcc -m32 -shared -W conversor_C.c main.o -o libconversorc.so
	python2.7 cotiza.py

debug: 
	nasm -f elf main.asm -o main.o
	gcc -g -m32 -c -o conversor_C.o conversor_C.c
	gcc -g -m32 conversor_C.o main.o -o debug
	gdb debug

clean:
	rm *.o *.so

clean_debug: clean
	rm debug 
