import streamlit as st
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "bmi_records.csv"

st.set_page_config(page_title="Advanced BMI Calculator", layout="centered")

st.title(" Advanced BMI Calculator")
st.write("Track your BMI, view history, and analyze trends ")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Name", "Weight", "Height", "BMI", "Category", "Date"])
    df.to_csv(FILE_NAME, index=False)

st.subheader("📥 Enter Your Details")

name = st.text_input("Enter Your Name")
weight = st.number_input("Enter Weight (kg)", min_value=1.0, max_value=300.0)
height = st.number_input("Enter Height (m)", min_value=0.5, max_value=2.5)

if st.button("Calculate BMI"):
    if name.strip() == "":
        st.error("Please enter your name.")
    else:
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        st.success(f"Your BMI is {bmi:.2f}")
        st.info(f"Category: {category}")

        new_data = pd.DataFrame([[name, weight, height, round(bmi,2), category,
                                  datetime.now().strftime("%Y-%m-%d %H:%M:%S")]],
                                columns=["Name", "Weight", "Height", "BMI", "Category", "Date"])

        new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)

st.subheader(" BMI History")

df = pd.read_csv(FILE_NAME)

if not df.empty:
    st.dataframe(df)

    st.subheader(" Individual BMI Trend")

    selected_user = st.selectbox("Select User", df["Name"].unique())

    user_data = df[df["Name"] == selected_user]

    if len(user_data) > 0:
        plt.figure()
        plt.plot(user_data["Date"], user_data["BMI"], marker='o')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.title(f"BMI Trend for {selected_user}")
        plt.tight_layout()
        st.pyplot(plt)

        st.subheader(" Overall Statistics")

    avg_bmi = df["BMI"].mean()
    max_bmi = df["BMI"].max()
    min_bmi = df["BMI"].min()

    col1, col2, col3 = st.columns(3)
    col1.metric("Average BMI", f"{avg_bmi:.2f}")
    col2.metric("Highest BMI", f"{max_bmi:.2f}")
    col3.metric("Lowest BMI", f"{min_bmi:.2f}")

else:
    st.info("No records found. Start by adding your BMI data!")

st.markdown("---")
st.write("Made with using Streamlit")
