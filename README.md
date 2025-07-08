# 🔪 DNA-Free Cancer Risk Tool

An AI-powered web application that predicts cancer risk using health symptoms, lifestyle choices, and family history—**without the need for DNA testing**. Built for accessibility, especially in **rural India**, this tool offers early detection support through an easy-to-use interface.

---

## 🚀 Features

* 🧠 **AI-based risk prediction** via backend API (Flask)
* 📋 **User-friendly input** with Streamlit frontend
* 📦 **Auto-logs all submissions** to CSV and Excel
* 💾 **Downloadable reports** with correct column headers
* ⚙️ Ready for integration with ML model (backend API: `/predict`)

---

## 📸 Screenshot

Here’s a quick look at the tool UI:

![Cancer Risk Tool UI](https://github.com/user-attachments/assets/6e1a0889-fb7d-4a62-82ea-fb34b05a39f7)

---

## 💠 Tech Stack

| Frontend  | Backend            | Storage     | Libraries                        |
| --------- | ------------------ | ----------- | -------------------------------- |
| Streamlit | Flask (Python API) | CSV / Excel | `pandas`, `requests`, `openpyxl` |

---

## 🧬 How It Works

1. User enters health data (age, gender, symptoms, etc.)
2. Data is saved locally (`user_inputs.csv`)
3. A POST request is sent to the Flask API (`/predict`)
4. Risk score is returned and displayed
5. User can download data or view previous records

---

## 📁 Project Structure

```
dna_free_cancer_risk_tool/
│
├── streamlit_ui/
│   └── app.py             # Streamlit frontend
│
├── backend/
│   └── app.py             # Flask backend (with /predict)
│
├── user_inputs.csv        # Auto-saved user data
├── README.md              # Project documentation
```

---

## 📦 Installation & Run

### 1. Install dependencies:

```bash
pip install streamlit flask pandas openpyxl requests
```

### 2. Start the backend (Flask):

```bash
cd backend
python app.py
```

### 3. Start the frontend (Streamlit):

```bash
cd ../streamlit_ui
streamlit run app.py
```

---

## 🧠 Future Improvements

* ✅ AI Model Integration for actual prediction logic
* 🌍 Multilingual UI for rural outreach
* 🏥 Sync with health databases or cloud

---

## 🙇‍♀️ Creator

**Amisha Rahangdale**
🔗 [LinkedIn](https://linkedin.com/in/amisha-rahangdale) | 💻 Python • AI • Healthcare Tech

---
