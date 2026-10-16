import pandas as po
import matplotlib.pyplot as plt
df = po.read_csv("scores.csv")
print(df)
print(df.columns)


plt.scatter(df.index, df["math"],label = "math")
plt.scatter(df.index, df["python"], label = "python")
plt.scatter(df.index, df["database"], label = "database")

plt.xlabel("Student")
plt.ylabel("Score")
plt.legend()
plt.savefig("scattered.png")
plt.show()

fig, axes = plt.subplots(1, 3, figsize = (12, 4))
axes[0].hist(df["math"])
axes[0].set_title("math")

axes[1].hist(df["python"])
axes[1].set_title(df["python"])

axes[2].hist(df["database"])
axes[2].set.title(df["database"])



