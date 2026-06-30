import requests
import pandas as pd
from pathlib import Path

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    print(f"Downloading {name}...")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(output_folder / f"{name}_NAV.csv", index=False)

        print(f"Saved {name}_NAV.csv")
    else:
        print(f"Failed for {name}")