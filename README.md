# 🛡️ Bad Hand v2.5
### *The Swiss Army Knife for Security Auditing*

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)

**Bad Hand** is a comprehensive modular Python-based framework designed for conducting penetration tests on local networks and web applications. With 30 powerful tools organized into an intuitive command-line interface, it automates common scanning and testing processes while maintaining precision and ease of use.

---

## 🚀 Toolkit Overview

The project includes **30 specialized tools** organized into independent modules for maximum efficiency:

### 🌐 Network Analysis & Attack
| Tool | Description |
| :--- | :--- |
| `scan.py` | Active host discovery and comprehensive network mapping |
| `deauther.py` | Wi-Fi client deauthentication for wireless security testing |
| `udp_attak.py` | Network stress testing via UDP flood attacks |
| `port_scanner.py` | Nmap-like port scanning to identify open services |

### 🔐 Web Application Security
| Tool | Description |
| :--- | :--- |
| `xss_scanner.py` | Detects Cross-Site Scripting (XSS) vulnerabilities in web forms |
| `sqli_scanner.py` | Comprehensive SQL Injection vulnerability scanner |
| `rce_test.py` | Tests for Remote Code Execution (RCE) vulnerabilities |
| `clickjacking_test.py` | Identifies clickjacking attack vectors |
| `header_check.py` | Analyzes HTTP security headers for misconfigurations |
| `robots_analyzer.py` | Examines robots.txt for hidden paths and misconfigurations |
| `param_miner.py` | Discovers hidden URL parameters for testing |

### 🕵️ OSINT & Reconnaissance
| Tool | Description |
| :--- | :--- |
| `subdomain_enum.py` | Advanced subdomain enumeration for target expansion |
| `dns_lookup.py` | Comprehensive DNS record enumeration and analysis |
| `whois_recon.py` | Gathers WHOIS information for domain intelligence |
| `reverse_ip.py` | Reverse IP lookup to find domains on shared hosting |
| `cms_detector.py` | Identifies Content Management Systems (WordPress, Joomla, etc.) |
| `cloud_finder.py` | Discovers exposed cloud storage buckets (AWS, Azure, GCP) |
| `wp_scan.py` | WordPress-specific vulnerability scanner |
| `js_extractor.py` | Extracts and analyzes JavaScript files for sensitive data |
| `api_discovery.py` | Maps and discovers hidden API endpoints |

### 🔓 Authentication & Brute Force
| Tool | Description |
| :--- | :--- |
| `credential_stuffing.py` | Tests login endpoints against credential databases |
| `ssh_brute.py` | SSH protocol brute force authentication testing |
| `ftp_brute.py` | FTP server credential brute forcing |
| `dir_bruteforce.py` | Directory and file discovery through brute forcing |

### 🛡️ SSL/TLS & Security
| Tool | Description |
| :--- | :--- |
| `ssl_checker.py` | Validates SSL/TLS certificates and cipher configurations |

### 🔧 Utilities & Analysis
| Tool | Description |
| :--- | :--- |
| `hash_id.py` | Identifies hash types (MD5, SHA1, SHA256, etc.) |
| `ip_geo.py` | IP address geolocation and ASN lookup |
| `mail_spoof.py` | Tests email spoofing vulnerabilities (SPF, DMARC, DKIM) |
| `honeypot_det.py` | Detects potential honeypot systems |
| `sub_takeover.py` | Identifies subdomain takeover vulnerabilities |

---

## 🛠️ Installation

### Prerequisites
- **Operating System**: Linux (Kali Linux, Parrot OS, or Ubuntu recommended)
- **Python**: Version 3.8 or higher
- **Privileges**: Root/sudo access required for network-level tools

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BitJacker/BadHand.git
   cd BadHand
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   python3 badhand.py
   ```

---

## 🔌 Usage

### Running the Framework

**Standard Mode:**
```bash
python3 badhand.py
```

**With Elevated Privileges** (required for network tools):
```bash
sudo python3 badhand.py
```

### Interactive Menu

Bad Hand features an intuitive menu-driven interface:

1. Select a tool by entering its number (1-30)
2. Read the tool description
3. Confirm execution
4. Provide required parameters (target IP, URL, wordlist, etc.)
5. View results in real-time

### Example Workflows

**Network Reconnaissance:**
```bash
# 1. Run Bad Hand
sudo python3 badhand.py

