### Conditional filtering
One common approach is to use conditional statements to create boolean masks that
 indicate which rows satisfy the given conditions. For instance, you can use comparison 
operators such as greater than (`>`), less than (`<`), equal to (`==`), and logical operators 
like `and`, `or`, and `not` to define the conditions. Applying these conditions to the DataFrame 
using square brackets allows you to filter the data and obtain a subset that meets the 
specified criteria.

- Filtering with one or multiple сonditions:

  ```python
  # Filtering based on multiple conditions
  filtered_data = df[(df['column1'] > 10) & (df['column2'] == 'A')]
  ```
  This filters the DataFrame df to include only the rows where the values in column 'column1' 
  are greater than 10 and the values in column 'column2' are equal to 'A'. 
  The & operator is used for the logical 'and' operation.

  
- Filtering with String Methods:
You can use built-in string methods to filter strings such as `startswith`, `contains`, `endswith` and so on.
  ```python
  # Filtering based on string values
  filtered_data = df[df['column'].str.contains('apple', case=False)]
  ```
  This filters the DataFrame to include only the rows where the values in column 'column' 
  contain the substring 'apple'. The `str.contains()` method performs a case-insensitive search.


- Filtering with Negation:
  ```python
  # Filtering with negation
  filtered_data = df[~(df['column'] == 'A')]
  ```
  This filters the DataFrame to exclude the rows where the values in the 'column' 
  column are equal to 'A'. The `~` operator is used to negate the condition.


- Filtering with `isin()`:
  ```python
  # Filtering based on multiple values
  values_to_filter = ['A', 'B', 'C']
  filtered_data = df[df['column_name'].isin(values_to_filter)]
  ```
  This filters the DataFrame to include only the rows where the values in the column 
  'column_name' are present in the `values_to_filter` list.

## Task
You're required to filter the DataFrame such 
that it only retains entries fulfilling these specification:
1. `Age` is 60 or less.
2. `Name` starts with either "A" or "D".
3. `Surname` is not "Brown".
