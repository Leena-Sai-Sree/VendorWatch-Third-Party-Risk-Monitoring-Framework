import csv
import matplotlib.pyplot as plt

vendor_scores = {}

with open("vendor_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        vendor = row["vendor"]

        if vendor not in vendor_scores:
            vendor_scores[vendor] = 0

        if row["access_level"] == "high":
            vendor_scores[vendor] += 10

        if row["event"] == "privilege_escalation":
            vendor_scores[vendor] += 20

        if row["event"] == "payment_network_access":
            vendor_scores[vendor] += 25

        if row["status"] == "terminated":
            vendor_scores[vendor] += 30

        if row["anomaly"] == "yes":
            vendor_scores[vendor] += 10

vendors = list(vendor_scores.keys())
scores = list(vendor_scores.values())

plt.bar(vendors, scores)
plt.title("Third-Party Vendor Risk Scores")
plt.xlabel("Vendor")
plt.ylabel("Risk Score")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("vendor_risk_scores.png")
plt.show()
