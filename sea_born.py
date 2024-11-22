import seaborn as sns
import matplotlib.pyplot as plt

# scatter plot
data = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=data)
plt.title("Total Bill vs Tip Amount")
plt.show()

# Bar plot
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Total Bill By Day of Week")
plt.show()


# Clear and Cluttered visualization
X = [1,2,3,4,5]
Y = [10,20,25,30,35]
plt.plot(X,Y, color="green", linewidth=4, linestyle="--", marker="o")
plt.title("Too many styles at once")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

plt.plot(X,Y)
plt.title("Simple and Consise")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

sns.set_palette("colorblind")
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Colorblind-Friendly Plot")
plt.show()