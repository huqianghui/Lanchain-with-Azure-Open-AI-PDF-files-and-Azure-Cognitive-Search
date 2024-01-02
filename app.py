import pandas as pd
from app_chain_stuff_type import get_content_by_index_content
from resultFinetune import get_finetune_result

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("./documents/指标定位样例-万科A2022年年报.xlsx", sheet_name="Sheet1")

# Define a function to add the contents of two columns together
def refine_result_by_context(row):
    index_content = row["指标内容"]
    print(">> 指标内容:"+ index_content)
    if index_content:
        amount, unit = get_content_by_index_content(index_content)
        return pd.Series({"gpt值": amount, "gpt单位": unit})
    else:
        return pd.Series({"gpt值": "", "gpt单位": ""})

# Apply the "generate_gpt_values" function to each row of the DataFrame to fill in the "gpt_value" and "gpt_unit" columns
# df[["gpt值", "gpt单位"]] = df.apply(refine_result_by_context, axis=1)
    
# Define a function to add the contents of two columns together
def get_result_by_context(row):
    index_content = row["指标内容"]
    index_type= row["指标类型"]
    print("\n\n\n")
    print(">> 指标内容和指标类型:"+ index_content + " " + index_type)
    if index_content:
        answer = get_content_by_index_content(index_content + " " + index_type)
        finetunedResult = get_finetune_result(index=index_content, index_type=index_type, content=answer)
        return pd.Series({"gpt值": finetunedResult,"gpt内容": answer})
    else:
        return pd.Series({"gpt值": "","gpt内容": ""})

df[["gpt值","gpt内容"]] = df.apply(get_result_by_context, axis=1)

# Write the updated DataFrame back to the Excel file
df.to_excel("./documents/指标定位样例-万科A2022年年报-gpt-filled-v2.xlsx", index=False)