"""
Interfaccia a linea di comando interattiva
"""

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

class CLI:
    def __init__(self, generator):
        self.generator = generator
        self.console = Console()
        self.history = InMemoryHistory()
    
    def show_welcome(self):
        """Mostra il messaggio di benvenuto"""
        welcome = """
# 🧞‍♂️ Code Genie

Benvenuto! Sono un'AI specializzata nella generazione di codice.

**Comandi disponibili:**
- Scrivi la tua richiesta per generare codice
- `exit` o `quit` per uscire
- `help` per vedere questo messaggio

**Esempio:**
> crea uno script python per rinominare tutti i file .txt in una cartella
        """
        self.console.print(Markdown(welcome))
    
    def run(self):
        """Avvia la CLI interattiva"""
        self.show_welcome()
        
        while True:
            try:
                # Input utente
                user_input = prompt(
                    '\n> ',
                    history=self.history
                ).strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    self.console.print("\n👋 Ciao!", style="bold green")
                    break
                
                if user_input.lower() == 'help':
                    self.show_welcome()
                    continue
                
                # Genera il codice
                self.console.print("\n🤔 Generando il codice...", style="yellow")
                
                code = self.generator.generate(user_input)
                
                # Mostra il risultato
                self.console.print(
                    Panel(
                        code,
                        title="✨ Codice Generato",
                        border_style="green"
                    )
                )
                
            except KeyboardInterrupt:
                self.console.print("\n\n👋 Ciao!", style="bold green")
                break
            except Exception as e:
                self.console.print(f"\n❌ Errore: {e}", style="bold red")
