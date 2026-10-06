import json
from datetime import datetime
import matplotlib.pyplot as plt

data_filename = input("Enter the data filename: ").strip()

with open(data_filename, "r", encoding="utf-8") as file:
    eva_data = json.load(file)

selected_country = input("Enter a country (USA or Russia): ").strip()

records = []
country_total_hours = 0
category_counts = {"Short": 0, "Standard": 0, "Long": 0}

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")

    if not duration_text:
        continue

    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    if duration_hours < 4:
        category = "Short"
    elif duration_hours < 7:
        category = "Standard"
    else:
        category = "Long"
    category_counts[category] += 1

    if eva.get("country", "").casefold() == selected_country.casefold():
        country_total_hours += duration_hours

    if not date_text:
        continue

    date = datetime.fromisoformat(date_text)
    records.append((date, duration_hours))

print(
    f"Total EVA duration for {selected_country}: "
    f"{country_total_hours:.2f} hours"
)

classified_evas = sum(category_counts.values())
print("EVA duration categories (all EVAs with a duration):")
for category, count in category_counts.items():
    percentage = count / classified_evas * 100 if classified_evas else 0
    print(f"{category}: {count} EVAs ({percentage:.2f}%)")

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

for date, duration_hours in records:
    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)

plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
