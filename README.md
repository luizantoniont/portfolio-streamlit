# Portifólio de Cientista de Dados - Aplicativo Streamlit

## Visão Geral
Um aplicativo Streamlit que apresenta meu portfólio de ciência de dados, projetos e informações profissionais.

## Pré-requisitos
- Python 3.8+
- Poetry (Gerenciamento de Dependências)

## Configuração e Instalação

### 1. Instalar Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
## Instalação via pip:
```
pip install poetry
```
### 2. Clonar o Repositório
```bash
git clone https://github.com/seunome/portfolio-streamlit.git
cd portfolio-streamlit
```

### 3. Instalar Dependências
```bash
poetry install
```

### 4. Ativar Ambiente Virtual e Executar
```bash
poetry shell
poetry run start
poetry run streamlit run src/portifolio_streamlit/app.py  # Executa o aplicativo Streamlit
```

## Comandos de Desenvolvimento
- Executar testes: `poetry run pytest`
- Executar linter: `poetry run flake8`
- Verificação de tipos: `poetry run mypy`

## Estrutura do Projeto
- `src/`: Código principal do aplicativo
- `tests/`: Testes unitários e de integração
- `data/`: Recursos de dados e projetos
- `pyproject.toml`: Configuração do projeto e dependências

## Personalização
Substitua imagens de placeholder, atualize o `projects.json` e modifique as informações pessoais nos componentes.

## Contribuição
Pull requests são bem-vindos. Para mudanças importantes, por favor, abra primeiro uma issue para discutir as mudanças propostas.
