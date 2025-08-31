# 📧 Email Classifier

Um classificador inteligente de e-mails que identifica se um e-mail é **Produtivo** ou **Improdutivo** e sugere respostas automáticas personalizadas com IA.

---

## ✨ Funcionalidades
- 🔍 Classificação de e-mails usando modelos da Hugging Face (DistilBERT) e OpenAI.
- 🤖 Geração de respostas automáticas inteligentes (Flan-T5 / Hugging Face API).
- 🌐 Interface web simples e intuitiva (HTML + CSS + JS).
- 🚀 Pronto para rodar localmente ou em produção.

---

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone git@github.com:LeandroMedvedev/email-classifier.git
cd email-classifier
```

### 2. Crie um ambiente virtual e instale as dependências
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Configure variáveis de ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```env
OPENAI_API_KEY="sua_chave_openai"
HF_API_TOKEN="seu_token_huggingface"
```

👉 Como obter:
* 🔑 OpenAI API Key: [OpenAI](https://platform.openai.com/)
* 🔑 Hugging Face Token: [Hugging Face](https://huggingface.co/settings/tokens)

---

### ▶️ Executando a aplicação
```bash
uvicorn src.app:app --reload
```

Depois, abra no navegador:
👉 http://localhost:8000  

---

### 🛠 Tecnologias

* Python 3.9+
* FastAPI
* Hugging Face Transformers
* Flan-T5 (local e Hugging Face API)
* HTML, CSS e JS

---

### 🤝 Contribuições
Sinta-se à vontade para abrir issues ou enviar PRs! 🙌  

### 📜 Licença
MIT License
