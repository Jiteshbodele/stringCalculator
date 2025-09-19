📘 String Calculator Test Suite
This project implements a simple string-based calculator function add(strng) that parses a string of numbers separated by delimiters and returns their sum. The accompanying unit tests ensure the function behaves correctly across various input scenarios.

<br><br>

✅ Function Overview
python
def add(strng: str) -> int
Accepts a string containing numbers separated by delimiters.

Default delimiters: comma , and newline \n.

Supports custom single-character delimiters using the format //<delimiter>\n.

Raises a ValueError if negative numbers are present.

<br><br>


🧪 Test Cases Explained
| Test Case Name            | Input String             | Expected Output  | Description                                                                 |
|---------------------------|--------------------------|------------------|-----------------------------------------------------------------------------|
| `test_empty_string`       | `""`                     | `0`              | Returns 0 for an empty string.                                              |
| `test_one_num`            | `"1"`                    | `1`              | Returns the number itself if only one is provided.                          |
| `test_two_nums`           | `"2,5"`                  | `7`              | Adds two comma-separated numbers.                                           |
| `test_arbitrary_nums`     | `"1,2,3,4,5,6,7,8,9"`    | `45`             | Adds multiple comma-separated numbers.                                      |
| `test_newline_delimeter`  | `"1,2,3\n4,5,6,7,8\n9"`  | `45`             | Supports newline `\n` as a valid delimiter.                                 |
| `test_change_delemeter`   | `"//;\n1;2;3"`           | `6`              | Supports custom delimiter `;` using the `//<delimiter>\n` format.           |
| `test_negative_nums`      | `"1,-2,-3"`              | `ValueError`     | Throws an error listing all negative numbers in the input.                  |


<br> <br>
⚠️ Error Handling
Negative Numbers: If any negative numbers are found, the function raises a ValueError with a message like:

ValueError: negative numbers are not allowed -2,-3

<br><br>

🛠️ How to Run Tests
Make sure you have Python installed. Then run:

python -m unittest testStringCal.py

<br><br>

📌 Notes
The function uses regular expressions to split the input string based on the specified delimiters.

Only single-character custom delimiters are supported.

The function assumes all inputs are valid integers unless negative.
