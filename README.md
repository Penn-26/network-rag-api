[README.md](https://github.com/user-attachments/files/25110613/README.md)
<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI



---

![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_g3h4i5j6)

---

In this project, I will be learning more about working with APIs and LLMs

### Key services and concepts

Services I used were Ollama, FastAPI, uvicorn, Swagger UI, chroma to build the RAG API. 

### Challenges and wins

It was nice working with the FastAPI, abstracting work around routing HTTP requests and generrating documentation.

### Why I did this project

I did this project because I wanted to do more work with APIs and build and AI API from scratch. Lookinbg foward to building more projects!

---

## Setting Up Python and Ollama

In this step, I'm setting up Python and Ollama. Python is a popular, high-level programming language known for its simplicity and readability. Ollama is an open-source tool that lets you run large language models (LLMs) directly on your own computer.  I need these tools because they will run locally on my computer

### Python and Ollama setup

![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_i9j0k1l2)

### Verifying Python is working

### Ollama and tinyllama ready

Ollama is a tool that lets you run large language models locally.  I downloaded the tinyllama model because it is lightweight, fast and simple. The model will help my RAG API by being the brain of the responses 

---

## Setting Up a Python Workspace

### Python workspace setup

### Virtual environment

A virtual environment is a separate workspace that stores all the dependencies necessary seperate from the other projects on your computer. I created one for this project to store my python packages. Once I activate it makes sure all versions installed only affect this project. To create a virtual environment, I ran the venv module.

### Dependencies

The packages I installed are FastAPI, Chroma, Uvicorn and Ollama. FastAPI is used to build APIs quickly so I can focus on building the RAG. Chroma is used for the retrieval part of the RAG when users query the database, Uvicorn actually runs the API defined by the FasrAPI and handles incoming requests(HTTP, routing  and conversion) and Ollama client sends everything to the local llm for answer generation, and uvicorn serves it all up.

![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_u1v2w3x4)

---

## Setting Up a Knowledge Base

In this step, I'm creating a knowledge base which I need to give my AI accurate up to date info.

### Knowledge base setup

![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_t1u2v3w4)

### Embeddings created

Embeddings are numerical representations of text that capture meaning. I created them by writing a python script that will read the knowledge document and store in chroma as embeddings.  The db/ folder contains the knowledge base's embedding script. This is important for RAG because Chroma can quickly search through them when the API is running.

---

## Building the RAG API

In this step, I'm building a RAG API. An API is an Application Programming Interface that lets software  retrieve and share data with other apps. FastAPI is a modern Python web framework that's designed to be fast, easy to use and well documented. I'm creating this because I can then build a web UI that calls your API, integrate your API into mobile apps
or connect your API to other services.

### FastAPI setup

### How the RAG API works

My RAG API exposes a `/query` endpoint that takes a user question, retrieves the most relevant document from a persistent ChromaDB collection, and then uses that retrieved text as “context” to help the LLM answer. The main components are **FastAPI** (the web server/router), **ChromaDB** (the vector store that persists embeddings and documents under `./db` in the `docs` collection), and **Ollama** (the local LLM runtime). At request time, ChromaDB performs a similarity search (`collection.query`) to return the top match, and the API builds a prompt that includes `Context + Question` for the model. Finally, Ollama’s `tinyllama` generates the response, which the API returns as JSON.
rks by...

![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_f3g4h5i6)

---

## Testing the RAG API

In this step, I'm testing my RAG API. I'll test it using the CLI first then I'll use swagger UI, an automatically generated, interactive documentation page for your FastAPI server .

### Testing the API

### API query breakdown

I queried my API by running the command The command uses the POST method, which means I queried the API by using curl to make an HTTP  POST request to your FastAPI endpoint at http://127.0.0.1:8000/query, my local machine on port 8000. The `-G` flag tells curl to put the parameters in the URL query string (like a GET-style ?q=...) even though the method is POST, and `--data-urlencode` safely URL-encodes the text so spaces and punctuation don’t break the URL. FastAPI received that `q` value, ran a ChromaDB similarity search to fetch the best matching document as context, then sent Context + Question to Ollama’s tinyllama to generate an answer. Finally, the API returned a JSON response containing the model’s generated much more accurate answer.


![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_g3h4i5j6)

### Swagger UI exploration

Swagger UI is an interactive, browser-based documentation page that FastAPI automatically generates from your API’s OpenAPI spec. I used it to test my /query endpoint by opening the docs page, entering a sample `q` value, and clicking Execute to send a request and view the response. The best part about using Swagger UI was that it let me quickly validate the request format and see the exact response JSON or building a front end.


---

## Adding Dynamic Content

In this project extension, I'm adding a new endpoint to my API that lets you dynamically add content to your knowledge base 

### Adding the /add endpoint

![Image](http://learn.nextwork.org/triumphant_cyan_clever_dragonfly/uploads/ai-devops-api_w9x0y1z2)

### Dynamic content endpoint working

The /add endpoint allows me to upload (or submit) new documents into my ChromaDB docs collection so they can be retrieved later as context during queries. This is useful because it lets me continuously expand and update the knowledge base my RAG system searches, improving answer accuracy and making the API more helpful over time.

---

---
