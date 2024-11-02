import google.generativeai as genai
import os
from dotenv import find_dotenv,load_dotenv
# from bs4 import BeautifulSoup
# from requests import get
# import requests
# from PyPDF2 import PdfReader
# from io import BytesIO
# from pydantic import BaseModel
# from enum import Enum

# def scrape(url):
#     page = get(url).text
#     soup = BeautifulSoup(page, 'html.parser')
#     post = soup.find_all('p')
#     text = ''
#     for line in post:
#         text = f'{text} {line.text}'
#     return text

# def get_pdf_text_from_url(url):
#     headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
#     }
#     response = requests.get(url,headers = headers)
#     pdf_file = BytesIO(response.content)
#     # reader = PdfReader(pdf_file)
#     # text = ''
#     # for page_num in range(len(reader.pages)):
#     #     page = reader.pages[page_num]
#     #     text = page.extract_text()
#     # return text
#     return pdf_file

# def ai(query, inputData):
#     dotenv = find_dotenv(usecwd=True)
#     load_dotenv(dotenv)
#     API_KEY = os.getenv("GEMINI_API_KEY")
#     genai.configure(api_key=API_KEY)
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     query += ". Please provide your response in a way that I can display it in a text box in a flask app."
#     response = model.generate_content([query, inputData])
#     # print(response.text)
#     return response.text

# class Type(str, Enum):
#     website = "website"
#     pdf = "pdf"

# class QueryRequest(BaseModel):
#     query: str
#     url: str
#     type: Type

# def call_gemini(queryRequest: QueryRequest):
#     if(queryRequest.type == "website"):
#         #scrape the data.
#         inputData = scrape(queryRequest.url)
#         print(inputData)
#     elif(queryRequest.type == "pdf"):
#         inputData = get_pdf_text_from_url(queryRequest.url)
#         print("data is: ")
#         print(inputData)

#     return ai(queryRequest.query,inputData)

def ai2(path_name):
    dotenv = find_dotenv(usecwd=True)
    load_dotenv(dotenv)
    API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    uploaded_file = genai.upload_file(path_name)    
    query = "Two parts, first Please summarize this file detailing the positives and negatives, second list down the technical jargons with meaning if any. Please provide your response in a json format, with key 'summary' to provide summary, key 'positives' point out the positives and 'negative' to point out negative, 'tech-jargon' to have a array of objects with jargon and meaning.Please make sure you only reply with json and nothing else"
    response = model.generate_content([uploaded_file, query])
    # print(response.text)
    return response.text
    # json_response = json.load(response.text)
    # return json_response

def call_gemini2(path_name):

    return ai2(path_name)

# call_gemini()