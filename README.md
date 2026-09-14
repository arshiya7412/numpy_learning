# NumPy Learning
 
A collection of small NumPy exercises documenting core concepts I've learned and worked through in Google Colab. Each script is self-contained and focuses on one concept.
 
## 📂 Contents
 
| File | Concept |
|---|---|
| `matrix_addition.py` | Matrix/vector addition, broadcasting, and dot product |
| `matrix_transpose_shape.py` | Matrix transpose and shape manipulation |
| `mean_max_std.py` | Basic statistics: mean, max, standard deviation |
| `z-score.py` | Z-score standardization (feature scaling) |
 
## 🧠 Concepts Covered
 
### 1. Matrix Addition & Broadcasting
Adding matrices/vectors element-wise, adding a scalar to an entire array (broadcasting), and computing the dot product of two vectors.
 
### 2. Transpose & Shape
Flipping a matrix's rows and columns with `.T`, and inspecting array dimensions with `.shape` before and after the transpose.
 
### 3. Mean, Max & Standard Deviation
Core descriptive statistics using `np.mean()`, `np.max()`, and `np.std()` — the building blocks for understanding a dataset's central tendency and spread.
 
### 4. Z-Score Standardization
Rescaling data using:
 
```
z = (x - mean) / std
```
 
This transforms data to have a mean of 0 and standard deviation of 1, which is a common preprocessing step in machine learning so that no single feature dominates due to its scale.
 
## 🛠️ Tools Used
- Python
- NumPy
- Google Colab
## 🎯 Purpose
This repo is a personal reference for NumPy fundamentals, built while learning the basics for AI/ML and Data Science work.
 
