# Python-test_driven_development

 [ ] Task 0 

	python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
	
	python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
	
	python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l

 [ ] Task 1

	python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2

 [ ] Task 2

	python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2

 [ ] Task 3

	python3 -m doctest -v ./tests/4-print_square.txt

 [ ] Task4

	./5-main.py | cat -e

	python3 -m doctest -v ./tests/5-text_indentation.txt

 [ ] Task 5

	python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1

	head -7 tests/6-max_integer_test.py

 [ ] Task 6

	python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2

 [ ] Task 7

	python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 

 [ ] Task 8
	
	gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
	
	https://docs.python.org/3/howto/unicode.html
