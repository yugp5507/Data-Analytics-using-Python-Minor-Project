import streamlit as st
import pandas as pd
import joblib

# PDF libraries
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Student Result System", layout="centered")

st.title("🎓 Student Result & Performance Predictor")

# ---------------- LOAD MODELS ----------------
@st.cache_resource
def load_models():
    kmeans = joblib.load("..\\models\\kmeans_model.pkl")
    scaler = joblib.load("..\\models\\scaler.pkl")
    return kmeans, scaler

kmeans, scaler = load_models()

# ---------------- PDF FUNCTION ----------------
def generate_pdf(data, filename="result.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("COLLEGE RESULT MARKSHEET", styles['Title']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Seat Number: {data['seat']}", styles['Normal']))
    elements.append(Paragraph(f"Name: {data['name']}", styles['Normal']))
    elements.append(Paragraph(f"College: {data['college']}", styles['Normal']))
    elements.append(Spacer(1, 10))

    table_data = [["Subject", "External Theory", "External Practical", "Internal Theory", "Internal Practical", "Total Marks"]] + data["marks"]

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))

    elements.append(table)
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Total Marks: {data['total']} / 600", styles['Normal']))
    elements.append(Paragraph(f"SGPA: {data['sgpa']}", styles['Normal']))
    elements.append(Paragraph(f"Result: {data['result']}", styles['Normal']))
    elements.append(Paragraph(f"Performance: {data['performance']}", styles['Normal']))

    doc.build(elements)

# ---------------- STUDENT INFO ----------------
st.subheader("👤 Student Information")

seat = st.text_input("Seat Number")
name = st.text_input("Student Name")
college = st.text_input("College Name")

# ---------------- SUBJECT INPUT ----------------
st.subheader("📊 Enter Marks")

def subject_full(subject):
    st.markdown(f"### {subject}")
    col1, col2 = st.columns(2)

    with col1:
        ext_th = st.number_input(f"{subject} External Theory", 0, key=subject+"1")
        ext_pr = st.number_input(f"{subject} External Practical", 0, key=subject+"2")

    with col2:
        int_th = st.number_input(f"{subject} Internal Theory", 0, key=subject+"3")
        int_pr = st.number_input(f"{subject} Internal Practical", 0, key=subject+"4")

    total = ext_th + ext_pr + int_th + int_pr
    return ext_th, ext_pr, int_th, int_pr, total


def subject_theory_only(subject):
    st.markdown(f"### {subject}")
    col1, col2 = st.columns(2)

    with col1:
        ext_th = st.number_input(f"{subject} External Theory", 0, key=subject+"5")

    with col2:
        int_th = st.number_input(f"{subject} Internal Theory", 0, key=subject+"6")

    total = ext_th + int_th
    return ext_th, int_th, total

# ---------------- INPUT SUBJECTS ----------------
awd_ext_th, awd_ext_pr, awd_int_th, awd_int_pr, awd_total = subject_full("ADVANCE WEB TECHNOLOGY")

wfs_ext_th, wfs_ext_pr, wfs_int_th, wfs_int_pr, wfs_total = subject_full("WEB FRAMEWORK AND SERVICES")

net_ext_th, net_ext_pr, net_int_th, net_int_pr, net_total = subject_full(".NET TECHNOLOGY")

los_ext_th, los_ext_pr, los_int_th, los_int_pr, los_total = subject_full("LINUX OPERATING SYSTEM")

nt_ext_th, nt_int_th, nt_total = subject_theory_only("NETWORK TECHNOLOGY")

