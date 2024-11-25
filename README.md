# Roadmap
## Sesión 1
- Motivación: enseñar algún ejemplo de qué se puede lograr con el exploiting: algún exploit chulo de kernel (escalada de privilegios: ejecutar un programa y obtener root) o de navegador (RCE: abrir una página web y que se abra una calculadora, o se ejecute una reverse shell). Quizás enseñar también a cuánto se puede vender un exploit de este tipo?
- Teoría básica: cómo funciona la CPU, ensamblador, registros, stack, syscalls, libc.
- Ghidra, GDB, desensamblador, binary ninja.
- Reto de reversing sencillito.

## Sesión 2
- Breve recordatorio de la stack.
- Explicación de buffer overflow.
- Explicación de representación de números en bytes, hexadecimal, little endian.
- Empezamos retos sin ninguna mitigación: no NX, no canary, ASLR desactivado a nivel de sistema.
- **Reto 1**: reto de sobreescribir variable local. El programa tiene un buffer overflow, y comprueba si la variable tiene un valor específico, y en ese caso llama a una función win() que lanza una shell. El atacante tendrá que explotar el buffer overflow para sobreescribir el valor de la variable local. La solución se hará primero de forma naive desde la shell:
	python -c 'print("A"*40 + valor_especifico)'
Y después se mostrará como hacerlo con un script de python usando pwntools, que para exploits más complejos nos será necesario, y permite debuggear de forma cómoda. A partir de este momento todos los exploits se harán con pwntools.
- Recordatorio de que en la stack no solo hay variables locales: también hay direcciones de retorno, y un atacante con un buffer overflow puede sobreescribirlas para redirigir el flujo de ejecución.
- **Reto 2**: mismo reto, pero esta vez el programa nunca llama a la función win(). El atacante tendrá que explotar el buffer overflow, pero esta vez para sobreescribir la dirección de retorno y poder llamar a win().

## Sesión 3
- Breve recordatorio de la sesión anterior: stack, buffer overflows, solución del último reto.
- Explicación de shellcode injection.
- **Reto 3**: mismo reto, pero esta vez el programa no tiene función win(). El atacante tendrá que incluir un shellcode en su payload, y sobreescribir la dirección de retorno con la dirección del shellcode para conseguir ejecución de código.
- Explicación de nuestra primera mitigación: NX (No eXecute). La stack no tiene permisos de ejecución hoy en día, lo cual mitiga la técnica de shellcode injection.
- Explicación de técnica: ROP (Return Oriented Programming). Es una técnica de tipo "code reuse": en vez de ejecutar código que inyectamos nosotros, ejecutamos código que ya está presente en el programa.
- Recordatorio de calling convention en x86-64: los argumentos de llamada a una función se pasan en los registros. Mostrar ejemplo en Compiler Explorer de función que recibe dos argumentos y los suma, y ver el desensamblado.
- **Reto 4**: reto de buffer overflow con función win(), pero esta vez con NX, y la función win() recibe dos argumentos y comprueba que se esté llamando con unos valores específicos. El atacante tendrá que explotar el buffer overflow y utilizar ROP para asignar los valores correctos a los registros antes de llamar a win().

## Sesión 4
- Breve recordatorio de la sesión anterior: shellcode injection, cómo NX mitiga esa técnica, y cómo ROP bypassea esa mitigación.
- **Reto 5**: reto de buffer overflow sin función win() y con NX. Como no hay ASLR, el atacante podrá usar ROP para llamar a la función system() de la libc.
- Explicación de nuestra segunda mitigación: ASLR (Address Space Layout Randomization). De momento aplicado sólo a las librerias (libc), pero no al propio binario.
- **Reto 6**: mismo reto sin función win() y con NX, pero además el sistema tiene ASLR activado (lo que impide utilizar ROP para llamar a funciones de la libc, ya que no sabemos sus direcciones) y el binario está compilado estáticamente (hay muchos gadgets para utilizar ROP). Este reto creo que lo mejor es hacerlo todos juntos. La idea es utilizar ROPgadget, una tool que te genera automáticamente una ROP chain que lanza una shell y que utiliza solo gadgets presentes en el binario. Mostrar que el código ejecutado mediante esta chain es muy similar al del shellcode que inyectamos en la sesión anterior. Pero esta vez no estamos inyectando nuestro código, sino que estamos reutilizando código presente en el binario.

## Sesión 5
- Explicación de nuestra tercera mitigación: stack canary.
- **Reto 7**: reto con stack canary y función win(). El programa pide una longitud N sin comprobarla, llama a fgets() para leer N bytes, y luego imprime esos N bytes. Esto tiene dos bugs: en primer lugar buffer overflow, ya que no comprueba la longitud. Pero no es explotable por sí sólo, ya que está el stack canary. En segundo lugar, vulnerabilidad de infoleak, ya que el atacante puede dar una longitud N y luego introducir menos bytes, pero el programa seguirá imprimiendo N bytes, que ahora incluirán la memoria de la stack que está a continuación de la entrada del usuario. El atacante debe utilizar esto para leakear el canary, y así poder explotar el buffer overflow.
- Recordatorio de ASLR y cómo bypassearlo, necesidad de un leak.
- **Reto 8**: mismo reto, pero sin función win(). Como hay ASLR, no podemos hacer directamente lo que hicimos en el reto 5, ya que no conocemos las direcciones de la libc. Además, el binario no está linkeado estáticamente y no tiene suficientes gadgets como para generar una ROP chain para conseguir RCE, como hicimos en el reto 6. El objetivo es aprovechar la vulnerabilidad de infoleak para leakear no sólo el canary, sino también una dirección de la libc y así bypassear ASLR y poder llamar a la función system() de la libc.

# TODO
- [ ] Mirar pwn.college, y anotar materiales para revisar antes de cada sesión y retos que se pueden resolver después de cada sesión. Quizás también retos de otros CTFs.
- [ ] Que una tercera persona pruebe a resolver los ocho retos propuestos aquí por su cuenta.

