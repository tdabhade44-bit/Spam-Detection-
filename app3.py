from flask import Flask, render_template, request, redirect, session, send_file
import sqlite3
from fpdf import FPDF
import os

app = Flask(__name__)
app.secret_key = "secret123"

# -------------------- DATABASE --------------------
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS history (text TEXT, result TEXT)")

spam_words = ["win", "free", "offer", "money", "click", "urgent"]

# -------------------- LOGIN --------------------
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "123":
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Login"
    return render_template("login.html")

# -------------------- DASHBOARD --------------------
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    result = ""
    confidence = 0
    highlighted = ""

    if request.method == "POST":
        text = request.form["text"].lower()
        words = text.split()
        spam_count = sum(word in spam_words for word in words)
        prob = spam_count / len(words) if len(words) > 0 else 0

        result = "SPAM" if prob > 0.2 else "NOT SPAM"
        confidence = round(prob * 100, 2)

        # Highlight spam words
        highlighted = text
        for word in spam_words:
            if word in text:
                highlighted = highlighted.replace(word, f"[{word}]")

        # Save to DB
        cursor.execute("INSERT INTO history VALUES (?,?)", (text, result))
        conn.commit()

    # Fetch history
    cursor.execute("SELECT * FROM history")
    data = cursor.fetchall()

    return render_template("dashboard.html", result=result, confidence=confidence, highlighted=highlighted, data=data)

# -------------------- PDF REPORT (ASCII-safe) --------------------
@app.route("/report")
def report():
    cursor.execute("SELECT * FROM history")
    data = cursor.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Spam Detection Report", ln=True, align="C")
    pdf.ln(10)

    for row in data:
        # Convert text to ASCII to avoid Unicode errors
        safe_text = row[0].encode('ascii', 'ignore').decode('ascii')
        pdf.cell(200, 10, f"{safe_text} - {row[1]}", ln=True)

    pdf_file = "report.pdf"
    pdf.output(pdf_file)

    return send_file(pdf_file, as_attachment=True)

# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)