import fsspec
import re
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import pandas as pd
from scipy.io.arff import loadarff 
import zipfile, os
from glob import glob
from constants import *
import json 

def convert_link(links):
  output = []
  for link in links.split(","):
    if 'github.com' in link.lower():
      user_name = link.split("/")[3]
      repo_name = link.split("/")[4]
      if link.count('/') > 4:    
        branch_name = 'master' if 'master' in link else 'main'

        
        base_path = f"https://raw.githubusercontent.com/{user_name}/{repo_name}/{branch_name}/"
        file_name = link.split(branch_name)[-1][1:]
        fs = fsspec.filesystem("github", org=user_name, repo=repo_name)
        
        if fs.isdir(file_name):
          output = output +  [base_path+f for f in fs.ls(f"{file_name}/")]
        else:
          output.append(base_path+file_name)
      else:
        output.append(f'https://github.com/{user_name}/{repo_name}/archive/master.zip')
    elif 'drive.google' in link.lower():
      base = "https://drive.google.com/file/d/"
      trail = "/view"
      id = link.replace(trail,"").replace(base,"")
      output.append(f"https://drive.google.com/uc?export=download&id={id}")
    elif 'docs.google' in link.lower():
      sheet_name = "Sheet1"
      sheet_id = link.split("/d/")[-1].split("/")[0]
      url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
      output.append(url)
    else:
      output.append(link)
  return output

def get_data(bs, column):
    elements =  [attr[column] for attr in bs.find_all(attrs={column : re.compile(".")})]
    if len(elements) == 0:
      elements = [el.text for el in bs.find_all(column)]
    return elements

def read_xml(paths, columns):
  dfs = []
  for path in paths:
    with open(path, 'rb') as f:
        data = f.read()
    
    bs = BeautifulSoup(data, "xml")
    data = {}
    for column in columns:
      elements = get_data(bs, column)
      data[column] = elements
    dfs.append(pd.DataFrame(data))
  return pd.concat(dfs)

def read_json(path, lines = False, json_key = ''):
  if json_key:
    data = json.load(open(path))
    df = pd.DataFrame(data[json_key])
  else:
    df = pd.read_json(path, lines=lines)
  return df

def read_arff(path):
  raw_data = loadarff(path)
  df_data = pd.DataFrame(raw_data[0])
  return df_data

def get_df(type, paths, skiprows = 0, sep = "", lines = False, json_key = ''):
  best_sep = ""
  best_columns = 0
  dfs = []
  for path in paths:
    if type == "xlsx":
      df = pd.read_excel(path, skiprows = skiprows)
    if type == 'jsonl' or type == 'json':
      df = read_json(path, lines = lines, json_key = json_key)
    if type == 'arff':
      df = read_arff(path)
    if type == 'txt':
      lines = open(path, 'r').read().splitlines()[skiprows:]
      df = pd.DataFrame(lines)
    if type in ['csv', 'tsv']:
      if len(sep) > 0:
        df = pd.read_csv(path, sep = f'{sep}', skiprows = skiprows, error_bad_lines = False)
      else:
        for sep in ["\\\t", ";", ","]: #TODO I need to consider the case when we have single sepace separator
          try:
            df = pd.read_csv(path, sep = f'{sep}', skiprows = skiprows, error_bad_lines = False)
            num_columns = len(list(df.columns))
            if best_columns < num_columns:
              best_sep = sep
              best_columns = num_columns
          except:
            continue
    if type =='xml':
      tree = ET.parse(path)
      root = tree.getroot()
      xml_string = ET.tostring(root, encoding='unicode', method='xml')
      df = pd.DataFrame([xml_string[:500]])
    
    if len(dfs) > 0:
      try:
        df.columns = dfs[-1].columns
      except:
        continue
    dfs.append(df)
  return pd.concat(dfs), best_sep

def get_split_user(split_files):
    dif_splits = input('Enter different splits (y/n): ')
    if dif_splits == 'y':
        split_files = {}
        train_files = input('Enter train split files as a list: ')
        test_files = input('Enter test split files as a list: ')
        dev_files = input('Enter dev split files as a list: ')

        if train_files != '':
            split_files['TRAIN'] = train_files
        if test_files != '':
            split_files['TEST'] = test_files
        if dev_files != '':
            split_files['VALIDATION'] = dev_files
    return split_files

def extract_all(dir):
  zip_files = glob(f'{dir}/**/**.zip', recursive=True)
  for file in zip_files:
    with zipfile.ZipFile(file) as item:
      item.extractall('/'.join(file.split('/')[:-1])) 

def get_valid_files(zip_base_dir):
  files = []
  for ext in valid_file_ext:
    files += glob(f"{zip_base_dir}/**/**.{ext}", recursive = True)
  return files