from PyWrite import File

# Define the document
document = File("doc.txt") # File Name*, Mode, Encoding
# Use the functions
document.write("Information") # Just like the "w" mode with open, overrides all content
document.add("More Information") # Just like the "a" mode with open, adds to the content
print(document.read()) # Just like the "r" mode with open, reads and returns the content