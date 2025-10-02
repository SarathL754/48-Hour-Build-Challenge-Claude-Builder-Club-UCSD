#!/usr/bin/env python
import streamlit as st
import warnings
from datetime import datetime
from dotenv import load_dotenv
from crew import Innervoiceai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
load_dotenv()

st.set_page_config(page_title="InnerVoice AI", page_icon="🧘", layout="centered")

st.title("🧘 InnerVoice AI")
st.subheader("Break free from overthinking by simulating your inner voices")

with st.form("decision_form"):
    user_decision = st.text_area("🧠 What decision are you struggling with?")
    user_values = st.text_input("💡 What are your personal values or priorities?")

    submitted = st.form_submit_button("Get InnerVoice Recommendation")

if submitted:
    if not user_decision or not user_values:
        st.warning("⚠️ Please provide both your decision and your values.")
    else:
        with st.spinner("🧠 Inner voices are debating..."):
            try:
                inputs = {
                    "user_decision": user_decision,
                    "user_values": user_values,
                    "current_year": str(datetime.now().year)
                }

                result = Innervoiceai().crew().kickoff(inputs=inputs)

                # ✅ Just convert to string and show
                st.success("✅ Your inner voices have reached a decision!")
                st.write(str(result))


            except Exception as e:
                st.error(f"❌ An error occurred while running the crew: {e}")
