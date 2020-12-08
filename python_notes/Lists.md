## Lists

```
colors = ['red', 'blue', 'green']
print colors[0]    ## red
print colors[2]    ## green
print len(colors)  ## 3
```

Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.
The "empty list" is just an empty pair of brackets [ ]. The '+' works to append two lists, so
 [1, 2] + [3, 4] yields [1, 2, 3, 4] (this is just like + with strings).
 
 #### FOR and IN
```
squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print sum  ## 30
```

The `in` construct on its own is an easy way to test if an element appears in a list
```
list = ['larry', 'curly', 'moe']
if 'curly' in list:
  print 'yay'
```

It is also possible to use for/in to work on a string.
The string acts like a list of its chars, so `for ch in s: print ch` prints all the chars in a string.

#### Range
The range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1, ... b-1 -- up to
 but not including the last number.

```
## print the numbers from 0 through 99
  for i in range(100):
    print i
```

#### While loop
```
## Access every 3rd element in a list
i = 0
while i < len(a):
  print a[i]
  i = i + 3
```

#### List methods

`list.append(elem)` - adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.  
`list.insert(index, elem)` - inserts the element at the given index, shifting elements to the right.  
`list.extend(list2)` - adds the elements in list2 to the end of the list. + or += is similar to using extend().  
`list.index(elem)` - searches for the given element from the start of the list and returns its index (throws ValueError if not present)  
`list.remove(elem)` - searches for the first instance of the given element and removes it (throws ValueError if not present)  
`list.sort()` - sorts the list in place. (The sorted() function shown later is preferred)  
`list.reverse()` - reverses the list in place (does not return it)  
`list.pop(index)` - removes and returns the element at the given index. Returns the rightmost element if index is omitted  

#### Sorting
The easiest way to sort is with the sorted(list) function
For more complex custom sorting, sorted() takes an optional "key=" specifying a "key" function that transforms each element before comparison.
The key function takes in 1 value and returns 1 value, and the returned "proxy" value is used for the comparisons within the sort.
```
strs = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']
```

Use a custom function
```
## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
  return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print sorted(strs, key=MyFn)  ## ['wa', 'zb', 'xc', 'yd']
```

To sort on 2 properties, is better to create a tuple from those properties.
when 2 tuples have the same element in the first position, it will sort based on the second.
In this case we need to write the `key=` function to return a tuple.
```
a=[(2,'a'),(1,'b'),(1,'a')]
sorted(a) # [(1,'a'),(1,'b'),(2,'a')]
```

```
a = ['aa', 'bb', 'cc']
':'.join(a) # aa:bb:cc
a.split(':') # ['aa', 'bb', 'cc']
```

####Tuples
A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate.
Tuples are like lists, except they are immutable and do not change size.
To create a tuple, just list the values within parenthesis separated by commas. The "empty" tuple is just an empty pair
 of parenthesis. Accessing the elements in a tuple is just like a list -- len(), [ ], for, in, etc. all work the same.
```
tuple = (1, 2, 'hi')
print len(tuple)  ## 3
print tuple[2]    ## hi
tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
tuple = ('hi',)   ## size-1 tuple. wierd syntax, but the comma is necessary to distinguish the tuple from a expression in parentheses.
```

Assigning a tuple to an identically sized tuple of variable names assigns all the corresponding values.
If the tuples are not the same size, it throws an error. This feature works for lists too.
```
(x, y, z) = (42, 13, "hike")
print z  ## hike
(err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple
```

#List Comprehensions
A list comprehension is a compact way to write an expression that expands to a whole list.
Suppose we have a list nums `[1, 2, 3, 4]` and we want to compute the square of each value:
```
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
```
The syntax is `[ expr for var in list ]`

```
## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]

## Select fruits containing 'a' and change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
## ['APPLE', 'BANANA']
```