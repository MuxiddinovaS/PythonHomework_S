import pandas as pd
 #Rename column names using function. "First Name" --> "first_name", "Age" --> "age
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

df.rename(columns={"First Name" : "first_name", "Age" : "age"})

#Print the first 3 rows of the DataFrame
df.head(3)
#Find the mean age of the individuals
mean_age = df["Age"].mean()

mean_age


#Select and print only the 'Name' and 'City' columns
df=[["first_name", "city"]]


#Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
import pandas as pd
ds = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(ds)

sales_and_expenses

#Calculate and display the maximum sales and expenses.
max_sales= sales_and_expenses['Sales'].max()
max_expenses= sales_and_expenses['Expenses'].max()

max_expenses

max_sales
#Calculate and display the minimum sales and expenses.
min_sales = sales_and_expenses['Sales'].min()
min_expenses= sales_and_expenses['Expenses'].min()


min_sales
min_expenses
#Calculate and display the average sales and expenses.

avg_sales= sales_and_expenses['Sales'].mean()
avg_expenses=sales_and_expenses['Expenses'].mean()


avg_sales
avg_expenses
#Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories.
import pandas as pd

data = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

expenses

#Calculate and display the maximum expense for each category.
expenses["Max_Expense"] = expenses[["January", "February", "March", "April"]].max(axis=1)
expenses[["Category", "Max_Expense"]]

#Calculate and display the minimum expense for each category.
expenses["Min_Expense"] = expenses[["January", "February", "March", "April"]].min(axis=1)

expenses[["Category", "Min_Expense"]]

#Calculate and display the average expense for each category.

expenses["Avg_Expense"] = expenses[["January", "February", "March", "April"]].mean(axis=1)

expenses[["Category", "Avg_Expense"]]
