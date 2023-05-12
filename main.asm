
;%include "./asm_io.inc"
;
; To create executable:
; Using djgpp:
; nasm -f coff sub4.asm
; nasm -f coff main4.asm
; gcc -o sub4 sub4.o main4.o driver.c asm_io.o
;
; Using Borland C/C++
; nasm -f obj sub4.asm
; nasm -f obj main4.asm
; bcc32 sub4.obj main4.asm driver.c asm_io.obj


segment .data

segment .bss

segment .text
        global  convert_asm

convert_asm:
        push ebp
        mov ebp, esp            ;Guardo valor original de ebp y cargo el valor de esp

        fld dword [ebp + 8]     ;cargo parametro 1 en unidad de punto flotante ST0
        fld dword [ebp + 12]    ;cargo parametro 2 en unidad de punto flotante ST1
        fmul ST1                ;ST0 = ST0 * ST1

        ;dump_regs 1             ; Imprime los valores de todos los registros 
        ;dump_stack 1, 2, 4      ; Imprime las posiciones de la pila y la informacion de cada registro

        pop ebp                 ;Restauro ebp y salgo
        ret





