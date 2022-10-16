#Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle = {'KitKat': '34,456,432 US Dollars' , 'Nescafe':'14,106,132 US Dollars', 'Maggi': '9,960,312 US Dollars','Nido':'44,506,003 US Dollars'}
#Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever= {'Lipton':'3,456,000 US Dollars','Breyers':' 1,235,891 US Dollars','HellManns':'17,241,412 US Dollars','Marmite':'11,715,324 US Dollars'}

Nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#Print each product sold by Unilever and the sales figures / numbers for that product.
for key, value in Unilever.items():
    print(key, value)
#Print each product sold by Nestle and the sales figures / numbers for that product.
for key, value in Nestle.items():
    print(key, value)
#Print which of the companies has more products that the other company.
Nestle_total=sum
Unilever_total=sum
#Print the top selling product from Nestle with sales figures
#Print the top selling product from Unilever with sales figures.
#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print(Nestle_countries.union(Unilever_countries))
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print(Nestle_countries.intersection(Unilever_countries))
#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in
print(Nestle_countries.difference(Unilever_countries))