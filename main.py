"""
Main execution script to generate Prolog facts and rules using an LLM.
Author: Mateus Fernandes dos Santos
"""

from llm_client import LLMClient
from prolog_writer import PrologWriter

def main():

    api_key = os.getenv("OPENAI_API_KEY")
    facts_file="facts.pl"
    rules_file="rules.pl"
    #input_text = input("Type a sentence:\n> ")
    input_text = "Diana is the England Queen"

    #input_question = input("Type a question:\n> ")
    input_question = "Who is England Queen?"

    client = LLMClient(api_key)
    response = client.generate_prolog_knowledge(input_text)

    if response:
        facts, rules = client.parse_response(response)
        writer = PrologWriter(facts_file,rules_file)
        writer.write_facts(facts)
        writer.write_rules(rules)
        query = client.generate_prolog_query(input_question,facts_file,rules_file)
        prolog_answer = client.run_prolog_query(query,facts_file,rules_file)
        answer = client.generate_prolog_answer(input_question,prolog_answer)
        print(query)
        print(prolog_answer)
        print(answer)
    else:
        print("Couldn't get a reply from the LLM.")

if __name__ == "__main__":
    main()



