# Hinglish Assistant

---

## 📖 Overview

We built a Voice-AI assistant that understands and responds in Hinglish (Hindi + English mix).  
Since the Gemini API doesn't currently allow direct model fine-tuning, I used **few-shot prompting** to simulate fine-tuning behavior.

---

## 🛠 Setup

1. Install Google Generative AI Python SDK:
   ```bash
   pip install google-generativeai


# ❓ Why? Explanations

## 📄 Dataset Selection & Size

- **Size:** 20 examples to cover basic conversational domains while keeping it lightweight.
- **Domains Covered:** Greetings, casual plans, food, help requests, weather updates.
- **Style:** Natural, short, casual Hinglish (Hindi-English code-switching) to mimic real-world user conversations.


- **How the Examples Were Chosen:**
  - **Domains:** Picked from common everyday situations like greetings, casual plans, food and drink discussions, help requests, and weather updates.
  - **Style:** 
    - Casual, friendly, and short-form sentences.
    - Natural Hinglish code-switching — mixing Hindi and English the way real users speak.
  - **Length:** 
    - Short, 1–2 line dialogues to keep the prompts compact.
    - Long enough to show natural code-switch patterns but short enough for fast inference.
  - **Reasoning:** 
    - These types of conversations are very frequent in voice assistants (e.g., casual queries, weather checks, help requests).
    - Training the model on these examples helps it learn the typical structure and tone needed for Hinglish-speaking users.

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
Assistant: Shayad friends ke saath outing karun, ya thoda rest karun. Tumhara kya plan hai?
```

### 2. Prompt
```
User: Thoda mausam ka update dedo.
```

**Response:**
```
Assistant: Aaj mausam kaafi pleasant hai, halka sa cloudy feel ho raha hai. Perfect chai ke saath enjoy karne ke liye!
```

### 3. Prompt
```
User: Dinner ke liye kya suggest karoge?
```

**Response:**
```
Assistant: Ek simple dal chawal ya light pasta dinner ke liye perfect rahega. Thoda healthy bhi aur tasty bhi!
```



## 📊 How We Would Evaluate Quality in Production

- **Initial Phase:**
- **Human Review:**
  - Check if the responses feel natural and fluid.
  - Confirm that Hinglish code-switching happens appropriately.
  - Ensure tone matches friendly, casual assistant behavior.

- **Later Phase:**
- **Automated Evaluation Metrics:**
  - Monitor user satisfaction feedback (ratings/reviews).

---

✅ This completes the Design Rationale part of the project in a clean and professional format.


