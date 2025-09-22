## Format text files 

This folder contains the code to format text files (we mainly have Markdown files) so that only one sentence is on a single line. 

It contains: 
- Bash script (`reformat_files.sh`) that takes one or more text files as arguments, calls the Python script (`format_sentences.py`) on each, and replaces the original file with the reformatted version inplace (via a temporary file).
- Python script (`format_sentences.py`)

### Running the code

To make the Bash script executable, from the command line do: `chmod +x format_sentences.py`.

To run the Bash script on the Markdown files in the `pages` folder of the project root, do:

```shell
./reformat_files.sh ../pages/*/*.md
```
