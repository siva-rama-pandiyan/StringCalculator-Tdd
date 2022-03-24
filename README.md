# StringCalculator-Tdd

Solved Using Python

### Below Test cases are Solved:-

1. The method can take up to two numbers, separated by commas, and will return their sum. (for an empty string it will return 0)
   For example “” or “1” or “1,2” as inputs.
   
2. Add method can also handle an unknown amount of numbers

3. Add method handles new lines between numbers.
    -> the following input is ok: “1\n2,3” (will equal 6)
    -> the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)

4. Support for different delimiters
    -> To change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” 
       for example “//;\n1;2” should return three where the default delimiter is ‘;’
       the first line is optional. all existing scenarios should still be supported

5. Calling Add with a negative number will throw an exception "negatives not allowed" - and the negative that was passed.

**Created Add Funtion to handle the above test cases step by step. You can check out the snippet at each commit.**
