#!/usr/bin/env python3
"""
🔓 Uncensored Coder - Setup Automatico
Installa tutto quello che serve in automatico
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    banner = f"""
{Color.BLUE}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║      🔓 UNCENSORED CODER - Setup Automatico 🔓           ║
║                                                           ║
║   AI Offline senza censure per generazione codice        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Color.END}
    """
    print(banner)

def run_command(cmd, description, shell=True):
    """Esegue un comando e mostra output"""
    print(f"\n{Color.YELLOW}⚙️  {description}...{Color.END}")
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"{Color.GREEN}✅ {description} completato!{Color.END}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Color.RED}❌ Errore durante: {description}{Color.END}")
        print(f"{Color.RED}{e.stderr}{Color.END}")
        return False

def check_python_version():
    """Verifica versione Python"""
    print(f"\n{Color.BLUE}🔍 Controllo Python...{Color.END}")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"{Color.GREEN}✅ Python {version.major}.{version.minor} OK{Color.END}")
        return True
    else:
        print(f"{Color.RED}❌ Serve Python 3.8 o superiore{Color.END}")
        return False

def check_ollama_installed():
    """Controlla se Ollama è già installato"""
    return shutil.which("ollama") is not None

def install_ollama():
    """Installa Ollama"""
    print(f"\n{Color.BLUE}📦 Installazione Ollama...{Color.END}")
    
    if check_ollama_installed():
        print(f"{Color.GREEN}✅ Ollama già installato!{Color.END}")
        return True
    
    system = platform.system().lower()
    
    if system == "linux":
        print(f"{Color.YELLOW}⬇️  Scaricando Ollama per Linux...{Color.END}")
        success = run_command(
            "curl -fsSL https://ollama.com/install.sh | sh",
            "Download e installazione Ollama"
        )
        if not success:
            print(f"\n{Color.YELLOW}⚠️  Installazione automatica fallita.{Color.END}")
            print(f"{Color.YELLOW}Prova manualmente:{Color.END}")
            print(f"  curl -fsSL https://ollama.com/install.sh | sh")
            return False
        return True
    
    elif system == "darwin":  # macOS
        print(f"{Color.YELLOW}📱 macOS rilevato{Color.END}")
        print(f"Scarica Ollama da: {Color.BLUE}https://ollama.com/download/mac{Color.END}")
        input(f"\n{Color.YELLOW}Premi INVIO dopo aver installato Ollama...{Color.END}")
        return check_ollama_installed()
    
    elif system == "windows":
        print(f"{Color.YELLOW}🪟 Windows rilevato{Color.END}")
        print(f"Scarica Ollama da: {Color.BLUE}https://ollama.com/download/windows{Color.END}")
        input(f"\n{Color.YELLOW}Premi INVIO dopo aver installato Ollama...{Color.END}")
        return check_ollama_installed()
    
    return False

def start_ollama_service():
    """Avvia il servizio Ollama"""
    print(f"\n{Color.BLUE}🚀 Avvio servizio Ollama...{Color.END}")
    
    # Controlla se è già in esecuzione
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            timeout=2
        )
        if result.returncode == 0:
            print(f"{Color.GREEN}✅ Ollama già in esecuzione!{Color.END}")
            return True
    except:
        pass
    
    # Avvia in background
    try:
        if platform.system().lower() != "windows":
            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
        else:
            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
        
        # Aspetta che si avvii
        import time
        print(f"{Color.YELLOW}⏳ Aspetto che Ollama si avvii...{Color.END}")
        time.sleep(3)
        
        # Verifica
        result = subprocess.run(["ollama", "list"], capture_output=True)
        if result.returncode == 0:
            print(f"{Color.GREEN}✅ Ollama avviato!{Color.END}")
            return True
    except Exception as e:
        print(f"{Color.RED}❌ Errore avvio Ollama: {e}{Color.END}")
    
    return False

def create_venv():
    """Crea ambiente virtuale"""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print(f"{Color.GREEN}✅ Virtual environment già presente{Color.END}")
        return True
    
    print(f"\n{Color.BLUE}📦 Creazione virtual environment...{Color.END}")
    success = run_command(
        f"{sys.executable} -m venv venv",
        "Creazione ambiente virtuale"
    )
    return success

def install_requirements():
    """Installa dipendenze Python"""
    print(f"\n{Color.BLUE}📦 Installazione dipendenze Python...{Color.END}")
    
    # Determina il percorso di pip nel venv
    if platform.system().lower() == "windows":
        pip_path = "venv\\Scripts\\pip"
    else:
        pip_path = "venv/bin/pip"
    
    # Installa dipendenze
    success = run_command(
        f"{pip_path} install -r requirements.txt",
        "Installazione pacchetti Python"
    )
    return success

def download_model():
    """Scarica il modello AI"""
    print(f"\n{Color.BLUE}🤖 Download modello AI...{Color.END}")
    print(f"{Color.YELLOW}📦 Modello: deepseek-coder:6.7b (~3.8 GB){Color.END}")
    print(f"{Color.YELLOW}⏳ Questo può richiedere alcuni minuti...{Color.END}\n")
    
    # Controlla se già scaricato
    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True
    )
    
    if "deepseek-coder:6.7b" in result.stdout:
        print(f"{Color.GREEN}✅ Modello già scaricato!{Color.END}")
        return True
    
    # Scarica il modello
    try:
        process = subprocess.Popen(
            ["ollama", "pull", "deepseek-coder:6.7b"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        for line in process.stdout:
            print(line, end='')
        
        process.wait()
        
        if process.returncode == 0:
            print(f"\n{Color.GREEN}✅ Modello scaricato con successo!{Color.END}")
            return True
        else:
            print(f"\n{Color.RED}❌ Errore download modello{Color.END}")
            return False
            
    except Exception as e:
        print(f"{Color.RED}❌ Errore: {e}{Color.END}")
        return False

def create_startup_script():
    """Crea script di avvio rapido"""
    print(f"\n{Color.BLUE}📝 Creazione script di avvio...{Color.END}")
    
    if platform.system().lower() == "windows":
        script_content = """@echo off
