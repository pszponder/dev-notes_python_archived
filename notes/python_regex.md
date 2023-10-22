# Regex in Python

Using regular expressions in Python requires the import of the `re` library

```python
# import the "re" library to enable use of regular expressions
import re

string = 'search inside of this text please!'

# Generate a match object
# return None if a match is not found
result = re.search('this', string)

print(result.span())  # return start and end index of match
print(result.start()) # return index of where the match starts
print(result.end())   # return index where match ends
print(result.group()) #
```

```python
import re

string = "search this inside of this text please!"

# Compile a regular expression pattern based on passed in string
pattern = re.compile("this")

# Return a match object
a = pattern.search(string)
print(a)  # <re.Match object; span=(7, 11), match='this'>

# Return a list of all matches
b = pattern.findall(string)
print(b)  # ['this', 'this']

# Determine if the passed in string is a full match to the pattern
# Returns a match object if the result matches the full match
# Returns "None" if result is not a full match
c = pattern.fullmatch(string)
print(c)  # None

# Match 0 or more characters at the beginning of the string
d = pattern.match(string)
print(d)  # Returns a match object if the result contains the pattern
```

## Resources / References

- [Regex Exercises](https://regexone.com/)
- [Regex101.com](https://regex101.com/)
- [Python Regex](https://www.w3schools.com/python/python_regex.asp)
- [Real Python - Regular Expressions - Part 1](https://realpython.com/regex-python/#regexes-in-python-and-their-uses)
- [Real Python - Regular Expressions - Part 2](https://realpython.com/regex-python-part-2/#re-module-functions)
