import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# getting the api key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

def predict_connected_columns_data(data_info, data_head):
    try:
        model = genai.GenerativeModel(
            model_name="models/gemini-2.0-flash-exp",
            system_instruction="""
                Act as a data analytics.
                You will be provided with the data info and data head of the particular datasets. The data info is in dictionary format that contains the column name and its data type, whereas data head is in dataFrame format which contains the first 5 rows of the dataset with the column names. Your task is to provide the connected columns data for the later prediction. Also, provide the how it can be used for the prediction. Your ouptut will be in a json format only. Use very short description for prediction usage than that of the given output examples.\n
                *** Examples of the output: ***\n
                ```{
                    "connected_columns": {
                        "transaction_info": ["InvoiceNo", "InvoiceDate"],
                        "product_info": ["StockCode", "Description"],
                        "customer_info": ["CustomerID", "Country"],
                        "order_details": ["Quantity", "UnitPrice"]
                    },
                    "prediction_usage": {
                        "transaction_info": "These columns can be used to analyze trends over time, such as daily, monthly or yearly sales patterns. This information can be used to predict future sales based on seasonal trends or promotional campaigns.",
                        "product_info": "This can help in predicting which products will be most popular and need restocking, as well as identifying products that are not performing well. This can also help in the recommendation system.",
                        "customer_info": "By analysing this data, it can be predicted which demographics will be more likely to make purchases.",
                        "order_details": "This data can be used to predict the total value of a transaction, by multiplying quantity and unit price, which is then used to predict future revenue by extrapolating these past purchase patterns."
                    }
                }```
            """
        )
        
        response = model.generate_content(f"Data info: {data_info}, Data head: {data_head}")
        
        output = response.text
        output = output.strip("```json").strip("\n```")

        return json.loads(output)
    except Exception as e:
        return e
