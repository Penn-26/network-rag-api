import chromadb

client = chromadb.PersistentClient(path="./db") 
collection = client.get_or_create_collection("docs") 

with open("RAG.txt", "r") as f: 
    text = f.read()

collection.add(documents=[text], ids=["RAG"]) 

print("Embedding stored in Chroma") 
