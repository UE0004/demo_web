import streamlit as st 

# st.title("This is my first application")
# st.header("python")
# st.subheader("Java")
# st.markdown("I love python")


name = st.text_input("Enter your name")
fname = st.text_input("Enter your father name")
adr = st.text_area("Enter your text here:")
classdata=st.selectbox("Enter your class: ", (8,9,10,11,12))

button = st.button("done")

if button:
    st.markdown(f"""
                Name: {name}
                father name: {fname}
                Address :{adr}
                class : {classdata}""")
    

