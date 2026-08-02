MedShield-AI
MedShield-AI is a machine learning project I created to predict the likelihood of heart disease based on a patient's medical data.
I developed this project to understand how machine learning can be used in healthcare and to build a straightforward application that can give fast risk assessments. It is intended as an educational tool and is not meant for actual medical diagnosis.

The model used for prediction is a Random Forest Classifier trained on the UCI Heart Disease Dataset.
Before training, I prepared the dataset by addressing missing values and converting categorical features into numerical formats. After this preprocessing step, I split the data into training and testing sets. The model performed with an accuracy of roughly 89% on the test set.

The application is developed using Streamlit, which makes it easy to use.
Users can input the necessary patient information, click a button to get the prediction, and immediately see if the patient is classified as Low Risk or High Risk for heart disease. The app also shows the confidence level of the prediction, offers a brief health suggestion, and provides a summary of the entered information.

###  Features

- Heart disease risk prediction using machine learning
- Simple and interactive user interface with Streamlit
- Displays the confidence level of the prediction
- Gives a basic health recommendation
- Shows a summary of the patient's entered details

###  Project Structure

```
MedShield-AI/
│── app.py
│── models/
│ ├── heart_disease_model.pkl
│ └── feature_columns.pkl
│── data/
│ └── heart.csv
│── notebook/
│ └── Heart_Disease_Prediction.ipynb
│── requirements.txt
│── README.md
```

###  How to Run

1.
Clone the repository.
2.
Create and activate a virtual environment.
3.
Install the required packages using `pip install -r requirements.txt`.
4.
Start the application by running:

```bash
streamlit run app.py
```

###  Future Improvements

There are several ways this project could be enhanced in the future.
Some ideas include training the model on more extensive datasets, experimenting with different machine learning or deep learning methods, incorporating user authentication, saving the history of predictions, and deploying the application online for global access.

###  Disclaimer

This project was developed for educational and research purposes only.
The predictions provided should not be taken as medical advice and should not replace consultation with a qualified healthcare professional.

###  Author

Isha Saleem
Bachelor of Computer Science
The Shaikh Ayaz University, Shikarpur

###  License

This project is shared for academic and educational use.
