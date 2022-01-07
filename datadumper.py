## Importing required modules
import json
import urllib.request as req
import pandas as pd
from sqlalchemy import create_engine
import operator

## API call
with req.urlopen('https://d1hf8ajhua2dre.cloudfront.net/Altsplice/NCBI/CanonicalID/LongestCDS/CanonicalLIst.json') as response:
  source = response.read()
  json_data = json.loads(source)
  df=pd.DataFrame(json_data.items())



## Connecting to the DB
host='genomedatabase.cs6pl6l3pxsn.us-east-2.rds.amazonaws.com'
user='GeneSymbol'
password='batch2genome'
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=host, db='genome', user=user, pw=password))


def convert_json(records):
    dictionary = [jsonn(gene) for gene in records]
    gene_list = [list(x.values()) for x in dictionary]
    return gene_list

def jsonn(record):
        return {"Gene_name": record[0], "Transcript_id":record[1]}


def create_database():
    ## Creating DB
    try:
        engine.execute("create database genome")
        print("DB Created")
    except:
        print("Database already Exists")

    ## Using created DB
    engine.execute("use genome")


def create_table():
    ## Creating Table
    try:
        engine.execute("CREATE TABLE genedata ( genesymbol VARCHAR(10), transcriptid VARCHAR(10))")
        print("Table Created")
    except:
        print("Table already exists")

def insert_values():
    ## Inserting Data Frame into DB
    try:
        column_name = ['genesymbol','transcriptid']
        df.columns = column_name
        df.to_sql('genedata', engine,if_exists="replace", index=False)
        print("Data inserted")
    except:
        print("Data already exits")

def display():
    query = "select * from genedata where genesymbol like 'A%%' "
    res=engine.execute(query).fetchall() 
    return res
    
def alphabetsearch(alphabet):
    alphabet += '%%'
    query = "select * from genedata where genesymbol like "
    query_letter = "'{}'".format(alphabet)
    query += query_letter
    res=engine.execute(query).fetchall()
    return res

def update(gene,t_id):
    engine.execute("UPDATE genedata SET transcriptid= '{}' where genesymbol='{}'".format(t_id,gene))
    res  = alphabetsearch(gene[0])
    return res


def delete(gene):
    query = "delete from genedata where genesymbol = '{}'".format(gene)
    engine.execute(query)
    res = alphabetsearch(gene[0])
    return res
    
def create(gene,t_id):

    query = "select count(*) from genedata where genesymbol = '{}' ".format(gene)
    genecount=engine.execute(query).fetchall()
    for i in genecount:
        genecount=i
    for j in genecount:
        genecount=j
  
    if genecount > 0:
        update(gene,t_id)
        res = alphabetsearch(gene[0])
        return res
    else:
        query = "insert into genedata values('{}' , '{}')".format(gene,t_id)
        engine.execute(query)
        res = alphabetsearch(gene[0])
        return res
