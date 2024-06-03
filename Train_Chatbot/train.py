import json
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline
import pickle


# Initialize the DocumentStore
document_store = InMemoryDocumentStore(use_bm25=True)

# Load and process the JSON data
# Adjust the file path to your JSON file
json_file_path = r'D:\VSC\donnee.json'

with open(json_file_path, 'r') as f:
    data = json.load(f)

documents = [{"content" : "HEY HOW CAN I HELP YOU TODAY? "},{"content" : "HI WELCOME, WHAT IS YOUR QUESTION? "},{"content" : "HELLO WELCOME, WHAT IS YOUR QUESTION? "}]

CatList=[]
for category, items in data.items():
    subCatList=[]
    for subcategory, products in items.items():
        ProductsList=[]
        for product in products:
            # Vérifier et nettoyer les prix
            price_member = product.get('Member Price', 'N/A')
            price_regular = product.get('Regular Price ', 'N/A')

            # Formater le contenu selon les spécifications
            content = (
                f"Product {product['Name']} : the member price of this product is {price_member} , and for the regular price is {price_regular} ,the product category is {category}, and the product subcategory is {subcategory}."
            )
            document = {
                "content": content
            }
            documents.append(document)
            ProductsList.append(product['Name'])
        ProductsNames = ", ".join(ProductsList)
        content = (f"the products of the subcategory {subcategory} are : {ProductsNames} .")
        document = {
                "content": content
        }
        documents.append(document)
        subCatList.append(subcategory)
    #add the subcat to the document
    subCats = ", ".join(subCatList)
    content = (f"the subcategories of the {category} are: {subCats} .")
    document = {
                "content": content
    }
    documents.append(document)
    CatList.append(category)
#add the categories
Cats = ", ".join(CatList)
content = (f"the categories of this web site are: {Cats} .")
document = {
                "content": content
}
documents.append(document)

# Write documents to the DocumentStore
document_store.write_documents(documents)

# Initialize the Retriever
retriever = BM25Retriever(document_store=document_store)

# Initialize the Reader
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

# Create the pipeline
pipe = ExtractiveQAPipeline(reader, retriever)

with open(r'D:\Dev\DevPfa\Model\my_pipeline.pkl', 'wb') as f:
    pickle.dump(pipe, f)
