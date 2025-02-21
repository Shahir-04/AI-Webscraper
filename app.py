import streamlit as st
from scrape import scrape_website,clean_body_content,split_dom_content,extraxt_content
from extract import extract_with_deepseek
st.title('AI WebScraper')
url=st.text_input('Enter Url of website')
if st.button('Get Started'):
    # st.write('hello')
    scrape=scrape_website(url)
    body_content=extraxt_content(scrape)
    clean_content=clean_body_content(body_content)
    st.session_state.dom_content=clean_content

    with st.expander('View DOM Content'):
        st.text_area('DOM_content',clean_content,height=300)

    # st.write('Describe what you want to parse')
if 'dom_content' in st.session_state:
    parse_description=st.text_area('Describe what you want to Extract')

    if st.button('Extract Content'):
        if parse_description:
            st.write('Extracting the Content....')

            dom_cunks=split_dom_content(st.session_state.dom_content)
            result=extract_with_deepseek(dom_cunks,parse_description)
            st.write(result)