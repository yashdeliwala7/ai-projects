# 📘 Linear Algebra for Machine Learning (Notes)

## 🔹 1. Vector

A **vector** is a list of numbers representing features.

**Example:**

```
[100, 50, 200]
```

👉 (clicks, users, revenue)

**Key Idea:**

* Dimension = number of elements
* `[x]` → 1D
* `[x, y]` → 2D
* `[x, y, z]` → 3D

---

## 🔹 2. Vector Operations

### ➤ Addition

Add element-wise:

```
[1, 2] + [3, 4] = [4, 6]
```

### ➤ Scalar Multiplication

Multiply each element:

```
2 × [3, 4] = [6, 8]
```

---

## 🔹 3. Dot Product ⭐

Formula:

```
[a, b] · [c, d] = (a×c) + (b×d)
```

**Example:**

```
[2, 3] · [4, 5] = 8 + 15 = 23
```

**Key Idea:**

* Result is a single number
* Measures similarity / relationship

**ML Use:**

* Predictions
* Neural networks
* Feature weighting

---

## 🔹 4. Matrix

A **matrix** is a table of numbers (dataset representation).

**Example:**

```
[
 [1, 2, 3],
 [4, 5, 6]
]
```

**Shape:**

```
(rows, columns) = (2, 3)
```

---

## 🔹 5. Matrix × Vector ⭐

Multiply each row of matrix with vector (dot product).

**Example:**

```
[
 [1, 2],
 [3, 4]
] × [5, 6]

= [
 (1×5 + 2×6),
 (3×5 + 4×6)
]

= [17, 39]
```

**ML Meaning:**

* Data × weights → prediction

---

## 🔹 6. Matrix × Matrix ⭐

### ➤ Rule

```
(A columns) = (B rows)
```

### ➤ Result Shape

```
(rows of A, columns of B)
```

### ➤ Example

```
A = [
 [1, 2],
 [3, 4]
]

B = [
 [5, 6],
 [7, 8]
]
```

### ➤ Calculation

```
[
 [ (1×5 + 2×7), (1×6 + 2×8) ],
 [ (3×5 + 4×7), (3×6 + 4×8) ]
]

= [
 [19, 22],
 [43, 50]
]
```

---

## 🔹 7. Important Patterns

```
(2×3) × (3×2) = (2×2)
(2×3) × (3×3) = (2×3)
```

---

## 🔥 ML Interpretation

* Vector → single data point
* Matrix → dataset
* Dot product → prediction score
* Matrix × Vector → model output
* Matrix × Matrix → transformations (deep learning)

---

## ⚡ Quick Summary

* Vector = features
* Matrix = data
* Dot product = weighted sum
* Matrix multiplication = core ML operation

---

## 🚀 Why it Matters in ML

Linear Algebra is used in:

* Linear Regression
* Neural Networks
* Recommendation Systems
* Computer Vision

👉 Almost every ML model depends on matrix operations.
