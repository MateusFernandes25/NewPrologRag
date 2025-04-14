import os
from typing import Tuple, Optional
from openai import OpenAI

class LLMClient:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("A chave de API é obrigatória.")
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)

    def generate_prolog_knowledge(self, text: str) -> Optional[str]:
        prompt = f"""
You are a specialist in logic and Prolog. From the phrase below, generate:

1. FACTS in Prolog

2. RULES (functions) in Prolog

%IMPORTANT: Add docstrings for each predicate and logic with one example in the same line. Example: born_in(Name, Country) - represents a person's country of birth 

        
Format:
===FACTS===        
% facts here
...
===RULES===
%rules here
...

Sentence: "{text}"
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=800,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None

    def parse_response(self, content: str) -> Tuple[str, str]:
        try:
            parts = content.split("===RULES===")
            facts = parts[0].replace("===FACTS===", "").strip()
            rules = parts[1].strip()
            return facts, rules
        except IndexError:
            raise ValueError("Error")


    def generate_prolog_query(self, text: str, facts_path: str,rules_path: str) -> Optional[str]:
        import re
        def coletar_docstrings(*a):return [d for f in a for d in re.findall(r"/\*\*.*?\*/",open(f,encoding='utf-8').read(),re.DOTALL)]+["\n".join(g) for f in a for g in [re.findall(r"(?m)(^%!?[^\n]*)",open(f,encoding='utf-8').read())] if g]
        docs = coletar_docstrings(facts_path, rules_path)
        prompt = f"""
        Instructions: Using STRICTLY the Prolog docustring database provided below, generate a query in Prolog 
        
        \n\nProlog Base:\n\n{docs}
        
        that strictly answers the following question: '{text}' 
        
        You must use only the facts and rules available in the database:    
            Respond exclusively in one of the following formats: 
                - If the query can be generated:
                    true: <prolog_query>
                - If the query cannot be generated: 
                    false: <detailed_reason>
        Provide a clear and categorical response. Do not entertain ambiguities or alternatives.'''
        Ensure that the variables are properly instantiated before being used in operations such as comparisons or calculations'''
        Using STRICTLY the Prolog docustring database        

        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=800,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None


    def run_prolog_query(self, query: str, facts_path: str,rules_path: str) -> Optional[str]:
        from pyswip import Prolog
        if "Request failed" in query or "Unexpected response format" in query:
            return query
        if 'true' in query:
            query = query[query.find(":")+2:-1].strip().replace('"','')
            try:
                prolog = Prolog()
                prolog.consult(facts_path)  # Consult the Prolog file.
                prolog.consult(rules_path)  # Consult the Prolog file.
                results = list(prolog.query(query))
                return results
            except Exception as e:
                return f"Prolog execution failed: {e}"
        else:
            try:
                final = query[query.find(":")+1:-1].strip()
                return final
            except (KeyError, IndexError) as e:
                return f"Unexpected response format: {e}"



    def generate_prolog_answer(self, question: str, prolog_answer: str) -> Optional[str]:
        prompt = f"""
        Create a Answer concise about the question using ONLY de data. 
            Based only in the data.
        
            Question: {question}
            Data: {prolog_answer}
            Answer:
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                max_tokens=800,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None
