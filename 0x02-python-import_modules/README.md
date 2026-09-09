# Python - Import & Modules 🐍

A collection of Python exercises focused on **imports, modules, functions, command-line arguments, and basic arithmetic operations**.

This project is part of the **ALX Higher Level Programming** curriculum and introduces fundamental concepts for organizing and reusing Python code.

## 📌 Project Description

In this project, I learned how to:

* Import functions and variables from Python modules.
* Create and use custom Python modules.
* Use the built-in `dir()` function.
* Work with command-line arguments using `sys.argv`.
* Perform arithmetic operations using imported functions.
* Understand how Python modules are structured and reused.
* Write executable Python scripts.
* Work with Python bytecode and reproduce its behavior.
* Follow specific coding constraints while solving programming challenges.

The exercises gradually build familiarity with Python's module system and command-line programming.

## 🛠️ Requirements

The project was developed using:

* **Python 3**
* Ubuntu/Linux environment
* Shell / Bash
* Git and GitHub

### Python Version

```bash
python3 --version
```

Python 3 is required to run the scripts in this project.

### File Permissions

Some scripts are designed to be executed directly. If necessary, make them executable with:

```bash
chmod +x *.py
```

## 📂 Repository Structure

```text
0x02-python-import_modules/
│
├── 0-add.py
├── 1-calculation.py
├── 2-args.py
├── 3-infinite_add.py
├── 4-hidden_discovery.py
├── 5-variable_load.py
├── 100-my_calculator.py
├── 101-easy_print.py
├── 102-magic_calculation.py
├── 103-fast_alphabet.py
│
├── add_0.py
├── calculator_1.py
├── variable_load_5.py
├── hidden_4.pyc
│
└── README.md
```

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/Tolulope05/alx-higher_level_programming.git
```

Navigate to the project directory:

```bash
cd alx-higher_level_programming/0x02-python-import_modules
```

Run a Python script using:

```bash
python3 <filename>.py
```

For executable scripts, you can also use:

```bash
./<filename>.py
```

### Example

Run the simple addition program:

```bash
./0-add.py
```

Expected output:

```text
1 + 2 = 3
```

Run the calculator:

```bash
./100-my_calculator.py 10 + 5
```

Expected output:

```text
10 + 5 = 15
```

Run the command-line arguments program:

```bash
./2-args.py hello world
```

## 📚 Tasks

### 0. Import a simple function from a simple file

[`0-add.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/0-add.py)

Imports the `add(a, b)` function from [`add_0.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/add_0.py) and prints the result of adding `1` and `2`.

**Expected output:**

```text
1 + 2 = 3
```

---

### 1. My first toolbox!

[`1-calculation.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/1-calculation.py)

Imports arithmetic functions from [`calculator_1.py`](https://github.com/OssamaSabihi/high_level_programming/blob/main/0x02-python-import_modules/calculator_1.py) and performs addition, subtraction, multiplication, and division on `10` and `5`.

---

### 2. How to make a script dynamic!

[`2-args.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/2-args.py)

Uses command-line arguments to display the number of arguments passed to the program and their values.

**Example:**

```bash
./2-args.py hello world
```

---

### 3. Infinite addition

[`3-infinite_add.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/3-infinite_add.py)

Adds all command-line arguments and prints their total.

**Example:**

```bash
./3-infinite_add.py 10 20 30
```

**Expected output:**

```text
60
```

---

### 4. Who are you?

[`4-hidden_discovery.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/4-hidden_discovery.py)

Uses the compiled module `hidden_4.pyc` to discover and print all names defined in the module.

The names are:

* Printed in alphabetical order.
* Printed one per line.
* Names beginning with `__` are excluded.

---

### 5. Everything can be imported

[`5-variable_load.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/5-variable_load.py)

Imports the variable `a` from [`variable_load_5.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/variable_load_5.py) and prints its value.

---

### 6. Build my own calculator!

[`100-my_calculator.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/100-my_calculator.py)

Builds a command-line calculator by importing arithmetic functions from [`calculator_1.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/calculator_1.py).

**Usage:**

```bash
./100-my_calculator.py <a> <operator> <b>
```

Supported operators:

| Operator | Operation      |
| :------: | -------------- |
|    `+`   | Addition       |
|    `-`   | Subtraction    |
|    `*`   | Multiplication |
|    `/`   | Division       |

**Example:**

```bash
./100-my_calculator.py 10 + 5
```

**Output:**

```text
10 + 5 = 15
```

If an invalid operator is provided:

```text
Unknown operator. Available operators: +, -, *, and /
```

The program exits with status `1`.

If the number of arguments is incorrect:

```text
Usage: ./100-my_calculator.py <a> <operator> <b>
```

The program exits with status `1`.

---

### 7. Easy print

[`101-easy_print.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/101-easy_print.py)

Prints:

```text
#pythoniscool
```

The solution must not use:

* `print`
* `eval`
* `open`
* `sys`

---

### 8. ByteCode → Python #3

[`102-magic_calculation.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/102-magic_calculation.py)

Implements a Python function that reproduces the behavior of a provided bytecode.

This exercise provides practice with:

* Python bytecode.
* Functions.
* Conditional expressions.
* Arithmetic operations.
* Understanding how Python code is interpreted.

---

### 9. Fast alphabet

[`103-fast_alphabet.py`](https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x02-python-import_modules/103-fast_alphabet.py)

Prints the uppercase English alphabet followed by a new line.

The solution must not use:

* Loops
* Conditionals
* `str.join()`
* String literals
* System calls

## 🎯 Learning Objectives

By completing this project, I strengthened my understanding of:

* Python modules and imports.
* Function reuse.
* Command-line arguments.
* The `sys.argv` list.
* The `dir()` built-in function.
* Executable Python scripts.
* Basic exception and error handling.
* Python bytecode.
* Writing solutions under strict programming constraints.

## 🧪 Testing

Each script can be tested directly from the command line.

For example:

```bash
./0-add.py
./2-args.py
./3-infinite_add.py 1 2 3
./100-my_calculator.py 10 + 5
```

You can also run scripts explicitly with Python:

```bash
python3 0-add.py
python3 2-args.py
python3 3-infinite_add.py 1 2 3
python3 100-my_calculator.py 10 + 5
```

## 📖 Resources

Useful Python documentation:

* [Python Documentation](https://docs.python.org/3/)
* [Python Modules](https://docs.python.org/3/tutorial/modules.html)
* [Python Command-Line Arguments](https://docs.python.org/3/library/sys.html)
* [Python Built-in Functions](https://docs.python.org/3/library/functions.html)


⭐ If you find this project useful, feel free to explore the rest of the repository.
