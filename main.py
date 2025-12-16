import streamlit as st
import pyperclip
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.markdown(
    """
    <style>
    body {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    st.title("Email Generator for Jobs vacancy")
    url_input = st.text_input("Enter a URL:", value="https://careers.nike.com/global-senior-director-nike-entertainment-and-celebrity-partnerships/job/R-74166")
    st.markdown("""<div> <br> </div> """,unsafe_allow_html=True,)
    submit_button = st.button("Submit")
    
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                # st.code(email, language='markdown')

                # Display the email in a text area that users can copy from
                st.text_area("Generated Email", value=email, height=600) 


                

        except Exception as e:
            st.error(f"An Error Occurred: {e}")




def create_front_page():

    st.markdown(
    """
    <style>
    body {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )


    
    # Add title with a custom CSS class
    st.markdown('<h1 class="centered-title">Welcome to Job Email Composer tool</h1>', unsafe_allow_html=True)
    st.markdown('<br><br><br>', unsafe_allow_html=True)
    st.markdown('<h5 class="centered-title">This tool helps you to generate email based on the job openings.</h2>', unsafe_allow_html=True)
    st.markdown('<br><br><br>', unsafe_allow_html=True)   
 
   
    if st.button("Explore"):
        st.session_state.page = "job_email_generator"

    

if __name__ == "__main__":

    
    
    # Initialize session state to track current page
    if "page"   not in st.session_state:
        st.session_state.page = "front_page"  # Default page   


    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Job Email Generator")
    
    # Show either the front page or job email generator page based on session state
    if st.session_state.page == "front_page":
        create_front_page()
    elif st.session_state.page == "job_email_generator":
        create_streamlit_app(chain, portfolio, clean_text)
        


    





   

