- [Introduction](#introduction)
- [Zen of Python](#zen-of-python)
- [How to Run Python Code](#how-to-run-python-code)
- [Python code syntax](#python-code-syntax)
- [Semantics](#semantics)
  - [Variables](#variables)
# Introduction

Conceived in the late 1980s as a teaching and scripting language, Python has since become an essential tool for many programmers, engineers, researchers, and data scientists across academia and industry.

The appeal of Python is in its simplicity and beauty, as well as the convenience of the large ecosystem of domain-specific tools that have been built on top of it. For example, most of the Python code in scientific computing and data science is built around a group of mature and useful packages:
• NumPy provides efficient storage and computation for multidi‐ mensional data arrays.
• SciPy contains a wide array of numerical tools such as numeri‐ cal integration and interpolation.
• Pandas provides a DataFrame object along with a powerful set of methods to manipulate, filter, group, and transform data.
• Matplotlib provides a useful interface for creation of publication-quality plots and figures.
• Scikit-Learn provides a uniform toolkit for applying common machine learning algorithms to data.

# Zen of Python

```python
In [1]: import this

The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules. Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess. There should be one--and preferably only one--obvious way
to do it.
Although that way may not be obvious at first unless
you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea--let's do more of those!

```

# How to Run Python Code

Python code is run using the Python interpreter.

# Python code syntax
Consider the following example:

```python
# set the midpoint 
midpoint = 5
# make two empty lists
lower = []; upper = []
# split the numbers into lower and upper
for i in range(10): 
  if (i < midpoint):
    lower.append(i) 
  else:
    upper.append(i) 
    
  print("lower:", lower)
  print("upper:", upper) 
  
# O/P:  
# lower: [0, 1, 2, 3, 4]
# upper: [5, 6, 7, 8, 9]

```

1. Comments are marked by #. Multi-line comments by using /* ... */
2. End-Of-Line terminates a statement `midpoint = 5 #end of line`
3. Semicolon can optionally Terminate a Statement
4. Indentation is used as a block of code
5. Whitespace *Within* Lines Does Not Matter
6. Parentheses Are for Grouping or Calling
    ```python
    In[5]:2*(3+4)
    Out [5]: 14


    In [6]: print('first value:', 1)
    first value: 1
    ```

# Semantics

## Variables

Python variables are pointers.

In many programming languages, variables are best thought of as containers or buckets into which you put data. So in C, for example, when you write

```c
// C code
int x = 4;
```

you are essentially defining a “memory bucket” named x, and putting the value 4 into it. In Python, by contrast, variables are best thought of not as containers but as pointers. So in Python, when you write
x=4
you are essentially defining a pointer named x that points to some other bucket containing the value 4. 