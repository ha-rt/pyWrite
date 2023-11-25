# <img src="https://cdn.discordapp.com/attachments/1070174123159998495/1177845767721979984/pywrite.png?ex=6573fd5a&is=6561885a&hm=9838cc124631a8fd1dfcbd85c94fd62a67c0421f1576650557a15aa66adce701&">

A python module for easy file handling. Created for new users.

## How to use the module
```python
from PyWrite import File

# Define the document
document = File("doc.txt") # File Name*, Mode, Encoding
# Use the functions
document.write("Information") # Just like the "w" mode with open, overrides all content
document.add("More Information") # Just like the "a" mode with open, adds to the content
print(document.read()) # Just like the "r" mode with open, reads and returns the content
```
