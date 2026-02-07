"""
Template di prompt ottimizzati per la generazione di codice
"""

class PromptTemplates:
    
    LANGUAGE_SPECS = {
        'python': {
            'extension': '.py',
            'style': 'PEP 8',
            'docs': 'docstrings'
        },
        'bash': {
            'extension': '.sh',
            'style': 'Google Shell Style Guide',
            'docs': 'comments'
        },
        'javascript': {
            'extension': '.js',
            'style': 'Airbnb JavaScript Style Guide',
            'docs': 'JSDoc'
        },
        'sql': {
            'extension': '.sql',
            'style': 'SQL formatting best practices',
            'docs': 'inline comments'
        }
    }
    
    def get_system_prompt(self, language: str) -> str:
        """Genera il system prompt per un linguaggio specifico"""
        spec = self.LANGUAGE_SPECS.get(language.lower(), self.LANGUAGE_SPECS['python'])
        
        return f"""Sei un esperto programmatore specializzato in {language}.
Genera codice pulito, ben commentato e seguendo le best practices ({spec['style']}).
Includi sempre:
- Commenti esplicativi in italiano
- Gestione degli errori dove appropriato
- Codice pronto all'uso
- {spec['docs']} per documentare il codice

Rispondi SOLO con il codice, senza spiegazioni aggiuntive prima o dopo."""
    
    def get_user_prompt(self, request: str, language: str) -> str:
        """Genera il prompt utente ottimizzato"""
        spec = self.LANGUAGE_SPECS.get(language.lower(), self.LANGUAGE_SPECS['python'])
        
        return f"""Crea uno script {language} che: {request}

Requisiti:
- Codice funzionante e testato
- Commenti in italiano
- Gestione errori
- Best practices {language}

Formato output: codice {language} completo e pronto all'uso."""
