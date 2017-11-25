# App 1 - Shell Interactive

This application is a standard example for shell based interactive application produced in python.

It is a simple dictionary producer, it takes vocabulary from [data.json](./data.json) and searches for word mentioned by user.

If word not found it prefers (if-any) word similar to that word and shows its meaning, this process is performed using *difflib* module.

## Usage

    $python dict.py
    Enter a Word : <word>
    1 meaning...
    2 another meaning...