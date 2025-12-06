import json
from collections import Counter
import matplotlib.pyplot as plt

filename = input("Enter filename (*.json): ")
filename.strip()

# 1) JSON aus PyTM einlesen
with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

# In neueren PyTM-Versionen gibt es typischerweise ein Feld "findings"
findings = data.get("findings", [])

print(data.keys())
# oder:
print(data.get("findings", [])[:2])

# 2) Schweregrade einsammeln (z.B. "LOW", "MEDIUM", "HIGH")
severities = [f.get("severity", "UNDEFINED") for f in findings]
counts = Counter(severities)

if not counts:
    print("Keine Findings gefunden – evtl. ist dein Modell zu 'sicher' oder die JSON-Struktur ist anders.")
    exit(0)
else:
    for finding_threat in findings:
        print(finding_threat["target"], finding_threat["severity"], finding_threat["description"])
labels = list(counts.keys())
values = [counts[label] for label in labels]

# 3) Balkendiagramm bauen
plt.figure()
plt.bar(labels, values)
plt.xlabel("Schweregrad (Severity)")
plt.ylabel("Anzahl Findings")
plt.title("Threat Model – Findings pro Schweregrad")
plt.tight_layout()

# 4) Als PNG speichern und anzeigen
plt.savefig(f"{filename}_threatmodel_severity.png", dpi=150)
plt.show()
