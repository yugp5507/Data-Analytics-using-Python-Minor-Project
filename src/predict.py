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
    kmeans = joblib.load("models/kmeans_model.pkl")   # updated path
    scaler = joblib.load("models/scaler.pkl")
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

    elements.append(Paragraph(f"Total Marks: {data['total']} / 700", styles['Normal']))
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

# ---------------- INPUT SUBJECTS (UPDATED SEM 4) ----------------

java_ext_th, java_ext_pr, java_int_th, java_int_pr, java_total = subject_full("JAVA PROGRAMMING LANGUAGE")

net_ext_th, net_ext_pr, net_int_th, net_int_pr, net_total = subject_full(".NET PROGRAMMING")

mad_ext_th, mad_ext_pr, mad_int_th, mad_int_pr, mad_total = subject_full("MOBILE APPLICATION DEVELOPMENT - II")

iot_ext_th, iot_ext_pr, iot_int_th, iot_int_pr, iot_total = subject_full("INTERNET OF THINGS (IOT)")

oss_ext_th, oss_ext_pr, oss_int_th, oss_int_pr, oss_total = subject_full("ORGANIZATIONAL SOFT-SKILLS IN SOFTWARE INDUSTRY")

cc_ext_th, cc_int_th, cc_total = subject_theory_only("CERTIFICATE COURSE IN WEB DESIGNING")

bmp_ext_th, bmp_int_th, bmp_total = subject_theory_only("BHARATIYA MULYA PARAMPARA - II")

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Result & Predict", use_container_width=True):

    # Calculations
    total_marks = (
        java_total + net_total + mad_total + iot_total +
        oss_total + cc_total + bmp_total
    )

    sgpa = round((total_marks / 700) * 10, 2)
    result_status = "PASS" if total_marks >= 280 else "FAIL"

    # ML Input (ONLY TOTAL FIELDS)
    input_data = pd.DataFrame([{
        "JAVA_PROGRAMMING_LANGUAGE_Total": java_total,
        ".NET_PROGRAMMING_Total": net_total,
        "MOBILE_APPLICATION_DEVELOPMENT_-_II_Total": mad_total,
        "INTERNET_OF_THINGS_(IOT)_Total": iot_total,
        "ORGANIZATIONAL_SOFT-SKILLS_IN_SOFTWARE_INDUSTRY_Total": oss_total,
        "CERTIFICATE_COURSE_IN_WEB_DESIGNING_(HTML,JAVA_SCRIPT,CSS)_Total": cc_total,
        "BHARATIYA_MULYA_PARAMPARA_-_II_Total": bmp_total
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

    <tr><td>JAVA PROGRAMMING LANGUAGE</td><td>{java_ext_th}</td><td>{java_ext_pr}</td><td>{java_int_th}</td><td>{java_int_pr}</td><td>{java_total}</td></tr>
    <tr><td>.NET PROGRAMMING</td><td>{net_ext_th}</td><td>{net_ext_pr}</td><td>{net_int_th}</td><td>{net_int_pr}</td><td>{net_total}</td></tr>
    <tr><td>MOBILE APPLICATION DEVELOPMENT - II</td><td>{mad_ext_th}</td><td>{mad_ext_pr}</td><td>{mad_int_th}</td><td>{mad_int_pr}</td><td>{mad_total}</td></tr>
    <tr><td>INTERNET OF THINGS (IOT)</td><td>{iot_ext_th}</td><td>{iot_ext_pr}</td><td>{iot_int_th}</td><td>{iot_int_pr}</td><td>{iot_total}</td></tr>
    <tr><td>ORGANIZATIONAL SOFT-SKILLS</td><td>{oss_ext_th}</td><td>{oss_ext_pr}</td><td>{oss_int_th}</td><td>{oss_int_pr}</td><td>{oss_total}</td></tr>
    <tr><td>WEB DESIGNING COURSE</td><td>{cc_ext_th}</td><td>-</td><td>{cc_int_th}</td><td>-</td><td>{cc_total}</td></tr>
    <tr><td>BHARATIYA MULYA PARAMPARA - II</td><td>{bmp_ext_th}</td><td>-</td><td>{bmp_int_th}</td><td>-</td><td>{bmp_total}</td></tr>

    </table>

    <h3>Total Marks: {total_marks} / 700</h3>
    <h3>SGPA: {sgpa}</h3>
    <h3>Result: {result_status}</h3>
    <h3>Performance: {performance}</h3>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)

    # ---------------- PDF ----------------
    pdf_data = {
        "seat": seat,
        "name": name,
        "college": college,
        "marks": [
            ["JAVA PROGRAMMING LANGUAGE", java_ext_th, java_ext_pr, java_int_th, java_int_pr, java_total],
            [".NET PROGRAMMING", net_ext_th, net_ext_pr, net_int_th, net_int_pr, net_total],
            ["MAD-II", mad_ext_th, mad_ext_pr, mad_int_th, mad_int_pr, mad_total],
            ["IOT", iot_ext_th, iot_ext_pr, iot_int_th, iot_int_pr, iot_total],
            ["OSS", oss_ext_th, oss_ext_pr, oss_int_th, oss_int_pr, oss_total],
            ["WEB DESIGNING", cc_ext_th, "-", cc_int_th, "-", cc_total],
            ["BMP-II", bmp_ext_th, "-", bmp_int_th, "-", bmp_total]
        ],
        "total": total_marks,
        "sgpa": sgpa,
        "result": result_status,
        "performance": performance
    }

    generate_pdf(pdf_data)

    with open("result.pdf", "rb") as f:
        st.download_button("📥 Download Result PDF", f, file_name="SEM4_Result.pdf")