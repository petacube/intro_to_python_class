# Selecting data with MultiIndex
One advantage of accessing a DataFrame using a MultiIndex is that you can conveniently reference all levels at once (possibly excluding the inner levels) with an intuitive and familiar syntax.

* For columns selection, you can use the standard square brackets.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MultiIndex Selection Example</title>
<style>
  table {
    border-collapse: collapse;
    width: 50%;
    margin: 0 auto;
  }
  th, td {
    border: 1px solid black;
    padding: 5px;
    text-align: center;
  }
  th.sales, td.sales {
    background-color: #a6d09f;
    color: aliceblue;
  }
  th.offers, td.offers {
    background-color: #9ac8e3;
    color: aliceblue;
  }
</style>
</head>
<body>

<table>
  <tr>
    <td colspan="2"></td>
    <th colspan="2" style="color: aliceblue">df[<span style="background-color: #a6d09f">'Sales'</span>]</th>
    <td> </td>
    <th style="color: aliceblue">df[<span style="background-color: #9ac8e3">'Offers', 2022 </span>]</th>
  </tr>
  <tr>
    <th rowspan="2">City</th>
    <th rowspan="2">Category</th>
    <th colspan="2" class="sales">Sales</th>
    <th colspan="2" class="offers">Offers</th>
  </tr>
  <tr>
    <th class="sales">2021</th>
    <th class="sales">2022</th>
    <th>2021</th>
    <th class="offers">2022</th>
  </tr>
  <tr>
    <td>London</td>
    <td>Electronics</td>
    <td class="sales">5000</td>
    <td class="sales">7000</td>
    <td>50</td>
    <td class="offers">70</td>
  </tr>
  <tr>
    <td>London</td>
    <td>Clothing</td>
    <td class="sales">3000</td>
    <td class="sales">2000</td>
    <td>40</td>
    <td class="offers">20</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>Electronics</td>
    <td class="sales">6000</td>
    <td class="sales">7000</td>
    <td>70</td>
    <td class="offers">10</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>Electronics</td>
    <td class="sales">8000</td>
    <td class="sales">4000</td>
    <td>20</td>
    <td class="offers">70</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>Clothing</td>
    <td class="sales">4000</td>
    <td class="sales">5000</td>
    <td>30</td>
    <td class="offers">40</td>
  </tr>
  <tr>
    <td>Tokyo</td>
    <td>Electronics</td>
    <td class="sales">7000</td>
    <td class="sales">5000</td>
    <td>60</td>
    <td class="offers">50</td>
  </tr>
  <tr>
    <td>Tokyo</td>
    <td>Clothing</td>
    <td class="sales">2000</td>
    <td class="sales">1000</td>
    <td>80</td>
    <td class="offers">50</td>
  </tr>
</table>
</body>

* For rows and cells selection, you can use `.loc[]` syntax.

<table>
  <tr>
    <td rowspan="2"></td>
    <th rowspan="2">City</th>
    <th rowspan="2">Category</th>
    <th colspan="2">Sales</th>
    <th colspan="2">Offers</th>
  </tr>
  <tr>
    <th>2021</th>
    <th>2022</th>
    <th>2021</th>
    <th>2022</th>
  </tr>
  <tr>
    <th style="color: aliceblue">df.loc[<span style="background-color: #a6d09f">'London', 'Electronics'</span>]</th>
    <td class="sales">London</td>
    <td class="sales">Electronics</td>
    <td class="sales">5000</td>
    <td class="sales">7000</td>
    <td class="sales">50</td>
    <td class="sales">70</td>
  </tr>
  <tr>
    <td rowspan="4"></td>
    <td>London</td>
    <td>Clothing</td>
    <td>3000</td>
    <td>2000</td>
    <td>40</td>
    <td>20</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>Electronics</td>
    <td>6000</td>
    <td>7000</td>
    <td>70</td>
    <td>10</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>Electronics</td>
    <td>8000</td>
    <td>4000</td>
    <td>20</td>
    <td>70</td>
  </tr>
  <tr>
    <td>New York</td>
    <td>Clothing</td>
    <td>4000</td>
    <td>5000</td>
    <td>30</td>
    <td>40</td>
  </tr>
  <tr>
    <th rowspan="2" style="color: aliceblue">df.loc[<span style="background-color: #9ac8e3">'Tokyo'</span>]</th>
    <td class="offers">Tokyo</td>
    <td class="offers">Electronics</td>
    <td class="offers">7000</td>
    <td class="offers">5000</td>
    <td class="offers">60</td>
    <td class="offers">50</td>
  </tr>
  <tr>
    <td class="offers">Tokyo</td>
    <td class="offers">Clothing</td>
    <td class="offers">2000</td>
    <td class="offers">1000</td>
    <td class="offers">80</td>
    <td class="offers">50</td>
  </tr>
</table>

* Now, consider a situation where you want to select all cities in `Electronics` category or retain only the columns for 2022 year. 
Python syntax presents two restrictions in this case:

  1. There is no distinction between `df['a', 'b']` and `df[('a', 'b')]` in the way they are processed, so you can't simply use `df[:, 'Electronics']`. This is because Pandas cannot determine if you are referring to 'Electronics' as a column or as the second level of rows index.

  2. Python allows colons within square brackets, but not inside parentheses. Therefore, using `df.loc[(:, 'Electronics'), :]` is not possible.

### Task
Select all columns for the 2022 year (inner level) from the dataframe with column MultiIndex. 
You can use the [pandas.DataFrame.xs()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html) method or other workaround from the hint 2 below.

<div class="hint">
  Don't forget that year is in columns, so you need to choose the right axis.
</div>
<div class="hint">
  For a DataFrame with two levels, like the one we have here, you can use also the `pd.DataFrame.swaplevel()` method.
</div>
