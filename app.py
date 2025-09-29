import streamlit as st
import schedule
import time
import datetime
import threading

# -------------------------------
# Job functions
# -------------------------------
def backup_database():
    log = f"[{datetime.datetime.now()}] Database backup completed."
    st.session_state.logs.append(log)

def send_report():
    log = f"[{datetime.datetime.now()}] Daily report sent successfully."
    st.session_state.logs.append(log)

# -------------------------------
# Scheduler Runner
# -------------------------------
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="SmartJob Automation", page_icon="⚡", layout="wide")

st.title("⚡ SmartJob Automation Tool")
st.subheader("Automating tasks with AI-powered scheduling")

# Initialize session state for logs
if "logs" not in st.session_state:
    st.session_state.logs = []

# Sidebar: Job setup
st.sidebar.header("🛠 Job Configuration")

job_type = st.sidebar.selectbox(
    "Select Job Type",
    ["Database Backup", "Send Report"]
)

job_time = st.sidebar.text_input("Enter Time (HH:MM)", "09:00")

if st.sidebar.button("➕ Add Job"):
    if job_type == "Database Backup":
        schedule.every().day.at(job_time).do(backup_database)
        st.sidebar.success(f"✅ Database Backup scheduled at {job_time}")
    elif job_type == "Send Report":
        schedule.every().day.at(job_time).do(send_report)
        st.sidebar.success(f"✅ Report scheduled at {job_time}")

# Start scheduler in background
if "scheduler_thread" not in st.session_state:
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    st.session_state.scheduler_thread = scheduler_thread

# Display Logs
st.header("📜 Automation Logs")
for log in st.session_state.logs[-10:]:  # show last 10 logs
    st.write(log)