# CERTIFICATE COURSE (no practical)
cc_ext_th, cc_int_th, cc_total = subject_theory_only("CERTIFICATE COURSE")

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Result & Predict", use_container_width=True):

    # Calculations
    total_marks = awd_total + wfs_total + net_total + los_total + nt_total + cc_total
    sgpa = round((total_marks / 550) * 10, 2)
    result_status = "PASS" if total_marks >= 240 else "FAIL"

    # ML Input
    input_data = pd.DataFrame([{
        "AWD_Total": awd_total,
        "WFS_Total": wfs_total,
        ".NET_Total": net_total,
        "LOS_Total": los_total,
        "NT_Total": nt_total,
        "CC_Total": cc_total
    }])

    scaled = scaler.transform(input_data)
    cluster = kmeans.predict(scaled)[0]

    performance_map = {
        1: "🌟 High Performer",
        0: "👍 Average Performer",
        2: "⚠️ Needs Improvement"
    }

    performance = performance_map.get(cluster, "Unknown")

    # ---------------- HTML MARKSHEET ----------------
    st.markdown("---")

    html = f"""
    <div style="border:2px solid black; padding:20px; border-radius:10px">
    <h2 style="text-align:center;">COLLEGE RESULT MARKSHEET</h2>

    <p><b>Seat Number:</b> {seat}</p>
    <p><b>Name:</b> {name}</p>
    <p><b>College:</b> {college}</p>

    <table border="1" style="width:100%; text-align:center; border-collapse: collapse;">

    <tr>
    <th>Subject</th>
    <th>External Theory</th>
    <th>External Practical</th>
    <th>Internal Theory</th>
    <th>Internal Practical</th>
    <th>Total Marks</th>
    </tr>

    <tr>
    <td>ADVANCE WEB TECHNOLOGY</td>
    <td>{awd_ext_th}</td>
    <td>{awd_ext_pr}</td>
    <td>{awd_int_th}</td>
    <td>{awd_int_pr}</td>
    <td>{awd_total}</td>
    </tr>

    <tr>
    <td>WEB FRAMEWORK AND SERVICES</td>
    <td>{wfs_ext_th}</td>
    <td>{wfs_ext_pr}</td>
    <td>{wfs_int_th}</td>
    <td>{wfs_int_pr}</td>
    <td>{wfs_total}</td>
    </tr>

    <tr>
    <td>.NET TECHNOLOGY</td>
    <td>{net_ext_th}</td>
    <td>{net_ext_pr}</td>
    <td>{net_int_th}</td>
    <td>{net_int_pr}</td>
    <td>{net_total}</td>
    </tr>

    <tr>
    <td>LINUX OPERATING SYSTEM</td>
    <td>{los_ext_th}</td>
    <td>{los_ext_pr}</td>
    <td>{los_int_th}</td>
    <td>{los_int_pr}</td>
    <td>{los_total}</td>
    </tr>

    <tr>
    <td>NETWORK TECHNOLOGY</td>
    <td>{nt_ext_th}</td>
    <td>-</td>
    <td>{nt_int_th}</td>
    <td>-</td>
    <td>{nt_total}</td>
    </tr>

    <tr>
    <td>CERTIFICATE COURSE</td>
    <td>{cc_ext_th}</td>
    <td>-</td>
    <td>{cc_int_th}</td>
    <td>-</td>
    <td>{cc_total}</td>
    </tr>

    </table>

    <h3>Total Marks: {total_marks} / 550</h3>
    <h3>SGPA: {sgpa}</h3>
    <h3>Result: {result_status}</h3>
    <h3>Performance: {performance}</h3>
    </div>
    <br>
    """

    st.markdown(html, unsafe_allow_html=True)

    # ---------------- PDF DOWNLOAD ----------------
    pdf_data = {
        "seat": seat,
        "name": name,
        "college": college,
        "marks": [
            ["ADVANCE WEB TECHNOLOGY", awd_ext_th, awd_ext_pr, awd_int_th, awd_int_pr, awd_total],
            ["WEB FRAMEWORK AND SERVICES", wfs_ext_th, wfs_ext_pr, wfs_int_th, wfs_int_pr, wfs_total],
            [".NET TECHNOLOGY", net_ext_th, net_ext_pr, net_int_th, net_int_pr, net_total],
            ["LINUX OPERATING SYSTEM", los_ext_th, los_ext_pr, los_int_th, los_int_pr, los_total],
            ["NETWORK TECHNOLOGY", nt_ext_th, "-", nt_int_th, "-", nt_total],
            ["CERTIFICATE COURSE", cc_ext_th, "-", cc_int_th, "-", cc_total]
        ],
        "total": total_marks,
        "sgpa": sgpa,
        "result": result_status,
        "performance": performance
    }

    generate_pdf(pdf_data)

    with open("result.pdf", "rb") as f:
        st.download_button("📥 Download Result PDF", f, file_name="Student_Result.pdf")