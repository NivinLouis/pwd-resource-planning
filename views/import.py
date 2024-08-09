import streamlit as st
import xlwings as xw
from pathlib import Path

st.set_page_config(page_title="Import Data",layout="wide")
st.title("Import")
st.subheader("Add data by uploading the excel file with specified format below")

uploaded_file= st.file_uploader('Choose a XLSX file',type='xlsx')
if uploaded_file:
    st.markdown('----')

    save_path = Path('Data', "impcache.xlsx")
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())
    excel_app = xw.App(visible=False)
    master_wb=xw.Book(r"Data\main.xlsx")
    master_sheets = master_wb.sheets
    addat=master_sheets[0].range('B1').end('down').row

    newdata_wb = xw.Book(r"Data\impcache.xlsx")
    newdata_wb.sheets[0].range('A2').expand()
    lastline=master_wb.sheets[0].range('A1').end('down').row

    lastdate=master_wb.sheets[0].range('A'+str(lastline)).value

    new_data_raw=newdata_wb.sheets[0].range('A2').expand().value
    temp_data=[i[0:40] for i in new_data_raw if i[0]>lastdate]
    newrow=master_wb.sheets[0].range('A1').end('down').row + 1
    master_wb.sheets[0].range(newrow,1).value=temp_data
    if len(temp_data)!=0:
        st.subheader("Added "+str(len(temp_data))+" New Response to database")
    else:
        st.subheader("No new responses found")

    newdata_wb.save()
    master_wb.save()
    excel_app.quit()