# Cisco SD-WAN (vManage) Inventory & Certificate Monitor

A Python-based network automation tool designed to interface with the Cisco SD-WAN (vManage) REST API. The script securely authenticates against the controller, handles stateful session tokens, extracts internal inventory and control-plane security certification metrics, and maps raw JSON arrays into human-scannable data tables.

This repository demonstrates practical implementation of automated REST API data extraction, programmatic handling of non-standard stateful login workflows (cookie tracking), data fallback validation boundaries, and professional CLI output presentation.

---

## 🚀 Key Architectural Features

* **Stateful Token Extraction:** Programmatically intercepts and isolates the `JSESSIONID` authentication cookie from HTTP response headers during initial vendor web-auth sequences.
* **Defensive Key Fault-Tolerance:** Utilizes Python dictionary `.get()` retrieval parameters to guarantee script execution safety and prevent unexpected `KeyError` runtime crashes if edge-case data points are missing from managed enterprise nodes.
* **Granular Functional Isolation:** Decouples orchestration workflows by abstracting specific endpoints into dedicated, testable functions (`get_vmanage_token`, `get_device_certs`, `get_device_info`).
* **Operational Cryptographic Safety:** Integrates Python's native `getpass` library to capture interactive password input securely, shielding credentials from command-line echo vulnerability.
* **Structured Data Representation:** Integrates the third-party `rich` library to convert loose multi-layered JSON API dictionaries into clean, distinct, colorized CLI dashboards.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Libraries:** `requests` (HTTP operations), `getpass` (secure masking), `sys`
* **Third-Party Styling:** `rich` (for advanced terminal formatting)

---

## 📂 Project Blueprint

```text
├── vmanage_inventory.py      # Core modular automation engine 
├── .gitignore                # Excludes python bytecaches and local testing files
└── README.md                 # Detailed technical documentation
