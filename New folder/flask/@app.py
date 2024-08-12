@app.route('/predict', methods=['GET', 'POST'])

def predict():

Age = request.form['Age'] EmploymentType= request.form['EmploymentType"]

if EmploymentType== 'Private Sector/Self Employed':

EmploymentType=1

if EmploymentType == Government Sector': EmploymentType 0

AnnualIncome = request.form['Annual Income']

FamilyMembers = request.form['FamilyMembers']

ChronicDiseases = request.form['ChronicDiseases']

if ChronicDiseases== 'Yes':

ChronicDiseases = 1

if ChronicDiseases == 'No':

ChronicDiseases

= 0

FrequentFlyer= request.form['FrequentFlyer']

if FrequentFlyer== 'Yes':

FrequentFlyer = 1 if FrequentFlyer == No:

FrequentFlyer = 0

EverTravelledAbroad= request.form['EverTravelledAbroad"]

if EverTravelledAbroad== 'Yes': EverTravelledAbroad = 1 if EverTravelledAbroad == 'No':

EverTravelledAbroad = 0