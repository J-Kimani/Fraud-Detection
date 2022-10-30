import json
import numpy as np
import pickle
import streamlit as st
import base64


# load saved model
def load_saved_artifacts():
    global __model
    
    with open("./artifacts/fraud.pickle", "rb") as f:
        __model = pickle.load(f)


def Fraud(step, type, amount, old_origin, new_origin, old_dest, new_dest):
    x = np.zeros(7)

    x[0]: step
    x[1]: type
    x[2]: amount
    x[3]: old_origin
    x[4]: new_origin
    x[5]: old_dest
    x[6]: new_dest

        
    fr = __model.predict([x])[0]


    if fr == 1:
        return "Fraudulent transaction"
    else:
        return "Normal transaction"

@st.experimental_memo

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("fraud.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]> .main {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid= "stHeader"]{{
background: rgba(0,0,0,0);
}}
</style>
"""


def main():
    # background image
    st.markdown(page_bg_img, unsafe_allow_html=True)


    # Title
    st.title('Online Fraud Detection')

    # user instructions
    instructions = '<p style="font-family:Courier; color:White; font-size: 20px;">Welcome, Detect Fraud at the Touch of a Button</p>'
    st.markdown(instructions, unsafe_allow_html=True)
    
    # user input
    step = st.text_input('Length of transaction(Hours)')
   
    amount = st.text_input('Amount transacted')
    ty = st.selectbox(
        "Type of Transaction",
        ("Cash In", "Cash Out", "Debit", "Payment", "Transfer"))
    def tp(ty):
        if  ty == "Cash In":
            ty = 0
        elif ty == "Cash Out":
            ty = 1
        elif ty == "Debit":
            ty = 2
        elif ty == "Payment":
            type = 3
        elif ty == "Transfer":
            ty = 4
        return ty

    type = tp(ty)
    old_origin = st.text_input('Initial balance before transaction')
    new_origin = st.text_input("Customer's balance after the transaction.")
    old_dest = st.text_input('Initial recipient balance before the transaction.')
    new_dest = st.text_input("Recipient's balance after the transaction.")

    # prediction code
    is_fraud = ''

    # prediction button
    if st.button('Status'):

        is_fraud = Fraud(step, type, amount, old_origin, new_origin, old_dest, new_dest)
    
    st.success(is_fraud)

    
if __name__ == '__main__':
    load_saved_artifacts()
    main()
    