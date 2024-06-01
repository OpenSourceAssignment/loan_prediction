from django.http import HttpResponse
from django.shortcuts import render
import pickle

# Open the file in binary read mode
with open(r'C:\Users\Eng_Ahmed\projects\OpenSource\Notebooks\model.pkl', 'rb') as file:
    # Load the pickled object (in this case, the model)
    model = pickle.load(file)


# Create your views here.
def Welcome(request):
    return render(request, 'index.html') 

def predict(request):
    return render(request, 'predict.html') 

def formInfo(request):
    full_name=request.POST['full_name']
    Gender=request.POST['gender']
    Married=request.POST['married']
    Dependents=request.POST['dependents']
    Education=request.POST['education']
    Self_Employed=request.POST['employed']
    Credit_History=request.POST['credit']
    Property_Area=request.POST['area']
    ApplicantIncome=request.POST['ApplicantIncome']
    CoapplicantIncome=request.POST['CoapplicantIncome']
    LoanAmount=request.POST['LoanAmount']
    Loan_Amount_Term=request.POST['Loan_Amount_Term']
    print(LoanAmount)
    X_pred=[[Gender,Married,Dependents,Education,Self_Employed,Credit_History,Property_Area,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term]]
    y_predict=model.predict(X_pred)
    if y_predict == 0:
        return render(request, 'predict.html', {'sms': f'{full_name}, Sorry, try next time you cant get loan of {LoanAmount} for that time of {Loan_Amount_Term} month'})
    else:
      return render(request, 'predict.html',{'sms':f'{full_name},congeratulation'})
    