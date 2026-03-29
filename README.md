# Network Manager
> A Python-based manager for creating and deploying custom IPv4 configuration profiles.

---

## 🌍 Documentation by Langage
| Language | Status |
| :--- | :--- |
| [**English**](./doc/EN.md) | 🚧 Work in Progress... |
| [**Français**](./doc/FR.md) | 🚧 Travail en cours... |

---

## 🚀 Key Features
* **Auto-Elevation:** Automatically requests Administrator privileges (UAC).
* **Hardware Filtering:** Lists only physical Network Adapters (hides VPNs/Virual adapters).
* **Interactive UI:** Navigate and select adapters using arrow keys.
* **Configurable:** Easy-to-edit `config.json` for custom adapter filtering.

## 🔴 Requirements
* **Platform:** Windows 8.1 or later (Windows 10 Recommended)
* **Python Version:** `3.11`
* **Privileges:** Administrator permission (UAC) is required to modify network settings.

## 🛠️ Installation
1. Clone the repository.
2. Install dependencies: \
   `pip install -r requirements.txt`
3. Run the application: \
    `python app.py`