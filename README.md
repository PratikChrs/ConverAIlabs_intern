# Hinglish Voice-AI — Mini Fine-Tuning Project

---

## 📖 Overview

We built a Voice-AI assistant that understands and responds in Hinglish (Hindi + English mix).  
Since the Gemini API doesn't currently allow direct model fine-tuning, we used **few-shot prompting** to simulate fine-tuning behavior.

---

## 🛠 Setup

1. Install Google Generative AI Python SDK:
   ```bash
   pip install google-generativeai


# ❓ Why? Explanations

## 📄 Dataset Selection & Size

- **Size:** 10–20 examples to cover basic conversational domains while keeping it lightweight.
- **Domains Covered:** Greetings, casual plans, food, help requests, weather updates.
- **Style:** Natural, short, casual Hinglish (Hindi-English code-switching) to mimic real-world user conversations.

---

## 🧠 Model Choice

- **Model Used:** `gemini-1.5-flash`
- **Why?**
  - Extremely fast for real-time Voice-AI needs.
  - Handles few-shot prompting effectively.
  - Cost-efficient and lighter compared to heavier models like `gemini-1.5-pro`.

---

## ⚙️ Hyperparameters

- **Fine-Tuning:**  
  Not applicable (Gemini models currently don’t support direct fine-tuning).
  
- **Few-Shot Prompting:**  
  Simulated fine-tuning by including examples inside the prompt.

---

## 📝 Prompt Design

- **Approach:**  
  Few-shot examples are added inside the prompt before the user's real input.

- **Prompt Structure:**
   
   User: [example input]
   Assistant: [example output]

   User: [new user input]
   Assistant: [model generates...]


## 🔥 Sample Outputs from inference.py

### 1. Prompt
```
User: Sunday ka kya plan hai?
```

**Response:**
```
Shayad friends ke saath outing karun, ya thoda rest karun. Tumhara kya plan hai?
```

### 2. Prompt
```
User: Thoda mausam ka update dedo.
```

**Response:**
```
Aaj mausam kaafi pleasant hai, halka sa cloudy feel ho raha hai. Perfect chai ke saath enjoy karne ke liye!
```

### 3. Prompt
```
User: Dinner ke liye kya suggest karoge?
```

**Response:**
```
Ek simple dal chawal ya light pasta dinner ke liye perfect rahega. Thoda healthy bhi aur tasty bhi!
```

## 📊 Evaluation Plan

* **Initial Phase:** Human review for checking fluency, Hinglish naturalness, and tone consistency.
* **Later Phase:** Basic automated metrics like BLEU/ROUGE to assess Hinglish response quality.