echo Starting Uncensored Coder...
call venv\\Scripts\\activate
python main.py
pause
"""
        script_name = "start.bat"
    else:
        script_content = """#!/bin/bash
echo "🔓 Starting Uncensored Coder..."
source venv/bin/activate
python main.py
"""
        script_name = "start.sh"
    
    with open(script_name, 'w') as f:
        f.write(script_content)
    
    if platform.system().lower() != "windows":
        os.chmod(script_name, 0o755)
    
    print(f"{Color.GREEN}✅ Script creato: {script_name}{Color.END}")
    return True

def print_success_message():
    """Messaggio finale di successo"""
    system = platform.system().lower()
    
    if system == "windows":
        start_cmd = "start.bat"
        or_cmd = "venv\\Scripts\\activate && python main.py"
    else:
        start_cmd = "./start.sh"
        or_cmd = "source venv/bin/activate && python main.py"
    
    message = f"""
{Color.GREEN}{Color.BOLD}
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           ✅ INSTALLAZIONE COMPLETATA! ✅                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
{Color.END}

{Color.BLUE}🚀 Per avviare Uncensored Coder:{Color.END}

  {Color.YELLOW}{start_cmd}{Color.END}

{Color.BLUE}Oppure:{Color.END}
  {Color.YELLOW}{or_cmd}{Color.END}

{Color.BLUE}📚 Funzionalità:{Color.END}
  • ✅ Generazione codice senza limiti
  • ✅ Completamente offline
  • ✅ Privacy totale
  • ✅ Supporto multi-linguaggio

{Color.BLUE}💡 Comandi utili:{Color.END}
  • Digita il tuo prompt per generare codice
  • 'exit' per uscire
  • 'help' per vedere i comandi
  • 'clear' per pulire lo schermo

{Color.GREEN}Happy hacking! 💀🔓{Color.END}
    """
    print(message)

def main():
    """Setup principale"""
    print_banner()
    
    # Check preliminari
    if not check_python_version():
        sys.exit(1)
    
    print(f"\n{Color.BOLD}Iniziando installazione automatica...{Color.END}")
    
    steps = [
        ("Installazione Ollama", install_ollama),
        ("Avvio servizio Ollama", start_ollama_service),
        ("Creazione virtual environment", create_venv),
        ("Installazione dipendenze Python", install_requirements),
        ("Download modello AI", download_model),
        ("Creazione script avvio", create_startup_script),
    ]
    
    for step_name, step_func in steps:
        try:
            success = step_func()
            if not success:
                print(f"\n{Color.RED}❌ Setup fallito durante: {step_name}{Color.END}")
                print(f"\n{Color.YELLOW}💡 Prova a:{Color.END}")
                print(f"  1. Verificare la connessione internet")
                print(f"  2. Eseguire con sudo (Linux/Mac)")
                print(f"  3. Consultare la documentazione: README.md")
                sys.exit(1)
        except KeyboardInterrupt:
            print(f"\n\n{Color.YELLOW}⚠️  Setup interrotto dall'utente{Color.END}")
            sys.exit(1)
        except Exception as e:
            print(f"\n{Color.RED}❌ Errore inaspettato: {e}{Color.END}")
            sys.exit(1)
    
    print_success_message()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Setup annullato.{Color.END}")
        sys.exit(1)
