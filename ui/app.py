import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.product_manager import product_manager
from agents.developer import developer
from agents.designer import designer
from agents.marketer import marketer

import streamlit as st
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="🧠 Autonomous AI Brainstormer", layout="wide")

st.title("🧠 Autonomous AI Brainstorming System")
st.markdown("Simulate a team of AI agents collaboratively ideating on your startup or product idea.")

idea = st.text_area("💡 Enter your idea:", height=150, placeholder="e.g., A voice-based journaling app that summarizes your day")

# --- Function to format results ---
def format_results_as_text(results_dict):
    output = ""
    for role, response in results_dict.items():
        output += f"### {role} Response\n\n{response}\n\n"
    return output

# --- PDF Export Function ---
def export_as_pdf_buffer(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    buffer = BytesIO(pdf_bytes)
    return buffer


# --- Main Execution ---
if st.button("Generate Brainstorm"):
    if idea.strip() == "":
        st.warning("Please enter an idea to proceed.")
    else:
        results = {}

        with st.spinner("Product Manager thinking..."):
            pm_output = product_manager(idea)
        st.subheader("📋 Product Manager")
        st.markdown(pm_output)
        results["Product Manager"] = pm_output

        with st.spinner("Developer analyzing..."):
            dev_output = developer(pm_output)
        st.subheader("👨‍💻 Developer")
        st.markdown(dev_output)
        results["Developer"] = dev_output

        with st.spinner("Designer sketching..."):
            design_output = designer(pm_output)
        st.subheader("🎨 Designer")
        st.markdown(design_output)
        results["Designer"] = design_output

        with st.spinner("Marketer planning..."):
            market_output = marketer(pm_output)
        st.subheader("📈 Marketer")
        st.markdown(market_output)
        results["Marketer"] = market_output

        # --- Export Results ---
        st.markdown("---")
        st.subheader("⬇️ Export Your Brainstorming Report")

        formatted_text = format_results_as_text(results)

        st.download_button("Download as .md", formatted_text, file_name="brainstorm.md")
        st.download_button("Download as .txt", formatted_text, file_name="brainstorm.txt")

        pdf_buffer = export_as_pdf_buffer(formatted_text)
        st.download_button("Download PDF", pdf_buffer, file_name="brainstorm.pdf", mime="application/pdf")
