# 📘 Probability for Machine Learning (Notes)

## 🔹 1. What is Probability?

Probability measures the **chance of an event happening**.

```text
0 → impossible  
1 → certain
```

---

## 🔹 2. Basic Formula

```text
P(A) = favorable outcomes / total outcomes
```

**Example (Dice):**

```text
Even numbers = {2, 4, 6}
Total outcomes = 6

P(even) = 3/6 = 1/2
```

---

## 🔹 3. Types of Events

### ➤ Independent Events

One event does NOT affect the other.

**Example:**

* Toss coin + roll dice

```text
P(A and B) = P(A) × P(B)
```

---

### ➤ Dependent Events

One event affects the other.

**Example:**

* Picking cards without replacement

---

## 🔹 4. Conditional Probability ⭐

Probability of A **given B has already happened**

```text
P(A | B) = P(A and B) / P(B)
```

---

### ➤ Example

* 100 people
* 40 are male
* 10 males bought product

```text
P(buy | male) = 10 / 40 = 1/4
```

---

## 🔹 5. Complement Rule

```text
P(not A) = 1 - P(A)
```

**Example:**

```text
P(head) = 0.5  
P(not head) = 0.5
```

---

## 🔹 6. Total Probability (Simple Idea)

If event can happen in multiple ways:

```text
Total probability = sum of all possibilities
```

---

## 🔹 7. Bayes' Theorem ⭐ (Important for ML)

```text
P(A | B) = [P(B | A) × P(A)] / P(B)
```

---

### ➤ Meaning

Update probability based on new information.

---

### ➤ Example (Simple Intuition)

* Disease test
* Test positive → probability of actually having disease changes

---

## 🔥 ML Use Cases

Probability is used in:

* Classification models
* Naive Bayes algorithm
* Spam detection
* Risk prediction
* Recommendation systems

---

## 🔹 8. Random Variables

A variable whose value depends on chance.

**Example:**

* Dice roll outcome
* Number of clicks

---

## 🔹 9. Distributions (Basic Idea)

Describe how data is spread.

### ➤ Common Types:

* Uniform distribution
* Normal distribution (bell curve)

---

## 🔹 10. Expected Value (Mean)

Average outcome over many trials.

```text
E(X) = Σ (value × probability)
```

---

## ⚡ Quick Summary

* Probability = chance
* Conditional = filtered chance
* Independent = no effect
* Dependent = affected
* Bayes = update belief
* Expected value = average

---

## 🚀 Why it Matters in ML

Used in:

* Predicting outcomes
* Measuring uncertainty
* Building probabilistic models
* Decision making

👉 Most ML models rely on probability to make predictions with confidence.
