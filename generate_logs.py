import csv
import random

vendors = ["HVAC_Vendor", "Cloud_Vendor", "SaaS_Vendor", "Former_Vendor"]

events = [
    "login",
    "data_access",
    "privilege_escalation",
    "payment_network_access"
]

access_levels = ["low", "medium", "high"]
statuses = ["active", "terminated"]

with open("vendor_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "vendor",
        "event",
        "access_level",
        "status",
        "offboarding_delay_days",
        "anomaly"
    ])

    for i in range(100):
        vendor = random.choice(vendors)

        if vendor == "Former_Vendor":
            status = "terminated"
            offboarding_delay = random.choice([7, 14, 30])
        else:
            status = "active"
            offboarding_delay = 0

        event = random.choice(events)
        access = random.choice(access_levels)

        if event in ["privilege_escalation", "payment_network_access"]:
            anomaly = "yes"
        elif status == "terminated":
            anomaly = "yes"
        else:
            anomaly = random.choice(["no", "no", "yes"])

        writer.writerow([
            vendor,
            event,
            access,
            status,
            offboarding_delay,
            anomaly
        ])

print("Vendor logs generated successfully.")
