# 🤖 Chatbot de Apoio à Gravidez — FOCA IA

Este projeto é um **chatbot desenvolvido em Rasa** com o objetivo de **fornecer orientações e informações básicas sobre gravidez**, incluindo sintomas, alimentação, exames e exercícios recomendados para gestantes.

O bot foi projetado em **português**, com foco em **respostas simples, educativas e de apoio**, sem substituir a consulta médica.  
Criado por **FOCA IA** como parte de uma iniciativa de **assistência digital em saúde**.

---

## 🧠 Funcionalidades Principais

- 👋 Cumprimentos e despedidas naturais em português.  
- 💬 Orientações sobre sintomas nos diferentes trimestres da gravidez.  
- 🍎 Recomendações alimentares seguras para gestantes.  
- 🧘 Sugestões de exercícios leves e saudáveis.  
- 🧪 Indicação de exames importantes durante a gestação.  
- 🧩 Suporte a múltiplas intenções e entidades (trimestre, tipo de sintoma, medicamento, etc).

---

## ⚙️ Estrutura do Projeto

```
📦 chatbot-gravidez
 ┣ 📂 data/
 ┃ ┗ 📜 stories.yml        # Histórias de conversação
 ┃ ┗ 📜 rules.yml          # Regras de comportamento do bot
 ┣ 📂 models/              # Modelos treinados (gerado automaticamente)
 ┣ 📂 actions/             # Ações personalizadas em Python (se aplicável)
 ┣ 📜 domain.yml           # Intenções, entidades e respostas
 ┣ 📜 config.yml           # Configuração de pipeline do NLU e políticas
 ┣ 📜 credentials.yml      # Credenciais de canais (Telegram, etc)
 ┣ 📜 endpoints.yml        # Configuração de endpoints
 ┣ 📜 README.md            # Este ficheiro
 ┗ 📜 .gitignore
```

---

## 🚀 Como Executar o Projeto

### 🧩 1. Instalar o Rasa

Certifica-te de ter o Python 3.8 ou superior.  
Depois instala o Rasa:

```bash
pip install rasa
```

---

### ⚙️ 2. Treinar o modelo

Na raiz do projeto, executa:

```bash
rasa train
```

Isso vai gerar um modelo na pasta `models/`.

---

### 💬 3. Executar o chatbot em modo terminal

```bash
rasa shell
```

---

### 🌐 4. (Opcional) Executar o servidor e as ações personalizadas

Em dois terminais separados:

```bash
rasa run --enable-api
```

e

```bash
rasa run actions
```

---

## 🗣️ Intenções Suportadas

| Intenção        | Exemplo de Frase do Usuário |
|-----------------|-----------------------------|
| `saudacao`      | "Olá", "Boa tarde", "Oi" |
| `despedida`     | "Tchau", "Até logo" |
| `sintomas`      | "Quais são os sintomas no primeiro trimestre?" |
| `alimentacao`   | "O que devo comer na gravidez?" |
| `exercicios`    | "Posso fazer exercícios grávida?" |
| `exames`        | "Quais exames são feitos no segundo trimestre?" |
| `affirm` / `deny` | "Sim", "Não", "Certo" |
| `mood_unhappy`  | "Estou triste", "Não me sinto bem" |

---

## 🧩 Respostas do Bot

Exemplo de interações:

```
👩 Usuária: Quais são os sintomas do primeiro trimestre?
🤖 Bot: Os sintomas mais comuns no primeiro trimestre incluem náuseas, cansaço e sensibilidade nos seios.
```

```
👩 Usuária: O que devo comer?
🤖 Bot: É importante ter uma dieta rica em proteínas, ferro e ácido fólico durante a gravidez.
```

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT** — uso livre para fins acadêmicos, educativos e sociais.  
Créditos a **FOCA IA** e contribuições de **Embar**.

---

## ✨ Autor

**Desenvolvido por:** Embar — Projeto FOCA IA  
📧 Email: [coloca teu email aqui]  
🌐 GitHub: [https://github.com/teu-usuario](https://github.com/teu-usuario)
