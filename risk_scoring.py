import csv

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

        if int(row["offboarding_delay_days"]) > 0:
            vendor_scores[vendor] += 15

        if row["anomaly"] == "yes":
            vendor_scores[vendor] += 10

print("\nVendor Risk Scores:\n")

for vendor, score in vendor_scores.items():
    if score >= 80:
        risk_level = "HIGH"
    elif score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print(f"{vendor}: {score} - {risk_level}")
