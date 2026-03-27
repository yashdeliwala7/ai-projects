# NumPy Basics (Foundations for Machine Learning)

## 📌 What is NumPy?

NumPy (Numerical Python) is a Python library used for:

* Fast numerical computations
* Working with arrays and matrices
* Performing mathematical operations efficiently

It is the **core foundation** for libraries like Pandas, Scikit-learn, and TensorFlow.

---

## 📌 Why NumPy?

Python lists are:

* Slow for numerical operations
* Not optimized for math
* Do not support element-wise operations

NumPy provides:

* Faster performance (optimized in C)
* Built-in mathematical operations
* Support for multi-dimensional arrays

---

## 📌 Installing NumPy

```bash
pip install numpy
```

---

## 📌 Creating Arrays

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4])  # 1D array

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # 2D array
```

---

## 📌 Shape of Array

```python
print(arr1.shape)  # (4,)
print(arr2.shape)  # (2, 3)
```

* `(4,)` → 1D array with 4 elements
* `(2,3)` → 2 rows and 3 columns

---

## 📌 Important Concept: Indexing Starts from 0

```python
arr = np.array([
  [10, 20, 30],
  [40, 50, 60]
])
```

| Value | Index |
| ----- | ----- |
| 10    | [0,0] |
| 50    | [1,1] |
| 60    | [1,2] |

---

## 📌 Indexing

```python
arr[1,1]  # Output: 50
```

Format:

```
arr[row, column]
```

---

## 📌 Slicing

```python
arr[1, :]   # Full row → [40, 50, 60]
arr[:, 1]   # Full column → [20, 50]
arr[:, :]   # Whole array
```

👉 `:` means **select everything along that axis**

---

## 📌 Difference Between List and NumPy Array

```python
# Python list
[1,2,3] + [4,5,6]
# Output: [1,2,3,4,5,6]

# NumPy array
a = np.array([1,2,3])
b = np.array([4,5,6])

a + b
# Output: [5,7,9]
```

---

## 📌 Array Creation Rule (Very Important)

✅ Correct:

```python
np.array([[1,2,3], [4,5,6]])
```

❌ Incorrect:

```python
np.array([1,2,3], [4,5,6])
```

👉 NumPy expects **one argument (a structured list)**, not multiple lists.

---

## 📌 Shape Consistency Rule

All rows must have equal number of elements.

✅ Works:

```python
np.array([
  [1,2,3],
  [4,5,6]
])
```

❌ Error:

```python
np.array([
  [1,2,3,4],
  [5,6]
])
```

👉 Because rows are not equal length.

---

## 📌 Key Takeaways

* NumPy is used for fast numerical operations
* Arrays must have consistent shape
* Indexing starts from 0
* `:` is used for slicing
* Always pass a single structured list into `np.array()`

---

## 🚀 Next Step

* Broadcasting (automatic operations between arrays)
* Advanced slicing
* Mathematical operations

---
