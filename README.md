# Bahria Assistant – AI-Powered University Information Assistant

## Project Overview

**Bahria Assistant** is an AI-powered university information assistant developed to simplify how students access academic and administrative information at Bahria University. The system provides an interactive, conversational interface through which students can ask questions in natural language and receive relevant, context-aware answers based on official university documents.

The project leverages **Google Gemini API, LangChain, and Retrieval-Augmented Generation (RAG)** to process, retrieve, and interpret information from different university resources. These resources include university handbooks, academic regulations, semester timetables, elective subject lists, and other official documents available in PDF and Excel formats.

Traditionally, students have to manually search through lengthy documents, multiple PDF files, and spreadsheets to find specific information. This process can be time-consuming and sometimes confusing, particularly when information is distributed across different documents. Bahria Assistant addresses this challenge by providing a centralized platform where students can simply enter their questions and receive concise, relevant, and document-based responses.

Unlike traditional chatbots that rely only on pre-defined questions and answers, Bahria Assistant uses a document-based retrieval mechanism to identify relevant information before generating responses. This helps ensure that answers remain grounded in the university's available information rather than relying solely on the AI model's general knowledge.

## Key Features

### 1. University Handbook Assistance
- Provides information about university policies, academic regulations, and administrative procedures.
- Answers questions related to grading systems, GPA calculations, attendance requirements, examination rules, and academic eligibility.
- Helps students understand university rules without manually navigating lengthy handbook documents.
- Retrieves relevant information from official university handbooks to provide context-aware answers.

### 2. Timetable Assistance
- Allows students to search for relevant academic timetable information through natural-language queries.
- Helps identify course schedules, class timings, sections, and other available timetable details.
- Reduces the effort required to search through large timetable documents.
- Provides relevant schedule information based on the uploaded timetable sources.

### 3. Elective Subject Guidance
- Provides information about available elective subjects offered by the university.
- Helps students explore elective options based on available course information.
- Retrieves details such as course names, course codes, credit hours, and other available subject information.
- Makes it easier for students to compare and understand their elective choices.

### 4. AI-Powered Conversational Interface
- Allows students to interact with the system using everyday natural language.
- Understands questions even when they are phrased differently or contain follow-up queries.
- Provides conversational responses instead of requiring students to use specific keywords or predefined commands.
- Supports a more interactive and user-friendly information retrieval experience.

### 5. Document-Based Question Answering
- Uses Retrieval-Augmented Generation (RAG) to retrieve relevant content from university documents.
- Generates responses using the retrieved document content as contextual information.
- Helps minimize inaccurate or unsupported AI-generated answers.
- Can provide references or source information to help students verify the retrieved information.

### 6. Centralized Information Access
- Combines information from multiple university resources into a single platform.
- Reduces the need to search through separate PDFs, Excel sheets, and other academic documents.
- Provides a consistent and convenient way to access university-related information.

### 7. Scalable Document Management
- Supports multiple document formats, including PDF and Excel files.
- Allows university information sources to be updated by adding or replacing documents.
- Provides a foundation for expanding the system with additional academic departments, programs, and information categories.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Large Language Model (LLM) | Google Gemini API |
| AI Development Framework | LangChain |
| AI Architecture | Retrieval-Augmented Generation (RAG) |
| Knowledge Sources | PDF Handbooks, PDF Timetables, Excel Elective Lists |
| Document Processing | LangChain Document Loaders |
| Text Processing | Recursive Text Splitting / Chunking |
| Information Retrieval | Vector-Based Semantic Search |
| Vector Database | FAISS or ChromaDB |
| Embedding Model | Google Generative AI Embeddings |

*The vector database, embedding model, and document-processing components can be finalized according to the project's implementation.*

## System Architecture and Working Mechanism

Bahria Assistant follows a Retrieval-Augmented Generation (RAG) architecture that combines document retrieval with the language-generation capabilities of Google Gemini.

The system operates through the following stages:

