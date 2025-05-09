import time
import streamlit as st 




def main():
    st.set_page_config("Readme_MD_Generator")
    st.header("Readme.MD Generator System")

    with st.sidebar:
        st.title("Menu:")
    pdf_docs = st.file_uploader("Upload your pdf Files and click on the Submit & Process Button", accept_multiple_files=True)    
    if st.button("Submit & Process"):
        with st.spinner("Processing....."):
            st.success("Done")



if __name__ == "__main__":
    main()
