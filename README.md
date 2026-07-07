# Contact Book

A command-line contact book built in Python. Users can add new contacts, 
look up a contact by name, and store everything in a dictionary — no 
external libraries required.

## Features
- **Look up** a contact's phone number by name
- **Add** a new contact (name + phone number)
- Comes pre-loaded with a few sample contacts (Ginger, Shelly, Isaiah)

## Concepts Practiced
- Functions and return values
- Dictionaries (storing and updating key-value pairs)
- Conditionals (`if` / `else`)
- User input handling

## How to Run
\`\`\`
python3 contactbook.py
\`\`\`

You'll be prompted to choose whether you want to look someone up or add a 
new contact.

## Known Limitations
- Contacts added during a session are **not saved** after the program closes — 
  everything resets to the original sample contacts each time you run it. 
  (Persisting data would require writing to a file, which isn't implemented yet.)

## About
Built as part of my Python fundamentals learning journey.
