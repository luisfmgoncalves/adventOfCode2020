## Strings

Python has a built-in string class named "str" with many handy features.

```
s = 'hi'
print s[1]          ## access the character in position 1 which is i
print len(s)        ## access the string length which is 2
print s + ' there'  ## concatenate strings: 'hi there'
```

Unlike Java, the '+' does not automatically convert numbers or other types to string form.
The str() function converts values to a string form so they can be combined with other strings.

```
pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  ## yes
```

A "raw" string literal is prefixed by an 'r' and passes all the chars through without special treatment of backslashes,
 so r'x\nx' evaluates to the length-4 string 'x\nx'. A 'u' prefix allows you to write a unicode string literal
 
```
raw = r'this\t\n and that'
print raw #prints: this\t\n and that

multi = """It was the best of times. It was the worst of times."""
print multi #prints: It was the best of times. It was the worst of times.  
```

Comprehensive list of string methods in [here](https://docs.python.org/3/library/stdtypes.html#string-methods)

####String Slices

The "slice" syntax is a handy way to refer to sub-parts of sequences -- typically strings and lists. 
```
 H  e  l  l  o
 0  1  2  3  4
-5 -4 -3 -2 -1
```

```
s = 'Hello'
s[1:4] #chars starting at index 1 and extending up to but not including index 4 : 'ell'
s[1:] # omitting either index defaults to the start or end of the string : 'ello'
s[:] # omitting both always gives us a copy of the whole thing (copy a sequence like a string or list in python) : Hello
s[-1] # last char (1st from the end) : 'o'
s[-4] # 4th from the end: 'e'
s[:-3] # going up to but not including the last 3 chars: 'He'
s[-3:] # starting with the 3rd char from the end and extending to the end of the string: 'llo'

s[:n] + s[n:] == s
```

####String %
he % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point),
 and the matching values in a tuple on the right
 
```
text = (
  "%d little pigs come out, "
  "or I'll %s, and I'll %s, "
  "and I'll blow your %s down."
  % (3, 'huff', 'puff', 'house'))
```

####if statement
Python does not use { } to enclose blocks of code for if/loops/function etc.. Instead, Python uses the colon (:) 
 and indentation/whitespace to group statements.
 
```
if speed >= 80:
  print 'License and registration please'
  if mood == 'terrible' or speed >= 100:
    print 'You have the right to remain silent.'
  elif mood == 'bad' or speed >= 90:
    print "I'm going to have to write you a ticket."
    write_ticket()
  else:
    print "Let's try to keep it under 80 ok?"
```