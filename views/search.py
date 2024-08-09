import streamlit as st
import pandas as pd
from pathlib import Path
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.image.image import Image
from datetime import datetime
import random
from borb.pdf.pdf import PDF
from borb.pdf.canvas.color.color import HexColor, X11Color
from streamlit_pdf_viewer import pdf_viewer



st.set_page_config(page_title="Individual Data",layout="wide")


# --- Definition of PDF Layout ---
def _build_invoice_information():    
    table_001 = Table(number_of_rows=23, number_of_columns=2)
     
    table_001.add(Paragraph("Age", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,1]))) 

    table_001.add(Paragraph("Address", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,2])))  

    table_001.add(Paragraph("Phone No", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,3])))  

    table_001.add(Paragraph("Ward No", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,4])))  

    table_001.add(Paragraph("House No", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,5])))  

    table_001.add(Paragraph("Gender", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,6])))  

    table_001.add(Paragraph("CareTaker", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,7])+"\nPh No:"+str(df[mask].iloc[0,8])))  
        
    table_001.add(Paragraph("Guardian's Name", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT))
    table_001.add(Paragraph(str(df[mask].iloc[0,9])))  
        
    table_001.add(Paragraph("No.of Family Members", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT))
    table_001.add(Paragraph(str(df[mask].iloc[0,10])))
    #table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year))) 
    table_001.add(Paragraph("Parental Status", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,11])))  

    table_001.add(Paragraph("Marital Status", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,12])))  

    table_001.add(Paragraph("Aadhar No", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,13]))) 

    table_001.add(Paragraph("")) 
    table_001.add(Paragraph(""))  

    table_001.add(Paragraph("Medical Board Certificate", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,14])))  

    table_001.add(Paragraph("UID Card", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,15])))  

    table_001.add(Paragraph("Percentage of Disability", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,16])))  

    table_001.add(Paragraph("Type of Disablility", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,17])))  

    table_001.add(Paragraph("Level of Disability", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,18])))  

    table_001.add(Paragraph("Guardianship", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,19])))  
        
    table_001.add(Paragraph("Category", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT))
    table_001.add(Paragraph(str(df[mask].iloc[0,20])))  
        
    table_001.add(Paragraph("Classification", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT))
    table_001.add(Paragraph(str(df[mask].iloc[0,21])))
    #table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year))) 
    table_001.add(Paragraph("Religion", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,22])))  

    table_001.add(Paragraph("Social Protections Available", font="Helvetica-Bold", horizontal_alignment=Alignment.LEFT)) 
    table_001.add(Paragraph(str(df[mask].iloc[0,23])))  

    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))    		
    table_001.no_borders()
    return table_001

# --- CONDITION --
col1, col2,col3 = st.columns([4,1,6])

with col1:
    st.title("View Detailed Info")
    #st.header("View Detailed Info")
    st.text("")
    srch_code=st.text_input("Aadhar No", value="", max_chars=12, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
    # --- LOAD DATAFRAME ---
    excel_file = 'Data\main.xlsx'
    sheet_name = 'Form Responses 1'

    df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='B:AO',
                    header=0)
    srch_int=0
    if srch_code:
        srch_int=int(srch_code)
    # --- FILTERED DATAFRAME ---

    mask=(df['Aadhar card No']==srch_int)
    if df[mask].shape[0]:
        st.markdown(f'Found User')
        st.markdown(f'**{df[mask].iloc[0,0]}**')
        #st.dataframe(df[mask].reset_index(drop=True))
        with st.spinner('Getting Info...'):
            pdf = Document()
            # Creating Document
            page=Page()
            pdf.add_page(page)
            page_layout = SingleColumnLayout(page)
            page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
            page_layout.add(    
            Image(        
            image=Path(r"assets\pbanner.png"),
            
            width=Decimal(466),        
            height=Decimal(68),    
            ))
            # Title
            page_layout.add(
                Paragraph(
                    str(df[mask].iloc[0,0]), font_color=HexColor("#283592"), font_size=Decimal(25)
                )
            )
            # Invoice information table  
            page_layout.add(_build_invoice_information())  
        
            # Empty paragraph for spacing  
            page_layout.add(Paragraph(" "))

            with open("Data\cacheout.pdf", "wb") as pdf_file_handle:
                PDF.dumps(pdf_file_handle, pdf)
            with col3:
                with open("Data\cacheout.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                    pdf_viewer(input=PDFbyte,width=700)
                    with col1:
                        st.download_button(label="Download Report",
                                        data=PDFbyte,
                                        file_name=str(df[mask].iloc[0,0])+".pdf",
                                        mime='application/octet-stream')
            
    elif srch_int==0:
        st.markdown(f'*Enter UID Number*')
    else:
        st.markdown(f'*The person not available or there will be a mistake in data entry*')
