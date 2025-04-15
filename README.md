# New Prolog Rag

**NewPrologRag** is a hybrid framework that integrates Prolog-based symbolic reasoning with modern Large Language Models (LLMs). It enables users to define knowledge bases using Prolog and leverage LLMs for advanced reasoning tasks, combining the strengths of symbolic and statistical AI.

## Features

- **Prolog Integration**: Utilize `.pl` files (`facts.pl`, `rules.pl`) to define facts and rules for logical reasoning.
- **LLM Client**: Interface with LLMs through `llm_client.py` to enhance reasoning capabilities.
- **Prolog Writer**: Generate or modify Prolog code dynamically using `prolog_writer.py`.
- **Main Execution**: Orchestrate the interaction between Prolog knowledge bases and LLMs via `main.py`.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [SWI-Prolog](https://www.swi-prolog.org/) installed and accessible in your system's PATH

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MateusFernandes25/NewPrologRag.git
   cd NewPrologRag
   ```

2. **Set up a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: Ensure that `requirements.txt` exists and lists all necessary Python packages.*

## Usage

1. **Define your knowledge base**:

   - Edit `facts.pl` to include your Prolog facts.
   - Edit `rules.pl` to define the logical rules.

2. **Configure the LLM client**:

   - Update `llm_client.py` with your LLM API credentials and parameters.

3. **Run the main program**:

   ```bash
   python main.py
   ```

   *This will load the Prolog knowledge base, interact with the LLM as configured, and perform reasoning tasks.*

## Project Structure

```
NewPrologRag/
├── .env                # Environment variables (e.g., API keys)
├── .idea/              # IDE configuration files
├── __pycache__/        # Python cache files
├── facts.pl            # Prolog facts
├── rules.pl            # Prolog rules
├── llm_client.py       # LLM client interface
├── prolog_writer.py    # Prolog code generator
├── main.py             # Main execution script
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
