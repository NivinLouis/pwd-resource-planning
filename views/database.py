import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import mm, inch
import time

st.set_page_config(page_title="Database",layout="wide")
st.title("Search Database")

def print_pdf():
    # --- LOAD PDF ----
    custom =  (20 * inch, 10 * inch)
    pdf = SimpleDocTemplate("Data\export.pdf", pagesize=custom,topMargin=0.3*inch,bottomMargin=0.2*inch)
    table_data = []
    table_data.append(columns_selection)
    for i, row in data.iterrows():
        table_data.append(list(row))
    table = Table(table_data)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ])

    table.setStyle(table_style)
    pdf_table = []
    pdf_table.append(table)

    pdf.build(pdf_table)

# --- LOAD DATAFRAME ---

with st.spinner('Getting Info...'):
    time.sleep(0.5)
    excel_file = 'Data\main.xlsx'
    sheet_name = 'Form Responses 1'


    df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='B:AO',
                    header=0)
    # --- COLUMN SELECTION ---
    columns_list = df.columns.tolist()
    columns_default=['Name','Age','Address','Phone No','Ward No','Gender','Aadhar card No','Type of Disability','Level of Disability','Category','Religion']
    # --- DATA SELECTION ---
    marital_status= df['Marital Status'].unique().tolist()
    ages=df['Age'].unique().tolist()
    ward_no= df['Ward No'].unique().astype(int).tolist()
    ward_no.sort()
    genders= df['Gender'].unique().tolist()
    level_disabilities=df['Level of Disability'].unique().tolist()



# --- Defining additional filtering options ---
def _additional_filter():
    parental_status= df['Parental Status'].unique().tolist()
    family_members= df['No. of Family Members'].unique().astype(int).tolist()
    medical_certificate= df['Medical Board Certificate'].unique().tolist()
    type_of_disabilities=df['Type of Disability'].unique().tolist()
    percentage_disabilities=df['Percentage of Disability'].unique().tolist()
    # --- COLUMN VIEW ---
    col11, col12, col13, col14, col15  = st.columns([1,6,1,6,1])

    with col12:
        global family_selection,disability_selection,medical_selection,percentage_selection,parental_selection
        family_selection = st.slider('No.of Family Members',
                      min_value=min(family_members),
                      max_value=max(family_members),
                      value=(min(family_members),max(family_members)))
        disability_selection = st.multiselect('Type of Disability ',
                               type_of_disabilities,
                               default=type_of_disabilities,
                               )
    with col14:
        medical_selection = st.multiselect('Medical Certificate Status ',
                                   medical_certificate,
                                   default=medical_certificate,
                                   )
    
        percentage_selection=st.multiselect('Percentage of Disability ',
                               percentage_disabilities,
                               default=percentage_disabilities,
                               )
    col21, col22, col23  = st.columns([1,4,1])
    with col22:
        parental_selection = st.multiselect('Parental Status: ',
                                   parental_status,
                                   default=parental_status,
                                   )



# --- COLUMN VIEW ---
col1, col2 = st.columns([1,2])

with col1:
    with st.expander("Display"):
        columns_selection = st.multiselect('Select Columns to Display: ',
                                   columns_list,
                                   default=columns_default,
                                   )

with st.expander("Filter options"):
    # --- FILTERING MENU ---

    # --- COLUMN VIEW ---
    col11, col12, col13, col14, col15  = st.columns([1,6,1,6,1])

    with col12:
        age_selection = st.slider('Age:',
                        min_value=min(ages),
                        max_value=max(ages),
                        value=(min(ages),max(ages)))
        marital_selection = st.multiselect('Marital Status ',
                                marital_status,
                                default=marital_status,
                               )
        
    with col14:
        gender_selection = st.multiselect('Gender',
                                genders,
                                default=genders,
                                )
        level_selection = st.multiselect('Level of Disability',
                                level_disabilities,
                                default=level_disabilities,
                                )
        
    col21, col22, col23  = st.columns([1,4,1])
    with col22:
        ward_selection = st.multiselect('Ward ',
                                ward_no,
                                default=ward_no,
                                )
    on = st.toggle("Show Additional options")
    if on:
        _additional_filter()



# --- FILTERED DATAFRAME ---

mask=(df['Age'].between(*age_selection))&(df['Marital Status'].isin(marital_selection))&(df['Gender'].isin(gender_selection))&(df['Level of Disability'].isin(level_selection))&(df['Ward No'].isin(ward_selection))
number_of_result=df[mask].shape[0]
st.markdown(f'*Available Results:{number_of_result}*')
data=df[mask][columns_selection].reset_index(drop=True)
st.dataframe(data)


if st.button("Export Data",type='primary'):
    with st.spinner('Generating...'):
        print_pdf()
        with open("Data\export.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                    st.download_button(label="Download PDF",
                                        data=PDFbyte,
                                        file_name="Exported.pdf",
                                        mime='application/octet-stream')

