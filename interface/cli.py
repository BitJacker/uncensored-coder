from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from prompt_toolkit import prompt
import re

class CLI:
    def __init__(self, generator):
        self.generator = generator
        self.console = Console()
        self.last_code = None
        self.last_lang = "python"

    def display_code(self, code: str, language: str):
        # 1. Aesthetic Highlighted View
        syntax = Syntax(code, language, theme="monokai", line_numbers=False, word_wrap=True)
        self.console.print(Panel(syntax, title="✨ Generated Code", border_style="green"))
        
        # 2. Raw View for Copy-Paste (No Borders)
        self.console.print("\n[bold white]👇 SELECT AND COPY THE CODE BELOW:[/bold white]")
        print("-" * 40)
        print(code)
        print("-" * 40)

    def run(self):
        self.console.print("[bold cyan]🧞 Code Genie active! Type 'generate', 'save' or your request.[/bold cyan]")
        
        while True:
            try:
                user_input = prompt('\n🧞 > ').strip()
                if not user_input: continue
                if user_input.lower() in ['exit', 'quit']: break

                # SAVE command handling
                if user_input.lower().startswith('save'):
                    if not self.last_code:
                        self.console.print("[red]No code available to save.[/red]")
                        continue
                    fname = user_input.split()[1] if len(user_input.split()) > 1 else "script.py"
                    path = self.generator.save_to_file(self.last_code, fname)
                    self.console.print(f"[green]💾 Saved to {path}[/green]")
                    continue

                # Language detection logic
                lang = "python"
                for l in ["javascript", "java", "cpp", "html", "css", "sql", "rust", "go"]:
                    if l in user_input.lower(): lang = l

                with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=self.console) as prog:
                    prog.add_task(description="🤔 Generating...")
                    self.last_code = self.generator.generate(user_input, lang)
                    self.last_lang = lang

                self.display_code(self.last_code, self.last_lang)

            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
