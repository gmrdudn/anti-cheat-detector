import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

normal = df[df["label"] == "normal"]
cheat = df[df["label"] == "cheat"]

plt.hist(normal["reaction_ms"], bins=10, alpha=0.7, label="Normal")
plt.hist(cheat["reaction_ms"], bins=10, alpha=0.7, label="Cheat")

plt.xlabel("Reaction Time (ms)")
plt.ylabel("Player Count")
plt.title("Reaction Time Distribution")
plt.legend()

plt.savefig("reaction_graph.png")
plt.show()