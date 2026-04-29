import csv

print("\nContinuous Vendor Audit Alerts:\n")

with open("vendor_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        vendor = row["vendor"]
        event = row["event"]
        access = row["access_level"]
        status = row["status"]
        delay = int(row["offboarding_delay_days"])
        anomaly = row["anomaly"]

        if status == "terminated" and event in ["login", "data_access"]:
            print(f"CRITICAL: {vendor} still has access after termination.")

        if event == "privilege_escalation":
            print(f"HIGH: {vendor} attempted privilege escalation.")

        if event == "payment_network_access":
            print(f"HIGH: {vendor} accessed payment-related systems.")

        if access == "high" and anomaly == "yes":
            print(f"MEDIUM: {vendor} had high access with anomalous behavior.")

        if delay > 0:
            print(f"OFFBOARDING ISSUE: {vendor} access delayed by {delay} days.")
