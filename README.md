# 🚀 DocAssist - Intelligent Medical Decision Support System  

DocAssist is a **machine-learning-based project** designed to help doctors determine if a patient requires treatment based on **blood analysis data**.  
This project uses **Flask for the web UI** and a **Random Forest model for predictions**.  

---

## **📁 Project Structure**

      D:
      ¦   Project_report.pdf # Project detail report
      ¦   README.md # Project Documentation
      ¦   requirements.txt # Required Python Packages
      ¦   test_model.py # Optional Script to Test Model
      ¦   
      +---app # Flask Web Application
      ¦   ¦   app.py # Flask Application
      ¦   ¦   
      ¦   +---templates # HTML templates
      ¦           index.html # Web UI
      ¦           
      +---data # Dataset Storage
      ¦       dataset.xlsx # Raw Dataset
      ¦       preprocessed_data.csv # Processed Dataset
      ¦       
      +---models # Trained Machine Learning Model
      ¦       final_model.pkl # Saved Model
      ¦       
      +---notebooks # Jupyter Notebooks
      ¦       exploratory_analysis.ipynb  # Data Analysis
      ¦       model_training.ipynb # For Model Training
      ¦       
      +---utils
        preprocess.py # Data Preprocessing


## **Project Setup and Execution**

###  Step 1: Clone the Repository or Download the ZIP

Clone the repository or download the ZIP file:
     
     git clone https://github.com/shruthipanarajan/DocAssist

Alternatively, download and extract the ZIP file

### Step 2: Folder Structure

Ensure your project has the following folder structure as metioned above 

### Step 3: Install Dependencies

Navigate to the project directory and install the required Python packages using:

     pip install -r requirements.txt

### Step 4: Data Exploration and Model Training

1. Open the notebooks folder and run exploratory_analysis.ipynb to analyze the dataset.
2. Run model_training.ipynb to preprocess the data and train the model.
3. The trained model will be saved as final_model.pkl inside the models folder.

### Step 5: Running the Flask App

#### Using VS Code

1. Open the project in VS Code.
2. Ensure final_model.pkl is present inside the models folder.
3. Navigate to the app folder and run:
          
        python app.py
4. A local server link will appear in the terminal. Click on it or copy and paste it into your browser.

#### Using Command Prompt or PowerShell

1. Open the Command Prompt or PowerShell inside the project folder.
2. Navigate to the app directory:
      
         cd app
3. Run:
   
         python app.py
4. A local connection link will be displayed. Open the link in your browser.

### Step 6: Using the Web Interface

1. Enter the requested blood test values in the form.
2. Click Submit to get the prediction.
3. The model will indicate whether treatment is required or not required.

### Step 7: Testing the Model(Optional)

To test the model separately, you can run:
   
      python test_model.py
This script will validate the trained model’s predictions.

### Step 8: Stopping the Application

Once done, press Ctrl + C in the terminal to stop the Flask application.

## **Sample Data for Testing**

### Male Sample Data
<table border="1">
<tr>
<th>HAEMATOCRIT</th><th>HAEMOGLOBINS</th><th>ERYTHROCYTE</th><th>LEUCOCYTE</th><th>THROMBOCYTE</th><th>MCH</th><th>MCHC</th><th>MCV</th><th>AGE</th><th>SEX</th>
</tr>
<tr>
<td>45.2</td><td>15.0</td><td>5.50</td><td>7.2</td><td>250</td><td>30.1</td><td>34.0</td><td>85.4</td><td>30</td><td>M</td>
</tr>
<tr>
<td>42.8</td><td>13.5</td><td>5.10</td><td>6.5</td><td>300</td><td>28.7</td><td>33.2</td><td>88.0</td><td>50</td><td>M</td>
</tr>
</table>

### Female Sample Data
<table border="1">
<tr>
<th>HAEMATOCRIT</th><th>HAEMOGLOBINS</th><th>ERYTHROCYTE</th><th>LEUCOCYTE</th><th>THROMBOCYTE</th><th>MCH</th><th>MCHC</th><th>MCV</th><th>AGE</th><th>SEX</th>
</tr>
<tr>
<td>38.5</td><td>12.0</td><td>4.60</td><td>7.8</td><td>320</td><td>31.2</td><td>32.5</td><td>86.5</td><td>28</td><td>F</td>
</tr>
<tr>
<td>36.9</td><td>11.2</td><td>4.20</td><td>6.9</td><td>290</td><td>30.5</td><td>31.8</td><td>84.2</td><td>40</td><td>F</td>
</tr>
</table>
