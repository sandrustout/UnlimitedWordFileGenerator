**Flexible Word List Generator**
_**A Python script that generates a text file containing all possible combinations of words based on user-specified parameters. This tool is especially useful for generating large lists of words for brute-forcing, testing, and data generation needs**_.

**Features**
**Dynamic Word Length**: Starts with a minimum word length of 8 and increases automatically to meet the required number of unique words.
**Customizable Character Set**: Supports lowercase, uppercase, numerals, and special characters, with options to include or exclude each category.
**Efficient Memory Usage**: Uses generators to avoid memory issues and writes directly to the file as words are generated, handling large data requests smoothly.

# Unlimited Word File Generator
A Python-based tool to generate large wordlist files for custom needs. Useful for brute-forcing, testing, or other purposes.
- Customizable character sets (lowercase, uppercase, numerals).
- Adjustable word length and number of words.
- Outputs to a text file.

### Direct Download via `curl`
Run the following commands in your terminal:
curl -O https://raw.githubusercontent.com/sandrustout/unlimitedwordfilegenerator/main/main.py
chmod +x main.py
./main.py --filename wordlist --caps --numerals --min-length 8 --num-words 1000



**Usage**
**Clone the repository and navigate to the directory.**
_git clone <repo-url>
cd <repo-directory>_

**Run the script:**
_python generate_flexible_ordered_words.py_

**Input parameters:**
**Filename**: Base name of the output file (will be saved as <filename>.txt).
**Uppercase Letters**: Choose if words should include uppercase letters (yes or no).
**Numerals**: Choose if words should include numerals (yes or no).
**Special Characters**: Choose if words should include special characters (yes or no).
**Number of Words**: Specify the total number of words to generate.


**Example**
_Enter the filename (without .txt extension): wordlist
Should words contain uppercase letters? (yes or no): yes
Should words contain numerals? (yes or no): no
Should words contain special characters? (yes or no): no
How many words do you want to generate? 1000000
This will create a file named wordlist.txt containing 1,000,000 words, each composed of lowercase and uppercase letters only, and starting with words of length 8._

**_How It Works
Dynamic Character Pool: The script constructs a character pool based on the selected options (lowercase, uppercase, numerals, special characters)._**
Lexicographical Order: Words are generated in lexicographical order (e.g., aaaaaaaa, aaaaaaab).
Adaptive Length: Starting with 8 characters, the script increments the word length as needed to reach the desired number of words.
Efficient File Writing: To handle very large lists (millions or billions of words), the script writes each word to the file as it’s generated, ensuring minimal memory usage.
Requirements
Python 3.6 or higher
License
This project is open-source and available under the MIT License.
