# Advanced Retrieval-Augmented Generation System with LangChain and Apache Solr

## Overview

This project demonstrates an advanced **Retrieval-Augmented Generation (RAG) system** that processes over **10,000 documents**. It integrates **LangChain** with **Apache Solr** to build a scalable and efficient solution for handling large datasets. The system leverages **big data processing** with **PySpark** and provides a user-friendly interface using **Streamlit**.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
  - [Prerequisites](#prerequisites)
  - [Step 1: Install Python 3.8 or Later](#step-1-install-python-38-or-later)
  - [Step 2: Install Java Development Kit (JDK)](#step-2-install-java-development-kit-jdk)
  - [Step 3: Install Apache Solr](#step-3-install-apache-solr)
  - [Step 4: Install Apache Spark (Optional for PySpark)](#step-4-install-apache-spark-optional-for-pyspark)
  - [Step 5: Install Git](#step-5-install-git)
  - [Step 6: Clone the Repository](#step-6-clone-the-repository)
  - [Step 7: Set Up a Virtual Environment](#step-7-set-up-a-virtual-environment)
  - [Step 8: Install Required Python Packages](#step-8-install-required-python-packages)
  - [Step 9: Set Up OpenAI API Key](#step-9-set-up-openai-api-key)
  - [Step 10: Download NLTK Data](#step-10-download-nltk-data)
  - [Step 11: Start Apache Solr and Create a Core](#step-11-start-apache-solr-and-create-a-core)
  - [Step 12: Preprocess and Index Documents](#step-12-preprocess-and-index-documents)
  - [Step 13: Run the Streamlit Application](#step-13-run-the-streamlit-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Efficient Document Retrieval:** Utilizes Apache Solr for fast indexing and retrieval of documents.
- **Language Model Integration:** Harnesses OpenAI's GPT models via LangChain for generating accurate responses.
- **Big Data Processing:** Handles large volumes of data using PySpark.
- **User-Friendly Interface:** Interactive web application built with Streamlit.
- **Scalable Architecture:** Designed to handle substantial data growth and user load.

---

## Technologies Used

- **Python 3.8+**
- **LangChain**
- **OpenAI GPT Models**
- **Apache Solr**
- **PySpark**
- **Streamlit**
- **NLTK**
- **Apache Spark** (Optional for big data processing)
- **Git**
- **Windows 10 or later**

---

rag-system/
├── app.py                  # Main Streamlit application
├── data/                   # Directory containing the dataset
├── docs/                   # Documentation files
├── index_solr.py           # Script to index documents into Solr
├── preprocess.py           # Script for data preprocessing
├── rag_pipeline.py         # Implementation of the RAG pipeline
├── requirements.txt        # List of required Python packages
├── README.md               # Project README file
└── venv/                   # Python virtual environment


---

## Installation Guide

### Prerequisites

- **Windows 10 or later**
- **Administrator rights** on your laptop
- **Internet connection**

### Step 1: Install Python 3.8 or Later

1. **Download Python Installer:**

   - Visit the [Python Downloads](https://www.python.org/downloads/windows/) page.
   - Download the latest Python 3.x executable installer.

2. **Run the Installer:**

   - Double-click the downloaded installer.
   - **Important:** Check the box **"Add Python 3.x to PATH"** before proceeding.

3. **Complete Installation:**

   - Click **"Install Now"** and follow the prompts.

4. **Verify Installation:**

   - Open **Command Prompt** and run:

     ```bash
     python --version
     ```

   - It should display the installed Python version.

### Step 2: Install Java Development Kit (JDK)

1. **Download JDK:**

   - Visit the [AdoptOpenJDK](https://adoptopenjdk.net/) or [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html) download page.
   - Download **JDK 11** (LTS version).

2. **Install JDK:**

   - Run the installer and follow the prompts.

3. **Set JAVA_HOME Environment Variable:**

   - **Open Environment Variables:**

     - Search for **"Edit the system environment variables"** in the Windows search bar.

   - **Add New System Variable:**

     - Click **"Environment Variables..."**.
     - Under **System variables**, click **"New..."**.
       - Variable name: `JAVA_HOME`
       - Variable value: `C:\Program Files\Java\jdk-11.0.x` (Replace with your actual JDK installation path).

   - **Edit Path Variable:**

     - Under **System variables**, select **"Path"** and click **"Edit..."**.
     - Click **"New"** and add `%JAVA_HOME%\bin`.

4. **Verify Installation:**

   - Open **Command Prompt** and run:

     ```bash
     java -version
     ```

   - It should display the installed Java version.

### Step 3: Install Apache Solr

1. **Download Apache Solr:**

   - Go to the [Apache Solr Downloads](https://lucene.apache.org/solr/downloads.html) page.
   - Download the latest version (e.g., **Solr 8.x.x**).

2. **Extract Solr:**

   - Unzip the downloaded file to a directory, e.g., `C:\solr`.

3. **Start Solr Server:**

   - Open **Command Prompt** as Administrator.
   - Navigate to the Solr `bin` directory:

     ```bash
     cd C:\solr\solr-8.x.x\bin
     ```

   - Start Solr:

     ```bash
     solr start
     ```

   - **Allow Firewall Access:** If prompted by Windows Firewall, click **"Allow access"**.

4. **Verify Solr is Running:**

   - Open a web browser and go to [http://localhost:8983/solr](http://localhost:8983/solr).

### Step 4: Install Apache Spark (Optional for PySpark)

**Note:** This step is optional if you plan to use PySpark for big data processing.

1. **Download Apache Spark:**

   - Visit the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Choose a version and package type (e.g., **Spark 3.x.x pre-built for Apache Hadoop 2.7**).

2. **Extract Spark:**

   - Unzip the downloaded file to `C:\spark`.

3. **Set SPARK_HOME Environment Variable:**

   - **Open Environment Variables:**

     - Search for **"Edit the system environment variables"**.

   - **Add New System Variable:**

     - Variable name: `SPARK_HOME`
     - Variable value: `C:\spark\spark-3.x.x-bin-hadoop2.7` (Replace with your Spark path).

   - **Edit Path Variable:**

     - Add `%SPARK_HOME%\bin` to the `Path` variable.

4. **Verify Installation:**

   - Open **Command Prompt** and run:

     ```bash
     spark-shell
     ```

   - If Spark starts without errors, the installation was successful.

### Step 5: Install Git

1. **Download Git:**

   - Visit the [Git for Windows](https://git-scm.com/download/win) page.

2. **Install Git:**

   - Run the installer and follow the prompts.
   - Select **"Use Git from the command line and also from 3rd-party software"** when prompted.

3. **Verify Installation:**

   - Open **Command Prompt** and run:

     ```bash
     git --version
     ```

### Step 6: Clone the Repository

1. **Open Command Prompt:**

   - Navigate to the directory where you want to clone the project.

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/rag-system.git
   cd rag-system

