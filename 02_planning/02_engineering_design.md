# Engineering Design

**Team members:**

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

*List each input and its Python data type.*
    Client name
    Estimated work hours
    Hourly rate
    Direct expenses

## Processing

*What calculations, text clean up, numberic converstions, next will the program perform on the inputs?*
    
    
    .strip().title() for text clean up
    hour rate * hours worked in float 
    materials = material cost
    hour rates * hours worked + material cost = total amount


```text

```

## Output

*What will the program display? How will you format it?*
    PROJECT ESTIMATE
    Client: 
    Labor cost: 
    Direct expenses: 
    Total estimate: 
## Functions

*Describe `main()` and at least one calculation function. For each, give its name, purpose, parameters, and returned result (or none).*

def name(nameFormat):
    - .strip().title() for text clean up
    - return

def main():

    Input functions:
    - Client name
    - Estimated work hours (float)
    - Hourly rate (float)
    - Direct expenses (int)

    Processing:
    - Estimated work hours * Hourly rate (labor cost for time to dollar calculation )
    - Direct expenses = Direct expenses (Materials used to dollar ratio)
    - Direct expenses + (Estimated work hours * Hourly rate) ((Total cost for time and materials ))

    Output: (f"{}") for $$$ sign
    PROJECT ESTIMATE
    Client: 
    Labor cost: $
    Direct expenses: $
    Total estimate: $