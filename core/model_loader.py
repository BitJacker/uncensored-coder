"""
Gestisce il caricamento e l'interazione con i modelli Ollama
"""

import ollama
from typing import Optional

class ModelLoader:
    def __init__(self, model_name: str = "deepseek-coder:6.7b"):
        self.model_name = model_name
        self.client = ollama.Client()
        
    def is_model_available(self) -> bool:
        """Verifica se il modello è già scaricato"""
        try:
            models = self.client.list()
            return any(self.model_name in model['name'] for model in models['models'])
        except:
            return False
    
    def pull_model(self):
        """Scarica il modello se non presente"""
        if not self.is_model_available():
            print(f"Downloading {self.model_name}...")
            self.client.pull(self.model_name)
            print("Download completato!")
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Genera una risposta dal modello"""
        messages = []
        
        if system_prompt:
            messages.append({
                'role': 'system',
                'content': system_prompt
            })
        
        messages.append({
            'role': 'user',
            'content': prompt
        })
        
        response = self.client.chat(
            model=self.model_name,
            messages=messages
        )
        
        return response['message']['content']
