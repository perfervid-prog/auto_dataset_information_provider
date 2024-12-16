import streamlit as st
from modules.data_processing import load_data, get_data_info
from modules.ai_assist import predict_connected_columns_data
import pandas as pd

def main():

    st.set_page_config("Dynamic Dataset Information Generator", layout="centered")

    st.title("Dynamic Dataset Information Generator")

    file = st.file_uploader("Upload a file", type=["csv", "json", "xlsx", "xls"])

    # add the spinner
    with st.spinner("Getting data info..."):

        if file is not None:
            data = load_data(file) # loads the data

            if data is not None:
                data_infos = get_data_info(data)

                data_info = data_infos[0]
                data_head = data_infos[1]

                st.write("Data info:")
                st.json(data_info)

                st.write("Data head:")
                st.write(data_head)

            else:
                st.error("Cannot get file info")
    
    if file is not None:
        with st.spinner("Getting insights on connected columns..."):
            if data_info is not None and data_head is not None:

                columns_insigts = predict_connected_columns_data(data_info, data_head)
                
                st.write("Connected columns insights:")

                table_data = []
                for key, value in columns_insigts["connected_columns"].items():
                    table_data.append([", ".join(value), columns_insigts["prediction_usage"][key]])

                df = pd.DataFrame(table_data, columns=["Connected Columns", "Purpose"])

                st.dataframe(df, use_container_width=True, hide_index=True, column_order=["Connected Columns", "Purpose"])
                

                





if __name__ == "__main__":
    main()
