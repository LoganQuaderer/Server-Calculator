# Server Tip Calculator

## Description

This Python script is designed to help servers calculate their tip distributions at the end of their shift. It performs the following functions:

1. Calculates tipouts for bussers and bar team based on total sales.
2. Determines if the house owes the server money or vice versa.
3. Adjusts final amounts owed by accounting for the busser tipout.

## Features

- **Input Total Sales**: The user inputs the total sales for the night.
- **Automatic Tipout Calculation**: 
  - Calculates 4% tipout for bussers
  - Calculates 2.5% tipout for the bar team
- **House Owed Money Calculation**:
  - Asks if the house owes the server money
  - If yes, calculates the final amount after subtracting the busser tipout
- **Error Handling**: 
  - Ensures valid input for yes/no questions
  - Validates numeric inputs for sales and amounts
- **Clear Output**: Provides formatted output for easy reading of monetary values

## How to Use

1. Run the script
2. Enter the total sales for the night when prompted
3. View the calculated tipouts for bussers and bar team
4. Answer whether the house owes you money (Y/N)
5. If yes, enter the amount the house owes
6. View the final calculation, which accounts for the busser tipout

## Note

This script assumes that the busser tipout is deducted from any amount the house owes the server. The final output will indicate whether the house still owes money, the server owes money, or if everything is settled.