## Reading and Writing Files

You will, at some point, want to save your arrays to disk and load them back without having to 
re-run the code. Fortunately, there are several ways to save and load objects with NumPy.
`ndarray` objects can be saved to and loaded from disk files with [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt) 
and [`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt) functions, 
which handle normal text files. 

Let's say you have a file 'my_data.csv', which looks like this:
```text
id,value,size,amount
1,0.0660924327,8422,3
2,-0.2533106662,2738,9
3,0.1293063466,2925,10
4,-0.2420789913,1104,1
```
You can load it into a numpy array as follows:
```python
arr = np.loadtxt('my_data.csv', delimiter=',', skiprows=1)
```
You need to specify the delimiter and the number of rows that need to be skipped (header lines).

If there are missing values in your data, use [`numpy.genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt).
Let's say the above dataset does actually have a couple of missing values. 
```python
arr = np.genfromtxt('my_data.csv', delimiter=',', skip_header=1)
print(arr)
```
Output:
```text
[[ 6.60924327e-02  8.42200000e+03  3.00000000e+00]
 [            nan  2.73800000e+03  9.00000000e+00]
 [ 1.29306347e-01  2.92500000e+03  1.00000000e+01]
 [-2.42078991e-01             nan  1.00000000e+00]]
```
### Saving an array to a text file

[`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt) will help you with this.
Here are some examples:
```python
x = y = z = np.arange(0.0,5.0,1.0)
np.savetxt('test.out', x, delimiter=',')    # X is an array
np.savetxt('test.out', (x,y,z))   # x,y,z are equal sized 1D arrays
np.savetxt('test.out', x, fmt='%1.4e')   # use exponential notation
```
Output:
```text
#1:
0.000000000000000000e+00
1.000000000000000000e+00
2.000000000000000000e+00
3.000000000000000000e+00
4.000000000000000000e+00

#2:
0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00
0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00
0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00

#3:
0.0000e+00
1.0000e+00
2.0000e+00
3.0000e+00
4.0000e+00
```

### Task 
Read data from the file `somedata.csv` into the array `arr`.
Run the script to see the results and the saved file (`test.out`).

<div class="hint">There are missing values in the data.</div>
<div class="hint">Mind the extra lines at the top.</div>