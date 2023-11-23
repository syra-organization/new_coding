# Modules

```
A Python module is a python file with .py extension including statement and definitions. It contains code that you can reuse in several programs

For Example: A file containing python code, demo.py is called a module, and its module name would be demo
```

### Syntax for importing 

1. import module_name
2. import module_name as alias_name
3. from module_name import var_name,f_name,....
4. from module_name import address as alias_name
5. from module_name import *

```
Example for module is in module folder
```

# Packages

```
Packages are the same as directory containing other sum-packages and modules in a structured way. making the sub-packages and modules easy to access

This is an analogy to a folder, as folders allow us to sotre files. Packages help us keep other sub-packages and modules to be used by the user when necessary
```

- The directory that contains the `__init__.py` file is defined as a python package

- A package must contain a special file with name `__init__.py`

- `__init__.py` file can be empty

- A package can be imported the same way as a module is imported

![image](https://pythongeeks.org/wp-content/uploads/2021/12/structure-of-packages.webp)

```
Example for package is in packages folder
```