**1. Document Collection and Loading**

Official university documents, including handbooks, timetables, and elective subject lists, are collected and loaded into the system.

**2. Document Processing and Text Extraction**

The uploaded documents are processed to extract meaningful textual information. Large documents are divided into smaller chunks to make information retrieval more efficient.

**3. Embedding Generation and Storage**

The extracted text chunks are converted into numerical vector representations using an embedding model. These embeddings are stored in a vector database to support semantic searching.

**4. User Query Processing**

When a student submits a question, the system processes the query and converts it into an appropriate representation for searching the knowledge base.

**5. Context Retrieval**

The retrieval component searches the vector database to identify the most relevant document chunks related to the student's question.

**6. Response Generation**

The retrieved information is passed to Google Gemini through LangChain as contextual input. Gemini analyzes the question and retrieved content to generate a relevant, conversational response.

**7. Response Display**

The generated answer is displayed through the Streamlit interface, allowing students to interact with the assistant and ask additional questions.

## Project Objectives

The primary objective of Bahria Assistant is to improve the accessibility of university-related information by developing an intelligent, document-based conversational assistant.

The specific objectives include:

- Developing a centralized AI-powered platform for accessing Bahria University information.
- Reducing the time and effort required to search through lengthy academic and administrative documents.
- Implementing a Retrieval-Augmented Generation architecture to provide context-aware and document-grounded responses.
- Enabling students to ask questions using natural language rather than navigating documents manually.
- Providing easy access to university policies, academic regulations, timetables, and elective subject information.
- Improving the overall student experience through a simple and interactive conversational interface.
- Minimizing unsupported AI-generated responses by grounding answers in official university documents.
- Designing a modular architecture that can accommodate additional university documents and information sources in the future.

## Expected Outcomes

The expected outcome of this project is a functional AI-powered university assistant that provides students with quick and convenient access to academic and administrative information.

Students will be able to interact with the system through a web-based interface, ask questions about university-related topics, and receive relevant answers generated using information retrieved from official documents.

The system is expected to:

- Reduce manual document-searching efforts.
- Improve the speed of accessing university information.
- Make complex academic policies easier to understand.
- Provide a more convenient alternative to searching through multiple documents.
- Improve information accessibility for students.
- Establish a foundation for future AI-based university support services.

## Project Scope and Future Expansion

Initially, Bahria Assistant will focus on a single university, Bahria University, and will be designed to serve a relatively small student user base. The initial implementation will cover selected academic and administrative information sources, including university handbooks, semester timetables, and elective subject documents.

The architecture will follow a modular approach so that additional features and information sources can be integrated in the future.

Potential future enhancements include:

- **Multi-Department Support:** Extending the knowledge base to cover multiple departments, programs, and academic disciplines.
- **Multi-Campus Support:** Supporting university information from different campuses.
- **Personalized Student Assistance:** Providing more relevant responses based on a student's department, degree program, or semester, where appropriate student information is available.
- **Administrative Assistance:** Expanding the system to answer questions about admissions, fee structures, registration procedures, and other administrative matters.
- **Source Citations:** Displaying document names, page numbers, or relevant sections alongside generated answers for improved transparency and verification.
- **Multilingual Support:** Enabling students to interact with the assistant in multiple languages.
- **Expanded Document Support:** Integrating additional formats and university information sources as the project evolves.
- **Improved User Management:** Introducing authentication and role-based access for students, faculty, and administrators.

## Conclusion

Bahria Assistant aims to bridge the gap between students and the large amount of academic and administrative information maintained by the university. By combining Large Language Models, semantic search, and Retrieval-Augmented Generation, the system transforms traditional document searching into an interactive question-answering experience.

The project focuses on making university information more accessible, improving the efficiency of information retrieval, and reducing students' dependency on manually searching through lengthy documents. With its modular and scalable architecture, Bahria Assistant also provides a foundation for developing a more comprehensive AI-powered university support system in the future.