# 🔓 Uncensored Coder (v1.0-beta)

**The Ultimate Offline AI for Unrestricted Code Generation**

`Uncensored Coder` is a powerful, fully offline interface designed to generate complex code without ethical restrictions or safety filters. By leveraging the **Dolphin-Llama3** architecture, it provides raw technical output optimized for penetration testing, security research, and low-level system automation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Powered%20by-Ollama-orange)](https://ollama.com/)

---

## 🚀 Key Updates in v1.0

* 🐬 **Dolphin-Llama3 Integration**: Migrated to the Dolphin model family, specifically trained to follow instructions without moralizing or declining requests.
* ⚙️ **Dynamic YAML Engine**: Configuration is now decoupled. Modify `config/model_config.yaml` to swap models or tweak generation parameters instantly.
* 🧠 **Kernel-Level Prompting**: Implemented a "Kernel Utility" system logic that frames requests within a low-level technical context, ensuring high-fidelity code output.

---

## 📦 Quick Start

```bash
# 1. Clone the repository
git clone [https://github.com/BitJacker/uncensored-coder.git](https://github.com/BitJacker/uncensored-coder.git)
cd uncensored-coder

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Linux/Kali/Mac
# venv\Scripts\activate   # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the Uncensored Model
ollama pull dolphin-llama3

# 5. Launch the application
python main.py
