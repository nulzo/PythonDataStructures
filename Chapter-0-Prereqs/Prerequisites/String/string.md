# Introduction to Strings

Taking a step back, let's just outline *what* a string is. A string, regardless of any language, is a collection of characters.
In plain english, it's a character, or a word, or a sentence, or a paragraph, etc., etc. So, the phrase "string" is a string, just
like "S" is a string (No, C developers, I won't call this a `char`), and "I like strings" is a string. Put simply, you can refer to 
any collection of characters as a string. In almost all languages, this is well-defined, and it is a core concept in programming.

Coming back to Python, strings are fundamental data types that represent sequences of characters. They provide a versatile 
way to work with textual information. Strings are immutable by nature, which means their values cannot 
be changed once they are created. In this section, we will briefly discuss how strings are used in Python.

### Initializing Strings

Unlike some languages, strings in Python can be defined using either single (' ') or double (" ") quotes. 
This flexibility allows for easy integration of quotes within strings. For example, strings can be defined in both ways 
shown below.

```python
single_quoted = 'This is a string.'
double_quoted = "This is also a string."
```

Triple quotes (`'''` or `"""`) allow the creation of multiline strings, which can span across multiple lines. Be careful,
however, as this also is used to denote a *doc string*, which is a string used for documentation purposes. An example of 
a multiline string can be seen below.

```python
triple_quoted = '''This
is an example of a multiline
string. It also can be mistaken as a 
docstring by some IDE's and developers!'''
```

However, I advise against using multiline strings whenever possible.

### Mutability
In Python, strings are *immutable*, which means their values cannot be changed once they are created. This immutability 
ensures that the content of a string remains fixed throughout its existence. When you perform operations on strings, 
such as concatenation or conversion to all lowercase characters, **new** strings are created rather than modifying the original ones!
This has *massive* implications in terms of performance! If you are reading this, I'd imagine that performant code is not
something that you are concerned about yet, but these operations can become expensive quickly, and it is good to make note
of the implications of such operations.

Let's take the following code:

```python
some_string = "hello"
some_string = some_string.upper()
```

I have intentionally made it appear as though the string `some_string` is being modified. I mean, I am even updating the 
variable! However, `upper()` does **not** change the original string, but it instead creates a *new* string with the uppercase version of "hello."

This provides certain advantages, such as simplicity in handling strings. 
It ensures that once a string is defined, its content remains consistent, reducing the risk of unintended changes. 
If you need to modify a string, you typically create a new one with the desired changes.

### Concatenation

String concatenation is the process of combining or joining two or more strings to create a longer string. In Python, we can
combine (concatenate) two string type objects by using the `+` operator. The example shown below concatenates two strings
that are stored in variables, and one string constant, to create the string "Hello, World!". Remember, this process creates
a *new* string object.

```python
some_string = "Hello,"
another_string = "World!"
concatenated_string = some_string + " " + another_string
```

### Indexing and Slicing

One of the most powerful features of Python strings is the ability to "slice" and "index" individual characters.
Much like a `list`, elements (characters) in a string can be accessed using indices. Slicing allows extracting a substring from a string.
In fact, in languages such as `C`, a string is just an array of characters!

```python
some_string = "Can you hear me?"
first_char = some_string[0]  # Stores "C"
substring = some_string[8:12]  # Stores "hear"
```

It is worth noting that string slicing is an exclusive operation, so the example above takes elements from 8, 9, 10, 11, but *not* 12.

