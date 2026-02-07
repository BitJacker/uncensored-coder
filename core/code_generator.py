"""
Generatore di codice specializzato
"""

from .model_loader import ModelLoader
from .prompt_templates import PromptTemplates

class CodeGenerator:
    def __init__(self, model: str = "deepseek-coder:6.7b"):
        self.loader = ModelLoader(model)
        self.loader.pull_model()  # Assicura che il modello sia disponibile
        self.templates = PromptTemplates()
    
    def generate(self, user_request: str, language: str = "python") -> str:
        """
        Genera codice basato sulla richiesta dell'utente
        
        Args:
            user_request: Descrizione di cosa deve fare lo script
            language: Linguaggio di programmazione target
            
        Returns:
            Il codice generato con commenti
        """
        # Crea il prompt ottimizzato
        system_prompt = self.templates.get_system_prompt(language)
        user_prompt = self.templates.get_user_prompt(user_request, language)
        
        # Genera il codice
        code = self.loader.generate(user_prompt, system_prompt)
        
        return code
    
    def explain_code(self, code: str) -> str:
        """Spiega cosa fa un pezzo di codice"""
        prompt = f"Spiega in italiano cosa fa questo codice:\n\n{code}"
        return self.loader.generate(prompt)
    
    def improve_code(self, code: str, improvement: str) -> str:
        """Migliora un codice esistente"""
        prompt = f"Migliora questo codice: {improvement}\n\nCodice:\n{code}"
        return self.loader.generate(prompt)
