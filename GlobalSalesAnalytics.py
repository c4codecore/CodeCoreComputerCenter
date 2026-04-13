import numpy as np

# --- TASK 1: DATA INFRASTRUCTURE (Topics 2, 3, 4, 5) ---
# Setting a seed ensures the "random" numbers are the same every time we run it
np.random.seed(42) 

# Creating a 3D array: 3 Years, 4 Quarters, 5 Products [Topic 3, 16]
# Values range from 50 to 500
sales_data = np.random.randint(50, 501, (3, 4, 5)) 

print("--- Task 1: Attributes & Setup ---")
print(f"Dimensions (ndim): {sales_data.ndim}") # [Topic 5]
print(f"Structure (shape): {sales_data.shape}") # [Topic 5]
print(f"Total elements (size): {sales_data.size}") # [Topic 5]

# Optimizing memory by converting to int32 [Topic 8]
sales_data = sales_data.astype(np.int32)
print(f"Data Type optimized to: {sales_data.dtype}\n")


# --- TASK 2: DATA CLEANING & SLICING (Topic 6) ---
print("--- Task 2: Cleaning & Slicing ---")
# Boolean Indexing: Filtering sales higher than 450 [Topic 6.8]
high_sales = sales_data[sales_data > 450]
print(f"Count of High-Performance Sales (>450): {high_sales.size}")

# Slicing: Extracting all data for Year 1 [Topic 6.4]
year_1_data = sales_data[0, :, :] 
print(f"Year 1 Data extracted with shape: {year_1_data.shape}")

# Negative Indexing: Accessing the very last product entry [Topic 6.7]
last_entry = sales_data[-1, -1, -1]
print(f"Value of the final product entry: {last_entry}\n")


# --- TASK 3: OPERATIONS & BROADCASTING (Topics 9, 12, 15) ---
print("--- Task 3: Operations & Broadcasting ---")
# Broadcasting: Adding a flat ₹10 tax to every single value [Topic 15]
taxed_sales = sales_data + 10 
print("Applied ₹10 Logistics Tax using Broadcasting.")

# Universal Function (ufunc): Calculating Square Root [Topic 10]
growth_curve = np.sqrt(sales_data)

# Aggregation: Calculating the Running Total (Cumulative Sum) [Topic 12.3]
running_total = np.cumsum(sales_data)
print(f"Total sales volume achieved to date: {running_total[-1]}\n")


# --- TASK 4: STRUCTURAL TRANSFORMATION (Topics 7, 14) ---
print("--- Task 4: Transformation & Joining ---")
# Reshaping: Converting 3D data into a 2D table (12 Quarters x 5 Products) [Topic 7.1]
sales_2d = sales_data.reshape(12, 5)
print(f"Reshaped 3D data into 2D table: {sales_2d.shape}")

# Joining: Adding data for 5 new products using vstack [Topic 14.3]
new_products = np.random.randint(50, 501, (1, 5))
extended_sales = np.vstack((sales_2d, new_products))

# Transpose: Flipping rows and columns for a product-centric view [Topic 7.4]
product_view = extended_sales.T
print(f"Transposed table shape: {product_view.shape}\n")


# --- TASK 5: ADVANCED ANALYTICS (Topic 11, 13) ---
print("--- Task 5: Advanced Analytics ---")
# Statistical Analysis: Average sales per quarter (axis=1 means row-wise) [Topic 11.8]
quarterly_mean = np.mean(sales_2d, axis=1)
print(f"Average sales for first 3 quarters: {quarterly_mean[:3]}")

# Searching: Finding indices where sales are critically low (< 100) [Topic 13.3]
low_sales_indices = np.where(sales_2d < 100)
print(f"Identified {len(low_sales_indices[0])} instances of low sales.")

# Feature Scaling: Min-Max Normalization (Scaling data between 0 and 1) [Topic 11]
s_min, s_max = sales_2d.min(), sales_2d.max()
normalized_sales = (sales_2d - s_min) / (s_max - s_min)
print("Data successfully normalized for Machine Learning readiness.\n")


# --- TASK 6: EXPORT & STORAGE (Topic 17) ---
# Saving as a NumPy Binary file (.npy) for fast loading [Topic 17.1]
np.save("processed_sales_data.npy", sales_2d)

# Saving as a CSV for use in Excel/Pandas [Topic 17.3]
np.savetxt("global_sales_report.csv", sales_2d, delimiter=",", header="P1,P2,P3,P4,P5", comments='')

print("--- Project Successfully Completed & Files Saved ---")