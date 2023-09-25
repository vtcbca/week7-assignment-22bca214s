
# ### Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products.

import pandas as pd
import csv
details=("product_sales.csv")
header=["Product No", "Product Name", "January", "February", "March", "April", "May", "June"]


# ### 1.Add 12 records tack input from user.¶

list = []
for i in range(12):
    prod_no = int(input("Enter Product Number: "))
    prod_name = input("Enter Product Name: ")
    jan = int(input("Enter Sales for January: "))
    feb = int(input("Enter Sales for February: "))
    mar = int(input("Enter Sales for March: "))
    apr = int(input("Enter Sales for April: "))
    may = int(input("Enter Sales for May: "))
    jun = int(input("Enter Sales for June: "))
    list.append([prod_no, prod_name, jan, feb, mar, apr, may, jun])


# ### 2.create dataframe.

df = pd.DataFrame(list)
df


# ### 3. Change Column Name Product No, Product Name, January, February, March, April, May, June.

# Change Column Names
df.header = ["Product No", "Product Name", "January", "February", "March", "April", "May", "June"]
df


# ### 4. Add column "Total Sell" to count total of all month and "Average Sell"

df["Total Sell"] = df["Total Sell"].astype(str)
df["Average Sell"] = df["Average Sell"].astype(str)
print(df)


# ### 5. Add 2 row at the end.

new_rows = {'Product No': '', 'Product Name': '', 'January': '', 'February': '', 'March': '', 'April': '', 'May': '', 'June': ''}
for i in range(2):
    for column in new_rows:
        new_rows[column] = input(f"Enter value for {column}: ")
df = df.append(new_rows, ignore_index=True)
df.reset_index(drop=True, inplace=True)
df


# ### 6. Add 2 row after 3rd row.

header=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June','Total Sell','Average Sell']
df.loc[2.5] = [5,"erte",46,352,45,46,657,567]
df = df.sort_index().reset_index(drop=True)
df.loc[3.5] = [6, 'moniter',1140,1148,2260,2245,2256,2221,11270,1878.333333]
df = df.sort_index().reset_index(drop=True)
df


# ### 7. Print first 5 row.

df.head()


# ### 8. Print Last 5 row.

df.tail()


# ### 9. Print row 6 to 10.

df.loc[6:10]


# ### 10. Print only product name

df=["product Name"]


# ### 11. Print sell of January month with product id and product name.

print(df[["Product No", "Product Name", "January"]])


# ### 12. Print only those product id , product name where january sell is > 5000 and February sell is >8000

df["January"] = pd.to_numeric(df["January"])
df["February"] = pd.to_numeric(df["February"])

df2 = df[(df["January"] > 5000) & (df["February"] > 8000)]

df2[["Product No", "Product Name"]]


# ### 13. Print record in sorting order of Product name.

df.sort_values(by="Product Name")


# ### 14. Display only odd index number column record.

df.iloc[1::2]


# ### 15. Display alternate row.
df.iloc[::2]





