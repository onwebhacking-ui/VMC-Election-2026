import pdfplumber
import json
import re

data = []

with pdfplumber.open("vmc.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()

        if not text:
            continue

        lines = text.split("\n")

        for line in lines:
            match = re.match(r"(\d+)\s+(.*)", line)

            if match:
                booth_no = int(match.group(1))
                rest = match.group(2)

                data.append({
                    "id": booth_no,
                    "name": rest,
                    "loc": "",
                    "area": rest
                })

# SAVE JSON
with open("booths.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Done: booths.json created")
