# Test Cases

Run both cases separately. Calculate expected labor cost and total before each run.

From the repository folder, run:

```text
python 03_execution/freelance_quote_builder.py
```

For each case, paste the terminal input and output as evidence. Mark Pass or Fail and briefly explain why. A passing run has correct amounts, a cleaned client name, the `PROJECT ESTIMATE` heading, labeled costs, and dollars with two decimal places.

## Case 1: Ordinary values

Enter:

- Client name: `Alex Taylor`
- Estimated hours: `4`
- Hourly rate: `30`
- Direct expenses: `15`

**Expected labor cost and total:**
Laborcost: $120.0
Total estimate: $135.0
**Evidence (paste your terminal run):**

Project estimate
Client:Alex Taylor
Laborcost: $120.0
Direct expenses: $15
Total estimate: $135.0

```text

```

**Pass / Fail and why:** the estimated hours 4 * the hourly rate 30 when calulated the number for laborcost was $120.0 and the direct expenses 15 adding the total $135, making the program for the customer run passable.

## Case 2: Partial hours and text cleanup

Enter:

- Client name: `  aLEX tAYLOR  ` (include two spaces before and after the name)
- Estimated hours: `2.5`
- Hourly rate: `30`
- Direct expenses: `0`

The displayed name should be `Alex Taylor` without surrounding spaces.

**Expected labor cost and total:**

**Evidence (paste your terminal run):**


Project estimate
Client:Alex Taylor
client name: aLEX tAYLOR
estimated work hours: 2.5
hourly rate: 30
direct expenses: 0

Project estimate
Client:Alex Taylor
Laborcost: $75.0
Direct expenses: $0
Total estimate: $75.0

```text
client name: aLEX tAYLOR
estimated work hours: 2.5
hourly rate: 30
direct expenses: 0
project estimate
client:Alex Taylor
laborcost: $75.0
direct expenses: $0
total estimate: $75.0
```

**Pass / Fail and why:** The input must process the variable in order for the customer to run the output sucessfully. and it passed. when running the estimated work hours 2.5 * hourly rate of 30 had calculated laborcost exactly $75.0 and the direct expenses was $ 0 making the testing of the code complete to work.

If a case fails, fix the program and add evidence of the rerun below that case.


Pass: Has formatted and calculated inputs correctly 
