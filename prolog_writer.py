class PrologWriter:
    def __init__(self, facts_file: str = "facts.pl", rules_file: str = "rules.pl"):
        self.facts_file = facts_file
        self.rules_file = rules_file

    def write_facts(self, content: str) -> None:
        self._write_to_file(self.facts_file, content)

    def write_rules(self, content: str) -> None:
        self._write_to_file(self.rules_file, content)

    def _write_to_file(self, file_path: str, content: str) -> None:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        except IOError as e:
            print(f"Erro ao escrever no arquivo {file_path}: {e}")
