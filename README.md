🩺 MedShield-AI

MedShield-AI is a project I developed to predict the risk of heart disease using machine learning. The main goal was to explore how AI can help identify possible heart-related risks at an early stage so that patients can seek medical attention sooner if needed. The prediction model is based on a Random Forest classifier trained using the UCI Heart Disease dataset.

The application is built with Streamlit, which makes it simple and easy to use. Users only need to enter the required patient information, and the system quickly predicts whether the patient is at low or high risk of heart disease. Along with the prediction, the application also displays a probability score, a short health recommendation, and a summary of the entered patient information.

Before training the model, the dataset was cleaned by handling missing values and encoding categorical features. After preprocessing, the data was divided into training and testing sets. The Random Forest model was then trained using Scikit-learn and achieved an accuracy of approximately 89% on the test dataset. The model performs binary classification by separating patients into Low Risk and High Risk categories.

The project is organized into separate folders for the application, dataset, trained model, and Jupyter notebook. To run the project, clone the repository, create a virtual environment, install the required packages from the requirements.txt file, and launch the application using Streamlit.

There are several ways this project could be improved in the future, such as training on larger medical datasets, experimenting with deep learning models, adding user authentication, or deploying the application online. For now, MedShield-AI is intended for educational and research purposes only and should not be considered a replacement for professional medical advice.

👩‍💻 Author

Isha Saleem
Bachelor of Computer Science
The Shaikh Ayaz University, Shikarpur

📜 License

This project was developed for academic and educational purposes only.