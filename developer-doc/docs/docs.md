<h1 id="testmodule">testmodule</h1>


<h2 id="testmodule.b">b</h2>

```python
Breakfast.__call__(self)
```

This is `Breakfast.__call__()`.

<h2 id="testmodule.function_with_docstring_on_same_line">function_with_docstring_on_same_line</h2>

```python
function_with_docstring_on_same_line()
```
This is a pretty cool function.

__Arguments__

None actually.
__Example__

```python
# This is a very simple example.
mycoolfunction(samplesize, width, **options)
```
See also: `function_without_docstrings()`.
See also: [this page](https://keras.io/layers/convolutional/#conv2d) for
  the list of possible arguments.

<h2 id="testmodule.mycoolfunction">mycoolfunction</h2>

```python
mycoolfunction(samplesize, width=32, **options)
```

This is a pretty cool function.

__Arguments__

- __samplesize (int)__: Test sample size.
- __width (int)__: The width.
- __options__: Additional options.
__Example__

```python
# This is a very simple example.
mycoolfunction(samplesize, width, **options)
```
See also: `myothercoolfunction()`.

<h2 id="testmodule.myothercoolfunction">myothercoolfunction</h2>

```python
myothercoolfunction(prettycool, url)
```

Don't you think?
    # This is part of a code block and will not be transformed.
    Code here
```
# This is also part of a code block and will not be transformed.
More code here
```
__Parameters__

- __prettycool (any)__: Some parameter.
- __url (string)__: the url for this thing (default: 'http://localhost#foobar')

<h2 id="testmodule.add">add</h2>

```python
add(a, b)
```
Add two numbers.
__Arguments__

- __a (int)__: First number
- __b (int)__: Second number
__Example__

    assert add(2, 3) == 5
Simple as that.
Worth checking out: https://en.wikipedia.org/wiki/Addition#Properties

<h2 id="testmodule.Breakfast">Breakfast</h2>

```python
Breakfast(self, spam, eggs, ham=None)
```

This is a very simple class.
__Arguments__

- __spam (Spam)__: 200g of spam
- __eggs (Egg)__: 3 eggs
- __ham (Ham)__: As much ham as you like.

<h2 id="testmodule.rest_function">rest_function</h2>

```python
rest_function(a, b, c)
```

This function is documented using ReST Syntax.<br>
:param a: The first parameter.<br>
:param b: The second parameter.
:param c: The third parameter.
:raise RuntimeError: Maybe sometimes.
:return: Not much, really.

<h2 id="testmodule.ClassWithoutDocs">ClassWithoutDocs</h2>

```python
ClassWithoutDocs(self)
```

