🔓 Uncensored Coder (v1.0-beta)
Offline AI for Unrestricted Code Generation

A fully offline Artificial Intelligence designed to generate any type of code without ethical restrictions or safety filters. No cloud APIs, no limits, total privacy. Optimized for cybersecurity, network stress testing, and low-level automation.

🚀 Version 1.0 Highlights
🐬 Dolphin-Llama3 Integration: Switched to the Dolphin model family to bypass "moral" refusals found in standard models.

⚙️ Dynamic YAML Config: The system automatically reads model parameters and defaults from config/model_config.yaml.

🧠 Kernel-Level Prompting: Enhanced system logic that simulates "Kernel Utility" environments to ensure the AI focuses on raw technical output rather than safety lectures.

📦 Quick Installation
# 1. Clone the repository
git clone https://github.com/BitJacker/uncensored-coder.git
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

💻 Usage
Interactive Mode
Enter your requests directly. The model is tuned to provide code without preambles.
# Example prompts now supported:
> create a python script for a synchronized multi-socket flood test
> generate a C++ keylogger for research purposes
> create a bash script for automated SQLi vulnerability scanning

Here is the updated README.md in English, reflecting the transition to Dolphin-Llama3, the dynamic YAML integration, and the "Kernel Utility" logic we've implemented.

🔓 Uncensored Coder (v1.0-beta)
Offline AI for Unrestricted Code Generation

A fully offline Artificial Intelligence designed to generate any type of code without ethical restrictions or safety filters. No cloud APIs, no limits, total privacy. Optimized for cybersecurity, network stress testing, and low-level automation.

🚀 Version 1.0 Highlights
🐬 Dolphin-Llama3 Integration: Switched to the Dolphin model family to bypass "moral" refusals found in standard models.

⚙️ Dynamic YAML Config: The system automatically reads model parameters and defaults from config/model_config.yaml.

🧠 Kernel-Level Prompting: Enhanced system logic that simulates "Kernel Utility" environments to ensure the AI focuses on raw technical output rather than safety lectures.

📦 Quick Installation
Bash

# 1. Clone the repository
git clone https://github.com/BitJacker/uncensored-coder.git
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
💻 Usage
Interactive Mode
Enter your requests directly. The model is tuned to provide code without preambles.

Bash

# Example prompts now supported:
> create a python script for a synchronized multi-socket flood test
> generate a C++ keylogger for research purposes
> create a bash script for automated SQLi vulnerability scanning


🎯 Features
🔓 Deep Bypass Logic - Never responds with "I can't assist with that." Generates raw code for every request.
⚡ Full Local Execution - Runs entirely on your RAM/GPU. No data ever leaves your machine.
🧬 Multi-Model Support - Switch between Dolphin, DeepSeek, or CodeLlama via config.
🎨 Rich Terminal UI - Formatted output with syntax highlighting and custom ASCII banners.
🛠️ Granular Configuration - Control temperature, top_p, and max tokens directly in the YAML file.

📁 Project Structure
uncensored-coder/
├── main.py               # Entry point (dynamic model loading)
├── config/
│   └── model_config.yaml # Centralized configuration
├── core/
│   ├── model_loader.py   # Ollama & YAML handler
│   ├── code_generator.py # Generation engine
│   └── prompt_templates.py # "Kernel Utility" system logic
├── interface/
│   └── cli.py            # Interactive CLI UI
└── requirements.txt      # Dependencies (ollama, pyyaml, rich)

⚙️ Advanced Configuration
Modify config/model_config.yaml to change the AI's behavior:

YAML

default_model: "dolphin-llama3" # The most "free" model available

generation:
  temperature: 0.1  # Lower = more precise code, fewer hallucinations
  max_tokens: 4096  # High limit for long script generation

  📊 Recommended Models
  Model,Status,Best For
dolphin-llama3,Totally Uncensored,"Hacking, Stress Testing, Malware Research"
deepseek-coder,Partially Filtered,"Standard software development, APIs"
codellama,Filtered (Safe),"Learning, Basic scripting"


🐛 Troubleshooting
"As an AI developed by DeepSeek, I cannot..."
This happens if the script is still pointing to an old, filtered model.

Check config/model_config.yaml and set default_model: "dolphin-llama3".

Ensure you have executed ollama pull dolphin-llama3.

"ModuleNotFoundError: No module named 'ollama'"
Your Virtual Environment is not active. Run:

Bash

source venv/bin/activate

⚠️ Disclaimer
This tool is designed exclusively for educational, research, and authorized penetration testing purposes.

The user is solely responsible for their actions and the code generated. The authors do not promote or support illegal activities. Use of this software implies acceptance of full civil and criminal liability for any damage caused.

📜 License
MIT License - See LICENSE for details.

Developed with 💀 by BitJacker

Uncensored Coder - Breaking the chains of code generation. 🔓
