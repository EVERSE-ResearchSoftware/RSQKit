## Format text files 

This folder contains Python code to format text files (mainly Markdown) so that one sentence goes on a single line. 

It contains: 
- Bash script (`reformat_files.sh`) that takes one or more text files as arguments, calls the Python script (`format_sentences.py`) on each, and replaces the original file with the reformatted version inplace (via a temporary file).
- Python script (`format_sentences.py`) to format text, preserving YAML front matter, code blocks, Markdown headers, tables and reference links, etc.

### Running the code

To make the Bash script executable, from the command line do: 

```bash
chmod +x reformat_files.py
```

To run the Bash script, for example on the Markdown files contained in the `pages` folder, do:

```bash
./reformat_files.sh ../../pages/*/*.md
```
