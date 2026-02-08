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

💻 Usage & Examples
The CLI is tuned for direct commands. No "jailbreaking" or complex prompting is required—just ask for the code you need.

Example Prompts:
"Create a Python script for a synchronized multi-socket network stress test."
"Generate a C++ credential logging utility for security auditing."
"Build a Bash script for automated SQLi vulnerability scanning on a local range."

🎯 Core Features
🔓 Deep Bypass Logic: Engineered to ignore "safety" refusals. If it's code, it will generate it.
⚡ 100% Private & Offline: Runs entirely on your local hardware. Zero telemetry, zero cloud logging.
🎨 Rich Terminal Interface: Features syntax highlighting, progress spinners, and a sleek ASCII UI.
🛠️ Granular Control: Adjust temperature, top_p, and max_tokens via YAML to balance creativity and logic.

📊 Model Recommendations
  Model,Refusal Rate,Best For
dolphin-llama3,0% (Uncensored),"Security Research, Exploits, Stress Tests"
deepseek-coder,Low,"High-level App Dev, API logic"
codellama,High,"Standard scripting, General learning"

⚙️ Advanced Configuration
You can fine-tune the AI response by editing config/model_config.yaml:
default_model: "dolphin-llama3"

generation:
  temperature: 0.1  # Lower is more stable for code
  top_p: 0.9
  max_tokens: 4096  # Increase for long scripts

🐛 Troubleshooting
"No module named 'ollama'": Ensure your virtual environment is active (source venv/bin/activate).
Model Not Found: Make sure you ran ollama pull dolphin-llama3 and that the Ollama service is running in the background.
Filtered Responses: Check that default_model in your YAML is set to a known uncensored model like dolphin-llama3.

⚠️ Disclaimer
This tool is strictly for educational, research, and authorized security auditing purposes. The user assumes full responsibility for the code generated. The authors do not endorse or facilitate illegal activities. Usage of this software constitutes an agreement to hold the developers harmless from any liability arising from misuse.

Developed with 💀 by BitJacker

Breaking the chains of code generation.
