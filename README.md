# **Binary Classification - Scores for Unbalanced Dataset**  

## **Model Description**  
This notebook involves a Convolutional Neural Network (CNN) trained on a dataset consisting of two classes:  
  - **Normal**: Images corresponding to the normal region of a slide.  
  - **Tumor**: Images corresponding to the tumor region of a slide.  

The goal was to perform annotation using this model on an independent cohort to analyze the survival of patients from whom these slides originated.

### **Current Stage**  
This phase of the project focuses on evaluating our CNN (a DenseNet-based model) on the training data used for its training.

## **Data Folder**  
The **DATA** folder contains the model's prediction probabilities for each slice in the training dataset.

## **History**  
The following graphs show the model's loss function and accuracy evolution across 10 training epochs:

- **Accuracy Curve** (Training vs Validation):  
  ![Accuracy Curve](https://github.com/dinaOuahbi/binary-classification-_-scores-for-unbalanced-dataset/blob/main/acc_train_val.png)

- **Loss Curve** (Training vs Validation):  
  ![Loss Curve](https://github.com/dinaOuahbi/binary-classification-_-scores-for-unbalanced-dataset/blob/main/loss_train_val.png)

### **Note**  
The Python script requires the path to the **DATA** folder as input.
