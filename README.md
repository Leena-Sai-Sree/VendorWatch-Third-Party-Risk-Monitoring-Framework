# Third-Party Risk Monitoring & Audit Framework

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GRC](https://img.shields.io/badge/GRC-Third--Party%20Risk-8B0000?style=for-the-badge)
![IAM](https://img.shields.io/badge/IAM-Access%20Control-FF6900?style=for-the-badge)
![SOC](https://img.shields.io/badge/SOC-Continuous%20Monitoring-1679A7?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-TPRM%20%7C%20Audit%20%7C%20Compliance-4B0082?style=for-the-badge)

---

## Project Overview

This project implements an **end-to-end Third-Party Risk Monitoring and Audit Framework**, simulating a real-world GRC/SOC analyst workflow against vendor lifecycle activity logs.

The framework covers:
- Synthetic vendor activity log generation (login, access, escalation, offboarding)
- Automated risk scoring across the full vendor lifecycle
- Continuous audit alerting for anomalous vendor behavior
- Offboarding delay detection and access revocation monitoring
- Target-breach-style vendor compromise simulation (HVAC pivot scenario)
- Vendor risk score visualization dashboard

---

## Problem Statement

> **Given continuous vendor activity logs, can we reliably detect third-party access misuse, privilege escalation, and delayed offboarding — automatically, before a compliance review cycle catches it?**

Modern organizations rely on:
- **Static assessments** — one-time vendor questionnaires that go stale immediately
- **Periodic audits** — point-in-time snapshots that miss between-cycle risk
- **Self-attested controls** — no continuous evidence of vendor behavior

These gaps create exploitable windows. The 2013 Target breach demonstrated exactly this: a third-party HVAC vendor's compromised credentials provided the initial foothold into Target's payment network — a risk that continuous monitoring could have flagged.

---

## Environment & Tools

| Component         | Detail                                                       |
|-------------------|--------------------------------------------------------------|
| Language          | Python 3.10+                                                 |
| Log Format        | Simulated CSV vendor activity logs                           |
| Visualization     | `matplotlib` bar chart dashboard                             |
| Key Libraries     | `csv`, `random`, `matplotlib`                                |
| Output            | Console alerts, risk score report, PNG dashboard chart       |
| Framework Focus   | GRC / IAM / SOC-style continuous monitoring                  |

---

## Repository Structure

```
third-party-risk-monitoring-framework/
│
├── vendor_logs.csv          # Simulated vendor activity dataset
├── generate_logs.py         # Synthetic log generator (100 randomized events)
├── risk_scoring.py          # Vendor risk scoring engine
├── audit_monitor.py         # Continuous audit alert system
├── dashboard.py             # Risk score visualization (PNG output)
├── results_summary.md       # Key findings and methodology summary
└── README.md
```

---

## Methodology

### Step 1 — Log Generation

Generated a realistic synthetic vendor activity dataset using `generate_logs.py`, simulating four vendor profiles with distinct risk behaviors:

| Vendor          | Behavior Profile                                              | Risk Indicators                          |
|-----------------|---------------------------------------------------------------|------------------------------------------|
| `HVAC_Vendor`   | Target-style breach simulation — privilege escalation + payment network pivot | High access, anomalous events   |
| `Cloud_Vendor`  | Normal operational activity                                   | Low-medium access, no anomalies          |
| `SaaS_Vendor`   | Normal operational activity                                   | Low access, standard data access         |
| `Former_Vendor` | Terminated vendor with persistent access                      | Terminated status, 7–30 day offboarding delay |

---

### Step 2 — Risk Scoring Engine

`risk_scoring.py` calculates a cumulative risk score per vendor using a weighted indicator model:

| Risk Indicator              | Score Added |
|-----------------------------|-------------|
| High access level           | +10         |
| Privilege escalation event  | +20         |
| Payment network access      | +25         |
| Terminated vendor activity  | +30         |
| Offboarding delay > 0 days  | +15         |
| Anomalous activity flag     | +10         |

**Risk Tiers:**

| Score Range | Risk Level |
|-------------|------------|
| ≥ 80        | HIGH       |
| 40 – 79     | MEDIUM     |
| < 40        | LOW        |

---

### Step 3 — Continuous Audit Monitoring

`audit_monitor.py` replicates a SOC-style continuous monitoring loop — scanning every event row and firing alerts in real time:

| Alert Type        | Trigger Condition                                              | Severity    |
|-------------------|----------------------------------------------------------------|-------------|
| Persistent Access | Terminated vendor logs in or accesses data                     | CRITICAL    |
| Privilege Escalation | Any `privilege_escalation` event                            | HIGH        |
| Payment System Access | Any `payment_network_access` event                        | HIGH        |
| High Access Anomaly | `access_level=high` AND `anomaly=yes`                       | MEDIUM      |
| Offboarding Delay | `offboarding_delay_days > 0`                                  | OFFBOARDING ISSUE |

---

### Step 4 — Risk Visualization

`dashboard.py` produces a vendor risk score bar chart saved as `vendor_risk_scores.png` — ready for GitHub README, portfolio, or report inclusion.

---

## Results

| Metric                              | Value                  |
|-------------------------------------|------------------------|
| Total Vendor Events Analyzed        | 100 (generated)        |
| Vendors Monitored                   | 4                      |
| CRITICAL Alerts Generated           | Varies by run          |
| HIGH Alerts Generated               | Varies by run          |
| Vendors Rated HIGH Risk             | 2 (HVAC + Former)      |
| Offboarding Violations Detected     | Yes — Former_Vendor    |
| Payment Network Access Flagged      | Yes — HVAC_Vendor      |

> Scores vary between runs due to randomized log generation. Expected output: `HVAC_Vendor: HIGH`, `Former_Vendor: HIGH`, `Cloud_Vendor: LOW–MEDIUM`, `SaaS_Vendor: LOW–MEDIUM`.

---

## Key Findings

**HVAC_Vendor — HIGH RISK:** Simulates the Target breach attack vector. Privilege escalation and payment network access events detected. This vendor profile demonstrates how an active third-party credential compromise can go undetected without real-time monitoring.

**Former_Vendor — HIGH RISK:** Terminated vendor retains active system access with offboarding delays of 7–30 days. CRITICAL alerts fire on continued login and data access post-termination — a direct IAM control failure.

**Continuous Monitoring Advantage:** Static TPRM assessments conducted at onboarding or annual review would miss every finding in this dataset. All alerts occur between review cycles — exactly the detection window that continuous monitoring fills.

**Offboarding Gap:** Delayed access revocation for terminated vendors is one of the most common and preventable TPRM failures. The framework flags every instance with an explicit `OFFBOARDING ISSUE` alert tied to the exact delay duration.

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/third-party-risk-monitoring-framework
cd third-party-risk-monitoring-framework

# 2. Install dependencies
pip install matplotlib

# 3. Generate synthetic vendor logs
python generate_logs.py

# 4. Run risk scoring
python risk_scoring.py

# 5. Run continuous audit monitor
python audit_monitor.py

# 6. Generate risk score dashboard
python dashboard.py
```

**Expected output from `risk_scoring.py`:**
```
Vendor Risk Scores:

HVAC_Vendor: 120 - HIGH
Cloud_Vendor: 35 - LOW
SaaS_Vendor: 50 - MEDIUM
Former_Vendor: 160 - HIGH
```

---

## Limitations

- Synthetic dataset — directional simulation, not statistically representative of production vendor volumes
- Risk scoring uses additive weighting; production TPRM tools use normalized scoring with confidence intervals
- No API integration with real IAM systems (e.g., Okta, Azure AD) for live offboarding status
- No SOAR playbook integration for automated access revocation on CRITICAL alerts

## Possible Extensions

- [ ] Integrate with Okta / Azure AD API for real-time offboarding status pull
- [ ] Add SOAR webhook trigger on CRITICAL alerts (PagerDuty, Splunk SOAR)
- [ ] Export findings to JIRA / ServiceNow for GRC ticket workflow
- [ ] Build vendor risk trending over time with historical score comparison
- [ ] Add NIST CSF / ISO 27001 control mapping to each alert type

---

## Skills Demonstrated

- GRC Analysis & Third-Party Risk Management
- Vendor Lifecycle Management (onboarding → offboarding)
- IAM and Access Control Concepts
- SOC-Style Continuous Monitoring
- Audit and Compliance Validation
- Python Security Automation
- Risk Scoring & Tiering Logic
- Data Visualization (matplotlib)
- Target Breach Case Study Application

---

## Author

**[Your Name]**  
Cybersecurity Graduate Student | GRC · IAM · SOC · TPRM

---

## Resume Bullets

> Developed an evidence-driven Third-Party Risk Monitoring and Audit Framework using Python to compare static vendor assessments with continuous monitoring, demonstrating improved visibility into vendor access risks, offboarding gaps, and anomalous third-party activity.

> Built a Python-based TPRM simulation that modeled the 2013 Target breach HVAC vendor pivot scenario, implementing automated risk scoring, continuous audit alerting, and IAM offboarding delay detection across a synthetic vendor lifecycle dataset.

---

*Conducted in a controlled, simulated environment for educational and portfolio purposes only.*
