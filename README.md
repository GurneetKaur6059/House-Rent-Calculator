# House Expense Calculator

A simple command-line tool built with Python to help roommates or family members calculate their total monthly household expenses and split the cost evenly.

## Features

* **Calculate Total Expenses:** Sums up rent, food, electricity, and water bills.
* **Split Costs:** Divides the total expenses equally among the number of members.
* **Utility Calculation:** Includes a helper to estimate total electricity units consumed based on the bill and per-unit charge.
* **Safe Input:** Includes input validation to ensure only valid numbers are entered, preventing crashes.
* **Error Handling:** Safely handles division by zero (e.g., if 0 members are entered).

## How to Use

1.  **Clone or Download:**
    Get a copy of the script on your local machine.

2.  **Run the Script:**
    Open your terminal or command prompt, navigate to the project folder, and run:
    ```bash
    python your_script_name.py 
    ```
    *(Replace `your_script_name.py` with the actual name of your Python file.)*

3.  **Follow the Prompts:**
    The script will ask you to enter the following:
    * Total rent amount
    * Total food expenses
    * Total electricity bill
    * Charge per unit of electricity
    * Total water bill
    * Number of members

The script will then print a summary of the total expenses and the share per member.
