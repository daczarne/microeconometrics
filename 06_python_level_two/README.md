# Scope

This idea of scope in your code is very important to understand in order toproperly assign and call variable names. In simple terms, the idea of scope can be described by 3 general rules:

1. Name assignments will create or change local names by default.  

1. Name references search (at most) four scopes, these are:  

    - local  
    - enclosing functions  
    - global  
    - built-in  

1. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.

## LEGB Rule

**L (Local)**: names assigned in any way within a function (def or lambda) are local to that function.

``` python
def report():
  x = "local"
  print(x)
```

Python will look for `x` first locally, in our function. If it can find it, that's the variable that it will use.

**E (Enclosing function locals)**: name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

``` python
x = "This is global level"

def enclosing():
  x = "Enclosing level"
  def inslide():
    print(x)
  inside()
```

If Python can't find a variable at the local level, it will look for it at the enclosing level (ie, in the "local" of the function that is calling it).

**G (Global (module))**: names assigned at the top-level of a module file, or declared global in a def within the file.

``` python
x = "This is global level"

def enclosing():
  def inslide():
    print(x)
  inside()
```

If it can't find the variable at the enclosing level either, then it will look for it at the Global level.

**B (Built-in (Python))**: names preassigned in the built-in names module: `open`, `range`, `sum`, etc.

---

IF we want to alter a global variable inside a function we use the `global` keyword.

``` python
x = "outside"
def enclosing():
  global x
  x = "inside"
```

If we need to have access to a global variable inside a function, just pass it as an argument.

``` python
x = "outside"
def enclosing(x):
  x = "inside"
  return x
```

# Decorators

Decorators can be thought of as functions which modify the "functionality" of another function.
