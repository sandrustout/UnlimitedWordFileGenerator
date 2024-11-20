
---

# Word File Generator

**Word File Generator** is a Python-based utility for creating customized wordlists. It allows users to generate a text file with all possible word combinations based on user-defined parameters, such as inclusion of uppercase letters, numerals, special characters, word length, and the total number of words.

This tool is perfect for penetration testers, researchers, or anyone needing a highly flexible wordlist generator.

---

## Features
- **Customizable Character Set**: Include lowercase, uppercase, numerals, and/or special characters.
- **Dynamic Word Length**: Minimum word length is configurable, with automatic scaling based on the number of words required.
- **High-Performance Generation**: Efficiently generates large wordlists up to billions of combinations.
- **Command-Line Interface**: Easily usable via command-line arguments.
- **File Size Reporting**: Provides the final size of the generated wordlist file.
- **Cross-Platform**: Compatible with Linux, macOS, and Windows.

---

## Installation

### 1. Install via `pip` (Recommended)
Make sure Python is installed on your system (Python 3.6+ recommended). Install the package directly from [PyPI](https://pypi.org/):

```bash
pip install wordfilegenerator
```

### 2. Install from Source
Clone this repository and install the package manually:
```bash
git clone https://github.com/sandrustout/unlimitedwordfilegenerator.git
cd unlimitedwordfilegenerator
python setup.py install
```

---

## Usage

### Command-Line Tool
After installation, the tool can be run using the `generatewordlist` command:

```bash
generatewordlist --filename <output_filename> [--caps] [--numerals] [--min-length <length>] --num-words <count>
```

#### Parameters:
- `--filename` (Required): Name of the output file (without `.txt` extension).
- `--caps` (Optional): Include uppercase letters in the wordlist.
- `--numerals` (Optional): Include numbers in the wordlist.
- `--min-length` (Optional): Minimum length of words (default: 8).
- `--num-words` (Required): Total number of words to generate.

#### Example:
Generate a wordlist named `testfile` containing 10,000 words with lowercase letters, uppercase letters, and numbers:
```bash
generatewordlist --filename testfile --caps --numerals --min-length 8 --num-words 10000
```

---

### Using as a Python Module
You can also use the tool programmatically in your Python scripts:

```python
from wordfilegenerator.main import create_word_list

create_word_list(
    filename="my_wordlist",
    caps="yes",
    numerals="yes",
    specials="no",
    num_words=1000,
    min_word_length=8,
)
```

---

## Example Output

A wordlist file (`output.txt`) with words like the following will be generated based on user specifications:
```
aaaaaaaa
aaaaaaab
aaaaaaac
...
```

The final message includes the size of the generated file in MB.

---

## FAQs

### 1. **Why is the `generatewordlist` command not recognized?**
Ensure that the package is installed correctly and is accessible in your environment. Try:
```bash
pip install wordfilegenerator --force-reinstall
```

### 2. **How large can the file be?**
The tool can generate up to billions of words, but the file size will depend on your storage capacity. A 1 billion-word list with 8-character words (including uppercase and numbers) is approximately **8.8 GB**.

### 3. **What happens if my word count exceeds character possibilities?**
The tool automatically adjusts the word length to accommodate the required number of words.

---

## Contributing

Contributions are welcome! If you encounter a bug or have a feature request, please open an issue or create a pull request on [GitHub](https://github.com/sandrustout/unlimitedwordfilegenerator).

---

## License

This project is licensed under the MIT License. See the `LICENSE.txt` file for details.

---

## Support

If you face any issues or have questions, feel free to reach out via the [GitHub Issues page](https://github.com/sandrustout/unlimitedwordfilegenerator/issues).

---
