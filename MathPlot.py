import matplotlib.pyplot as plt

# Days vs stock prices
days = [1,2,3,4,5]
prices = [700,1200,1500,1400,1800]
# Plotting values
plt.plot(days,prices)
plt.title("Naira prices over days")
plt.xlabel("Days")
plt.ylabel("Maira Prices")
plt.show()

categories = ["Electronic", "Furniture", "Clothing", "Food"]
sales = [2000, 15000, 5000, 10000]
# Plotting values
plt.bar(categories,sales)
plt.title("Sales by product")
plt.xlabel("Category")
plt.ylabel("Sales($)")
plt.show()


# Advanced Matplotlib

#Subplots example
fig, axs = plt.subplots(1,2, figsize=(10,5))

# Page views
days = [1,2,3,4,5]
views = [100,120,130,115,150]
axs[0].plot(days,views)
axs[0].set_title("Page Views Over 5 Days")

# Sign-ups
signups = [5,10,15,7,9]
axs[1].bar(days,signups)
axs[1].set_title("User signups Over 5 Days")

plt.tight_layout()
plt.show()         