# 2. Select tool [3] NETWORK SCAN
# 3. Enter target: 192.168.1.0/24
# 4. View discovered hosts and services
```

**Web Vulnerability Assessment:**
```bash
# 1. Select tool [4] XSS SCANNER
# 2. Enter target: https://example.com
# 3. Review discovered vulnerabilities
```

**Subdomain Discovery:**
```bash
# 1. Select tool [10] SUBDOMAIN ENUM
# 2. Enter domain: example.com
# 3. Provide wordlist: /usr/share/wordlists/subdomains.txt
# 4. Analyze discovered subdomains
```

---

## 📁 Project Structure

```
BadHand/
├── badhand.py              # Main framework (interactive menu UI)
├── requirements.txt        # Python dependencies
├── LICENSE.txt             # License information
├── README.md               # Project documentation
└── tool/                   # Tool modules directory
    ├── api_discovery.py
    ├── clickjacking_test.py
    ├── cloud_finder.py
    ├── cms_detector.py
    ├── credential_stuffing.py
    ├── deauther.py
    ├── dir_bruteforce.py
    ├── dns_lookup.py
    ├── ftp_brute.py
    ├── hash_id.py
    ├── header_check.py
    ├── honeypot_det.py
    ├── ip_geo.py
    ├── js_extractor.py
    ├── mail_spoof.py
    ├── param_miner.py
    ├── port_scanner.py
    ├── rce_test.py
    ├── reverse_ip.py
    ├── robots_analyzer.py
    ├── scan.py
    ├── sqli_scanner.py
    ├── ssh_brute.py
    ├── ssl_checker.py
    ├── subdomain_enum.py
    ├── sub_takeover.py
    ├── udp_attak.py
    ├── whois_recon.py
    ├── wp_scan.py
    └── xss_scanner.py
```

---

## 🎯 Key Features

- ✅ **30 Specialized Tools** - Comprehensive security testing suite
- ✅ **Modular Architecture** - Easy to maintain and extend
- ✅ **User-Friendly Interface** - Intuitive menu-driven navigation
- ✅ **Detailed Descriptions** - Each tool includes usage guidance
- ✅ **Safe Input Handling** - Built-in input sanitization
- ✅ **Color-Coded Output** - Enhanced readability
- ✅ **Error Handling** - Graceful failure management
- ✅ **Cross-Tool Workflow** - Seamless integration between modules

---

## 📋 Requirements

The framework requires the following Python packages:

```
requests>=2.28.0
scapy>=2.5.0
beautifulsoup4>=4.11.0
dnspython>=2.3.0
python-whois>=0.8.0
paramiko>=3.0.0
ftplib (standard library)
hashlib (standard library)
ssl (standard library)
```

Additional system requirements:
- `libpcap-dev` (for packet capture)
- Wireless adapter with monitor mode support (for WiFi tools)
- `nmap` (optional, for enhanced scanning)

---

## 🔒 Security Best Practices

1. **Always obtain written authorization** before testing any system
2. **Use in isolated environments** (home lab, VMs) for practice
3. **Respect rate limits** to avoid service disruption
4. **Document findings** professionally in security reports
5. **Never store** credentials or sensitive data discovered during tests
6. **Follow responsible disclosure** when reporting vulnerabilities

---

## ⚠️ Legal Disclaimer

> **IMPORTANT**: Bad Hand is designed exclusively for **authorized security testing** and **educational purposes**.

**Unauthorized access to computer systems is illegal.** Use of this framework against targets without prior written consent violates laws including but not limited to:
- Computer Fraud and Abuse Act (CFAA) - United States
- Computer Misuse Act - United Kingdom  
- Similar legislation in other jurisdictions

**By using Bad Hand, you agree to:**
- Obtain proper authorization before conducting any security tests
- Comply with all applicable local, state, federal, and international laws
- Accept full responsibility for your actions

**The developer (BitJacker) assumes NO LIABILITY** for:
- Misuse of this toolkit
- Damage caused by unauthorized testing
- Legal consequences resulting from improper use

**Use at your own risk. Stay legal, stay ethical.**

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs
- Open an issue with detailed reproduction steps
- Include system information and error messages
- Suggest potential fixes if possible

### Adding Features
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewTool`)
3. Follow the existing code structure
4. Add documentation for new tools
5. Test thoroughly
6. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Include docstrings for functions
- Add error handling
- Sanitize user inputs
- Comment complex logic

---

## 📚 Documentation & Resources

- **GitHub Repository**: [https://github.com/BitJacker/BadHand](https://github.com/BitJacker/BadHand)
- **Issue Tracker**: Report bugs and request features
- **Wiki**: Detailed tool documentation and tutorials (coming soon)

### Recommended Learning Resources
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [HackerOne Hacker101](https://www.hacker101.com/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)

---

## 🏆 Credits

**Bad Hand** is developed and maintained by **BitJacker**.

### Special Thanks
- The open-source security community
- Contributors and testers
- Tool developers whose work inspired this project

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

---

## 📞 Contact

- **Developer**: BitJacker
- **GitHub**: [@BitJacker](https://github.com/BitJacker)
- **Issues**: [GitHub Issues](https://github.com/BitJacker/BadHand/issues)

---

## 🔄 Version History

### v2.5 (Current)
- Expanded to 30 specialized tools
- Enhanced menu interface
- Improved error handling
- Added tool categorization
- Better input sanitization

### v1.0 (Initial Release)
- 10 core security tools
- Basic menu system
- Foundation framework

---

<div align="center">

**Made with ❤️ for the security community**

*Remember: With great power comes great responsibility*

⭐ Star this repository if you find it useful!

</div>
