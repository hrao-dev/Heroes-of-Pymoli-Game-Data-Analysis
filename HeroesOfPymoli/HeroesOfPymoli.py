# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

# Determine Player Count and display the total number of players
total_players = purchase_data["SN"].unique()
player_count = pd.DataFrame({
    'Total Players': [len(total_players)]
    })
#print(player_count)
display(player_count)

#Purchasing Analysis (Total)
#Run basic calculations to obtain number of unique items, average price, etc.
#Create a summary data frame to hold the results
#Optional: give the displayed data cleaner formatting
#Display the summary data frame

unique_items = purchase_data["Item ID"].unique()
unique_items_count = len(unique_items)
avg_price = round(purchase_data["Price"].mean(),2)
total_purchases = len(purchase_data["Purchase ID"])
total_revenue = purchase_data["Price"].sum()
purchase_an_total = pd.DataFrame({
    'Number of Unique Items': [unique_items_count],
    'Average Price': [avg_price],
    'Number of Purchases': [total_purchases],
    'Total Revenue': [total_revenue]
})
purchase_an_total['Average Price'] = purchase_an_total['Average Price'].map("${:.2f}".format)
purchase_an_total['Total Revenue'] = purchase_an_total['Total Revenue'].map("${:,.2f}".format)
#print(purchase_an_total)
display(purchase_an_total)

#Gender Demographics
#Percentage and Count of Male Players
#Percentage and Count of Female Players
#Percentage and Count of Other / Non-Disclosed

gender_demo = purchase_data.groupby(['SN','Gender']).size()
gender_demo = gender_demo.groupby('Gender').size().reset_index(name='count')
gender_demo = gender_demo.sort_values('count',ascending=False)
gender_demo.rename(columns = {'count':'Total Count'}, inplace = True)
gender_demo['Percentage of Players'] =  gender_demo['Total Count'] / gender_demo['Total Count'].sum()
gender_demo['Percentage of Players'] = gender_demo['Percentage of Players'].map("{:.2%}".format)
gender_demo = gender_demo.set_index('Gender')
#print(gender_demo)
display(gender_demo)

#Purchasing Analysis (Gender)
#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
#Create a summary data frame to hold the results
#Optional: give the displayed data cleaner formatting
#Display the summary data frame

df1 = purchase_data.groupby('Gender').size().reset_index(name='count')
df1.rename(columns = {'count':'Purchase Count'}, inplace = True)
df2 = purchase_data.groupby('Gender', as_index=False)['Price'].mean()
df2.rename(columns = {'Price':'Average Purchase Price'}, inplace = True)
df3 = purchase_data.groupby('Gender', as_index=False)['Price'].sum()
df3.rename(columns = {'Price':'Total Purchase Value'}, inplace = True)
df4 = purchase_data.groupby(['SN','Gender'],as_index=False)['Price'].sum()
df5 = df4.groupby('Gender',as_index=False)['Price'].mean()
df5.rename(columns = {'Price':'Avg Total Purchase per Person'}, inplace = True)
gender_purchase = pd.merge(left=df1, right=df2)
gender_purchase = pd.merge(left=gender_purchase, right=df3)
gender_purchase = pd.merge(left=gender_purchase, right=df5)
gender_purchase['Average Purchase Price'] = gender_purchase['Average Purchase Price'].map("${:.2f}".format)
gender_purchase['Total Purchase Value'] = gender_purchase['Total Purchase Value'].map("${:,.2f}".format)
gender_purchase['Avg Total Purchase per Person'] = gender_purchase['Avg Total Purchase per Person'].map("${:.2f}".format)
gender_purchase = gender_purchase.set_index('Gender')
#print(gender_purchase)
display(gender_purchase)

#Age Demographics
#Establish bins for ages
#Categorize the existing players using the age bins. Hint: use pd.cut()
#Calculate the numbers and percentages by age group
#Create a summary data frame to hold the results
#Optional: round the percentage column to two decimal points
#Display Age Demographics Table

max_age = purchase_data["Age"].max()
data_copy = purchase_data.copy()
data_copy['Age_Ranges'] = pd.cut(x=data_copy['Age'], bins=[0,9,14,19,24,29,34,39,max_age], labels=['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+'])
age_demo = data_copy.groupby(['SN','Age_Ranges']).size()
age_demo = age_demo.groupby('Age_Ranges').size().reset_index(name='count')
age_demo.rename(columns = {'count':'Total Count'}, inplace = True)
age_demo['Percentage of Players'] =  age_demo['Total Count'] / age_demo['Total Count'].sum()
age_demo['Percentage of Players'] = age_demo['Percentage of Players'].map("{:.2%}".format)
age_demo = age_demo.set_index('Age_Ranges')
#print(age_demo)
display(age_demo)

#Purchasing Analysis (Age)
#Bin the purchase_data data frame by age
#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
#Create a summary data frame to hold the results
#Optional: give the displayed data cleaner formatting
#Display the summary data frame

