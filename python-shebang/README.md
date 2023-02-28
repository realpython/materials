# Executing Python Scripts With a Shebang

This folder holds the code for the Real Python tutorial entitled [Executing Python Scripts With a Shebang](https://realpython.com/python-shebang/).

## Sample Scripts

### Python

Command:

```shell
$ ./hello.py
Hello, World!
```

### Perl

Command:

```shell
$ ./hello.pl
Hello, World!
```

### JavaScript

Command:

```shell
$ ./hello.js
Hello, World!
```

### Java

Command:

```shell
$ ./hello.j
Hello, World!
```

## Custom Interpreter

Install your custom interpreter of a popular [esoteric programming language](https://esolangs.org/wiki/Esoteric_programming_language) into a Python virtual environment:

```shell
$ cd interpreter/
$ python3 -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install .
```

Execute sample scripts through the esoteric language interpreter while using the virtual environment:

```shell
(venv) $ cd scripts/
```

### Towers of Hanoi

```shell
(venv) $ ./hanoi.b

                         Towers of Hanoi in Brainf*ck
              Written by Clifford Wolf <http://www.clifford.at/bfcpu/>

                     
                       
                         
                           
                                                             
                xXXXXXx                                        
      xXXXXXXXXXXXXXXXXXXXXXXXXXx                         xXx    
    xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx                 xXXXXXXXXXXXXXx
  xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx             xXXXXXXXXXXXXXXXXXx
  -----------------------------------     -----------------------------------





                                         
                                           
                                  xXXXXXXXXXx
                            xXXXXXXXXXXXXXXXXXXXXXx
                      -----------------------------------
```


### Sierpiński Triangle

```shell
(venv) $ ./sierpinski.b
                               *
                              * *
                             *   *
                            * * * *
                           *       *
                          * *     * *
                         *   *   *   *
                        * * * * * * * *
                       *               *
                      * *             * *
                     *   *           *   *
                    * * * *         * * * *
                   *       *       *       *
                  * *     * *     * *     * *
                 *   *   *   *   *   *   *   *
                * * * * * * * * * * * * * * * *
               *                               *
              * *                             * *
             *   *                           *   *
            * * * *                         * * * *
           *       *                       *       *
          * *     * *                     * *     * *
         *   *   *   *                   *   *   *   *
        * * * * * * * *                 * * * * * * * *
       *               *               *               *
      * *             * *             * *             * *
     *   *           *   *           *   *           *   *
    * * * *         * * * *         * * * *         * * * *
   *       *       *       *       *       *       *       *
  * *     * *     * *     * *     * *     * *     * *     * *
 *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```


### Factorial

```shell
(venv) $ ./factorial.b
1
1
2
6
24
120
720
5040
40320
362880
3628800
39916800
479001600
6227020800
87178291200
1307674368000
20922789888000
355687428096000
6402373705728000
121645100408832000
2432902008176640000
51090942171709440000
1124000727777607680000
25852016738884976640000
620448401733239439360000
15511210043330985984000000
403291461126605635584000000
10888869450418352160768000000
^C
```

### Fibonacci Sequence

```shell
(venv) $ ./fib.b
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
^C
```

### ROT-13

This is an interactive script that will expect you to provide input from your keyboard:

```shell
(venv) $ ./rot13.b 
This text will be encrypted.
Guvf grkg jvyy or rapelcgrq.
```

### Hello World

```shell
(venv) $ ./hello.b 
Hello World!
```
