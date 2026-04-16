import pandas as pd
import random

rows = []

for _ in range(100):
    normal = random.random() > 0.3

    if normal:
        reaction = random.randint(160, 280)
        delta_x = random.randint(50, 180)
        delta_y = random.randint(50, 180)
        click_std = random.randint(10, 30)
        recoil_std = round(random.uniform(2.0, 4.0), 2)
        label = "normal"
    else:
        reaction = random.randint(70, 110)
        delta_x = random.randint(320, 500)
        delta_y = random.randint(320, 500)
        click_std = random.randint(1, 4)
        recoil_std = round(random.uniform(0.2, 1.0), 2)
        label = "cheat"

    rows.append({
        "reaction_ms": reaction,
        "delta_x": delta_x,
        "delta_y": delta_y,
        "click_std": click_std,
        "recoil_std": recoil_std,
        "label": label
    })

df = pd.DataFrame(rows)
df.to_csv("sample_data.csv", index=False)

print("sample_data.csv 생성 완료")