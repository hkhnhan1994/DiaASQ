import os
import pandas as pd
import json
unique_categories=[]
unique_sentiments=[]
# Function to preprocess text and remove special characters
def remove_specific_special_chars(text, special_chars_path= 'special_characters.txt'):
    try:
        with open(special_chars_path, 'r') as file:
            chars_to_remove = [line.strip() for line in file]
            # Remove specific special characters from the text
            new_text=text
            for char in chars_to_remove:
                new_text = new_text.replace(char, '')
            return new_text
    except: return text
# following the ACOS format, [a, c, s, o ]
def assign_positions_to_paragraphs(paragraphs, triplets):
    result = []
    categories =[]
    for p in paragraphs:
      assigned_targets = []
      for t in triplets:
          # index = transfer(t[0])
          # count = transfer(t[1])
          aspect = t[7]
          sentiment= t[6]
          category = t[8]
          opinion = t[9]
          cleaned_string=remove_specific_special_chars(p)
          _op=cleaned_string.replace(opinion, "~op/ "+opinion+" ~op/")
          _as=cleaned_string.replace(aspect, "~as/ "+aspect+" ~as/")
        
          _as_index =[]
          _op_index =[]
          for ind,val in enumerate(_op.split()):
              if val =="~op/":
                  _op_index.append(ind)
          for ind,val in enumerate(_as.split()):
              if val == "~as/":
                  _as_index.append(ind)
          try:
            _opinion=[i for i in range(_op_index[0],_op_index[1]-1) ]
            _aspect=[i for i in range(_as_index[0] ,_as_index[1]-1) ]
            # print(f"{_op.split()},{_opinion} ")
            # print(f"{_op.split()},{_opinion} ")
            # print(f"opinion: {opinion},aspect:{aspect}")
            assigned_targets.append([_aspect,_opinion,sentiment])
            categories.append(category)
            #   print(f"{cleaned_string}, [{_aspect},{_opinion},{sentiment}]")
          except: continue
      if len(assigned_targets)>0:
        result.append([cleaned_string, assigned_targets])
      assigned_targets = []
    categories= list(set(categories ))
    return result

def list_to_string(lst):
    return str(lst)

# Specify the directory path
directory_path= 'jsons_en'
Folder_path=os.path.join(os.getcwd(),directory_path)
# Get a list of all files in the directory
file_paths = [os.path.join(Folder_path, filename) for filename in os.listdir(Folder_path) if os.path.isfile(os.path.join(Folder_path, filename))]

out_put_folder_path= 'output'
if not os.path.exists(os.path.join(os.getcwd(),out_put_folder_path)):
    os.makedirs(out_put_folder_path)
        
# Now, file_paths contains the paths of all files in the specified folder
for path in file_paths:
    df= pd.read_json(path)
    my_list=list(df.apply(lambda row: assign_positions_to_paragraphs(row['sentences'], row['triplets']), axis=1))
    # Apply the function to each row and store the result in a new column
    # Flatten the nested list using list comprehension
    flattened_list = [(item[0], item[1]) for sublist in my_list for item in sublist]

    # Create a DataFrame
    final_result = pd.DataFrame(flattened_list, columns=['Sentence', 'Triplets'])
    # clean up empty rows
    count_empty_lists = (final_result['Triplets'].apply(lambda x: len(x) == 0)).sum()
    print("Number of rows with empty lists in 'Triplets':", count_empty_lists)
    final_result = final_result[final_result['Triplets'].apply(lambda x: len(x) > 0)]
    # generate the dataset format
    final_result['Formated'] = final_result['Sentence'] + '####'+final_result['Triplets'].apply(list_to_string)
    print(f"Shape of the dataset {os.path.basename(path)}:{final_result.shape[0]} ")
    # export data
    source_name=os.path.basename(path).split('.')[0]+'.txt'
    output_json_file=os.path.join(os.getcwd(),out_put_folder_path,source_name)
    final_result['Formated'].to_csv(output_json_file, sep='\t', index=False, header=False)
    
# export categorical
unique_categories = list(set(unique_categories))
with open(os.path.join(os.getcwd(),out_put_folder_path,'categories.txt'), 'w') as file:
        json.dump(unique_categories, file)
print (f"dataset located in {os.path.join(os.getcwd(),out_put_folder_path)}")
print(list(set(unique_sentiments)))
    

