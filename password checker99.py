import re
import streamlit as st  # type: ignore

#page styling
st.set_page_cofig(page_title="Password Strength Checker By Fariha Iqbal", page_icon="🌘", layout="centered")

#custom css
st.markdown("""
<style> 
     .main {text-align: centre;}
     .stTextInput {width: 60% !important; margin: auto; }
     .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px; }
     .st Button button:hover { background-color: red; color: white;}
</style>            
""", unsafe_allow_html=True) 

#page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #incresed score by 1
    else:
        feedback.append("❌ Password should be **at lest 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else: 
        feedback.append("❌ Password should include **at lest one number (0-9) **.")

    #special character
    if re.search(r"[!@#$%^&*]", password):
        score +=1
    else:
        feedback.append("C Include **at least one special character(!@#$%^&*)**.")

    #display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3 :
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more feature")
    else:
        st.error("❌ **Weak Password** - Follow the suggestion below to strength it. ")

    #feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")


#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!") #show warning if password if empty
