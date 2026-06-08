# Cisco SD-WAN (vManage) Inventory & Certificate Monitor

A Python-based network automation tool designed to interface with the Cisco SD-WAN (vManage) REST API. The script securely authenticates against the controller, handles stateful session tokens, extracts internal inventory and control-plane security certification metrics, and maps raw JSON arrays into human-scannable data tables.

---

## 🚀 Key Architectural Features

* **Defensive Key Fault-Tolerance:** Utilizes Python dictionary `.get()` retrieval parameters to guarantee script execution safety and prevent unexpected `KeyError` runtime crashes if edge-case data points are missing from managed enterprise nodes.
* **Granular Functional Isolation:** Decouples orchestration workflows by abstracting specific endpoints into dedicated, testable functions (`get_vmanage_token`, `get_device_certs`, `get_device_info`).
* **Structured Data Representation:** Integrates the third-party `rich` library to convert loose multi-layered JSON API dictionaries into clean, distinct, colorized CLI dashboards.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Libraries:** `requests` (HTTP operations), `getpass` (secure masking), `sys`
* **Third-Party Styling:** `rich` (for advanced terminal formatting)

---

## 📂 Project Blueprint

```text
├── cisco_sdwan_api.py      # Core modular automation engine 
├── .gitignore                # Excludes python bytecaches and local testing files
├── requirements.txt          # Packages required by a script to be working 
└── README.md                 # Detailed technical documentation
```

---

## 💻 Installation & Usage
1. Replicate Local Repository
```bash
git clone https://github.com/MarcinSZN/cisco-sdwan-data-collector.git
```   
2. Install Required Modules
```bash
pip install requirements.txt
```
3. Run the Tool
```bash
python cisco_sdwan_api.py
```

---

## 📊 Sample Execution Dashboards
1. Control Plane Certificate Overview Table

```text
        SDWAN Devices Certificates        
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Device Type ┃ Expiration Date          ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ vbond       │ Jul 08 16:17:34 2026 GMT │
│ vmanage     │ Aug 07 11:14:44 2026 GMT │
│ vsmart      │ Jul 08 16:17:53 2026 GMT │
└─────────────┴──────────────────────────┘
```

2. Edge Active Physical / Virtual Infrastructure Inventory
```text
                                         SDWAN Devices                                         
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ Hostname    ┃ Device-Model ┃ UUID                                     ┃ System-IP ┃ Site-ID ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ vManage     │ vmanage      │ 0b7491d5-8367-4240-8108-00de5ba53d14     │ 1.1.1.20  │ 1       │
│ vSmart      │ vsmart       │ a94d2e05-d621-4ef4-af6b-a599f3fd4bc7     │ 1.1.1.30  │ 1       │
│ vBond       │ vedge-cloud  │ 7fb6495d-4b8e-484c-9976-cd508cb9e16f     │ 1.1.1.10  │ 1       │
│ BR1-cEdge-1 │ vedge-C8000V │ C8K-6367175e-2df8-40f2-8793-772f91d444df │ 1.1.1.80  │ 101     │
│ BR2-cEdge-1 │ vedge-C8000V │ C8K-e95cfdf6-7d55-4dd3-8a9c-6f6c5fc6a369 │ 1.1.1.100 │ 102     │
│ BR3-cEdge-1 │ vedge-C8000V │ C8K-3f46e159-c306-45e4-b101-9e756271df65 │ 1.1.1.110 │ 103     │
│ DC1-cEdge-1 │ vedge-C8000V │ C8K-27b29de9-f227-4bbc-8ccc-86efaf6c3448 │ 1.1.1.40  │ 10      │
│ DC2-cEdge-1 │ vedge-C8000V │ C8K-dff0d720-003d-4b3a-9259-4951913fc1c5 │ 1.1.1.60  │ 20      │
└─────────────┴──────────────┴──────────────────────────────────────────┴───────────┴─────────┘
```

---

## DISCLAIMER

Script tested in a lab environment with SD-WAN version 20.16.1. Script was used to demonstrate how programmaticaly **some** informational data can be extracted from SD-WAN Controller using REST API and Python.
Solution might crash unexpected, it not handles every possible error (sorry for that :))
