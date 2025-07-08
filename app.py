# import streamlit as st
# import pandas as pd
# import os
#
# st.set_page_config(page_title="DNA-Free Cancer Risk Tool", layout="centered")
# st.title("🧪 DNA-Free Cancer Risk Tool")
# st.markdown("Enter your health details to assess risk.")
#
# # --- Input ---
# age = st.slider("Age", 10, 100, 30)
# gender = st.radio("Gender", ["Male", "Female", "Other"])
# smoking = st.selectbox("Do you smoke?", ["no", "yes"])
# alcohol = st.selectbox("Do you consume alcohol?", ["no", "yes"])
# family_history = st.selectbox("Any family history of cancer?", ["no", "yes"])
#
# symptoms = st.multiselect(
#     "Select any symptoms you have:",
#     ["Unexplained weight loss", "Persistent cough", "Lump/swelling",
#      "Fatigue", "Skin changes", "Fever", "Bleeding", "Pain"]
# )
#
# # --- Predict Function ---
# def assess_risk(age, smoking, alcohol, family_history, symptoms):
#     score = 0
#     if age > 50:
#         score += 2
#     if smoking == "yes":
#         score += 2
#     if alcohol == "yes":
#         score += 1
#     if family_history == "yes":
#         score += 2
#     score += len(symptoms)
#
#     if score <= 2:
#         return "Low"
#     elif score <= 5:
#         return "Moderate"
#     else:
#         return "High"
#
# # --- On Submit ---
# if st.button("Assess Risk"):
#     risk = assess_risk(age, smoking, alcohol, family_history, symptoms)
#
#     # Show result
#     st.success(f"🎯 Predicted Cancer Risk: **{risk}**")
#
#     # Save to CSV
#     data = {
#         "age": age,
#         "gender": gender,
#         "smoking": smoking,
#         "alcohol": alcohol,
#         "family_history": family_history,
#         "symptoms": ', '.join(symptoms),
#         "risk": risk
#     }
#
#     df = pd.DataFrame([data])
#     file_path = "user_inputs.csv"
#     if os.path.exists(file_path):
#         df.to_csv(file_path, mode='a', index=False, header=False)
#     else:
#         df.to_csv(file_path, index=False)
#
#     if st.checkbox("Show all saved entries"):
#         st.write(pd.read_csv(file_path))






import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(page_title="DNA-Free Cancer Risk Tool", layout="centered")

st.title("🧪 DNA-Free Cancer Risk Tool")
st.markdown("Enter your health details to assess risk.")

# Collect user input
age = st.slider("Age", 10, 100, 30)
gender = st.radio("Gender", ["Male", "Female", "Other"])
smoking = st.selectbox("Do you smoke?", ["no", "yes"])
alcohol = st.selectbox("Do you consume alcohol?", ["no", "yes"])
family_history = st.selectbox("Any family history of cancer?", ["no", "yes"])

symptoms = st.multiselect(
    "Select any symptoms you have:",
    ["Unexplained weight loss", "Persistent cough", "Lump/swelling",
     "Fatigue", "Skin changes", "Fever", "Bleeding", "Pain"]
)

# Predict risk when button is clicked
if st.button("Assess Risk"):
    data = {
        "age": age,
        "gender": gender.lower(),
        "smoking": smoking,
        "alcohol": alcohol,
        "family_history": family_history,
        "symptoms": symptoms
    }

    # Save data to CSV
    df = pd.DataFrame([data])
    file_path = "user_inputs.csv"
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', index=False, header=False)
    else:
        df.to_csv(file_path, index=False)

    st.info("✅ Your data has been saved successfully!")

    # Send to backend (if running)
    try:
        response = requests.post("http://localhost:5000/predict", json=data)
        if response.status_code == 200:
            risk = response.json().get("risk", "Unknown")
            st.success(f"🎯 Predicted Cancer Risk: **{risk}**")
        else:
            st.error("❌ Server error while predicting risk.")
    except Exception as e:
        st.warning(f"⚠️ Could not connect to backend. Showing only saved data.")

# Show saved data
if os.path.exists("user_inputs.csv"):
    with open("user_inputs.csv", "rb") as file:
        st.download_button(
            label="📥 Download All Submitted Data (CSV)",
            data=file,
            file_name="user_inputs.csv",
            mime="text/csv"
        )
    #
    # if st.checkbox("📋 Show all entries"):
    #     st.dataframe(pd.read_csv("user_inputs.csv"))
