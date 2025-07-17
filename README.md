# 🚨 Pen‑testing Abode

A centralized toolkit housing a variety of essential penetration‑testing utilities — everything from reconnaissance to exploitation, built in Python.

## 📌 Table of Contents

* [About](#about)
* [Key Features](#key-features)
* [Architecture & Technologies](#architecture--technologies)
* [Setup & Installation](#setup--installation)
* [Usage Examples](#usage-examples)
* [Contributing](#contributing)
* [License & Attribution](#license--attribution)

---

## About

Pen‑testing Abode is designed as a one‑stop‑shop for security enthusiasts and professionals alike to audit local networks and systems. Whether you're learning or auditing, this suite simplifies:

* Web crawling & enumeration
* Vulnerability scanning
* Keylogging
* ARP spoofing & MAC address manipulation
* HTTPS bypass and code injection capabilities ([GitHub][1], [Information Security Stack Exchange][2])

---

## Key Features

| Feature                   | Description                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| **Web Crawler**           | Automates link discovery for active scanning                     |
| **Vulnerability Scanner** | Identifies potential security issues in target systems           |
| **Keylogger**             | Captures keystrokes for local monitoring and testing scenarios   |
| **MAC Address Changer**   | Spoofs MAC addresses to evade detection or emulate other devices |
| **ARP Spoofer**           | Conducts man-in-the-middle attacks on local networks             |
| **HTTPS Bypasser**        | Enables testing of HTTPS restrictions and SSL fallback paths     |
| **Code Injector**         | Illustrates injection vulnerabilities in web applications        |

---

## Architecture & Technologies

* **Language**: 100% Python (used Django)
* **Modular design**: Each tool exists as a stand-alone script for ease of maintenance and use&#x20;
* **Extensions-ready**: Ideal scaffold for plugins, automation scripts, or integration with CI/CD pipelines

---

## Setup & Installation

Make sure you have **Python 3.8+** installed on Linux:

```bash
git clone https://github.com/fabihafatima/Pen-testing-Abode.git
cd Pen-testing-Abode
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Usage**

Each tool lives in its own file. Run them directly:

```bash
python webcrawler.py --help
python arp_spoof.py --target 192.168.1.5
```

Adjust flags based on tool (e.g., `--interface`, `--output`). Individual scripts include inline help.

---

## Usage Examples

### 🌐 Web Crawler

```bash
python webcrawler.py --url https://example.com --depth 2
```

Maps out website structure for manual review or automated scanning.

### 🛡️ Vulnerability Scanner

```bash
python vuln_scanner.py --host 10.0.0.12 --port 80
```

Scans for known services and misconfigurations for pen‑test prep.

### 🧠 ARP Spoofer

```bash
sudo python arp_spoof.py --victim 10.0.0.5 --gateway 10.0.0.1 --interface eth0
```

Intercepts network traffic between victim and router.

---

## Contributing

Contributions encouraged! Here's how to participate:

1. **Fork** this repo
2. **Create a branch** (`git checkout -b feature/awesome-tool`)
3. **Make your changes**, include appropriate tests or proof of concept
4. **Submit a pull request** — add details on your additions/improvements

Please follow [PEP8 coding standards](https://www.python.org/dev/peps/pep-0008/) and use clear commit messages.

---

## License & Attribution

This project is licensed under the **[MIT License](LICENSE)** — feel free to use or adapt it

---

## 📬 Get in Touch

I’m open to feedback, improvements, and collaboration. If you'd like to connect:

* ⭐ Star and follow on GitHub
* 📨 Open an issue or PR
* 💬 DM me on LinkedIn

---
