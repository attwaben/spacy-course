# Import the English language class
from spacy.lang.en import english()

# Create the nlp object
nlp = english()

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)