ag_df1 = data_copy.groupby('Age_Ranges').size().reset_index(name='count')
ag_df1.rename(columns = {'count':'Purchase Count'}, inplace = True)
ag_df2 = data_copy.groupby('Age_Ranges', as_index=False)['Price'].mean()
ag_df2.rename(columns = {'Price':'Average Purchase Price'}, inplace = True)
ag_df3 = data_copy.groupby('Age_Ranges', as_index=False)['Price'].sum()
ag_df3.rename(columns = {'Price':'Total Purchase Value'}, inplace = True)
ag_df4 = data_copy.groupby(['SN','Age_Ranges'],as_index=False)['Price'].sum()
ag_df5 = ag_df4.groupby('Age_Ranges',as_index=False)['Price'].mean()
ag_df5.rename(columns = {'Price':'Average Total Purchase per Person'}, inplace = True)
age_purchase = pd.merge(left=ag_df1, right=ag_df2)
age_purchase = pd.merge(left=age_purchase, right=ag_df3)
age_purchase = pd.merge(left=age_purchase, right=ag_df5)
age_purchase['Average Purchase Price'] = age_purchase['Average Purchase Price'].map("${:.2f}".format)
age_purchase['Total Purchase Value'] = age_purchase['Total Purchase Value'].map("${:,.2f}".format)
age_purchase['Average Total Purchase per Person'] = age_purchase['Average Total Purchase per Person'].map("${:.2f}".format)
age_purchase = age_purchase.set_index('Age_Ranges')
#print(age_purchase)
display(age_purchase)

#Top Spenders
#Run basic calculations to obtain the results in the table below
#Create a summary data frame to hold the results
#Sort the total purchase value column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame

sp_df1 = data_copy.groupby(['SN','Purchase ID','Price']).size()
sp_df1 = sp_df1.groupby('SN').size().reset_index(name='count')
sp_df1.rename(columns = {'count':'Purchase Count'}, inplace = True)
sp_df2 = data_copy.groupby('SN', as_index=False)['Price'].mean()
sp_df2.rename(columns = {'Price':'Average Purchase Price'}, inplace = True)
sp_df3 = data_copy.groupby('SN',as_index=False)['Price'].sum()
sp_df3.rename(columns = {'Price':'Total Purchase Value'}, inplace = True)
spend_purchase = pd.merge(left=sp_df1, right=sp_df2)
spend_purchase = pd.merge(left=spend_purchase, right=sp_df3)
spend_purchase_an = spend_purchase.nlargest(5, 'Total Purchase Value', keep='first')
spend_purchase_an['Average Purchase Price'] = spend_purchase_an['Average Purchase Price'].map("${:.2f}".format)
spend_purchase_an['Total Purchase Value'] = spend_purchase_an['Total Purchase Value'].map("${:.2f}".format)
spend_purchase_an = spend_purchase_an.set_index('SN')
#print(spend_purchase_an)
display(spend_purchase_an)

#Most Popular Items
#Retrieve the Item ID, Item Name, and Item Price columns
#Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
#Create a summary data frame to hold the results
#Sort the purchase count column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame

pop_it_df = data_copy.groupby(['SN','Item ID','Item Name','Price']).size()
pop_it_df1 = pop_it_df.groupby(['Item ID','Item Name','Price']).size().reset_index(name='count')
pop_it_df1 = pop_it_df1.sort_values('count',ascending=False)
pop_it_df1.rename(columns = {'count':'Purchase Count'}, inplace = True)
pop_it_df1.rename(columns = {'Price':'Item Price'}, inplace = True)
pop_it_df2 = data_copy.groupby(['Item ID','Item Name'],as_index=False)['Price'].sum()
pop_it_df2.rename(columns = {'Price':'Total Purchase Value'}, inplace = True)
pop_item = pd.merge(left=pop_it_df1, right=pop_it_df2)
pop_item = pop_item[['Item ID','Item Name','Purchase Count','Item Price','Total Purchase Value']]
pop_item_an = pop_item.nlargest(5, 'Purchase Count', keep='first')
pop_item_an['Total Purchase Value'] = pop_item_an['Total Purchase Value'].map("${:.2f}".format)
pop_item_an['Item Price'] = pop_item_an['Item Price'].map("${:.2f}".format)
pop_item_an = pop_item_an.set_index(['Item ID', 'Item Name'])
#print(pop_item_an)
display(pop_item_an)

#Most Profitable Items
#Sort the above table by total purchase value in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the data frame

pro_item_an = pop_item.nlargest(5, 'Total Purchase Value', keep='first')
pro_item_an['Total Purchase Value'] = pro_item_an['Total Purchase Value'].map("${:.2f}".format)
pro_item_an['Item Price'] = pro_item_an['Item Price'].map("${:.2f}".format)
pro_item_an = pro_item_an.set_index(['Item ID', 'Item Name'])
#print(pro_item_an)
display(pro_item_an)
