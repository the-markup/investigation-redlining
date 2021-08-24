
def setup_dti_cat(row):
    
    '''
    Setup dti categories based on lenders and CFPB approach to them
    '''
    
    dti = row['debt_to_income_ratio']
    
    healthy = ['<20%', '20%-<30%', '30%-<36%', ]
    manageable = ['36', '37', '38', '39', '40', '41', '42',]
    unmanageable = ['43', '44', '45', '46', '47', '48', '49']
    struggling = ['50%-60%', '>60%']
    
    if dti in healthy:
        return '1'
    elif dti in manageable:
        return '2'
    elif dti in unmanageable:
        return '3'
    elif dti in struggling:
        return '4'
        
    elif dti == 'Exempt':
        return '5'
    elif dti == 'null':
        return '6'
        
        
def categorize_cltv(row):
    
    '''
    Use CLTV to create a downpayment flag
    
    '''
    
    cltv = row['cltv_ratio']
    
    if cltv <= 80:
        return '1'
    elif cltv > 80:
        return '2'
        
    else:
        return '3'
        
        
        
def calculate_prop_zscore(row):
    
    '''
    Calculate property z scores 
    Mean and standard deviation are based on ratio below 10
    '''
    
    
    ### This numbers come from 1_property_value_analysis Jupyter Notebook
    standard_deviation = 0.907
    mean = 1.475
    
    prop_value_ratio = row['property_value_ratio']
    
    z_score = ((prop_value_ratio - mean)/standard_deviation)
    
    return z_score
        
def categorize_property_value_ratio(row):
    
    '''
    Creating categories based on z-scores
    '''
    
    prop_value_ratio = row['property_value_ratio']  
    

    ### More than one negative standard deviation
    if prop_value_ratio >= 0.009 and prop_value_ratio <= 0.567:
        return '1'
    
    ### Between negative one standatd deviation and zero
    elif prop_value_ratio >= 0.568 and prop_value_ratio <= 1.474:
        return '2'
        
    ### Between zero and one standard deviation       
    elif prop_value_ratio >= 1.475 and prop_value_ratio <= 2.381:
        return '3'
    
    ### Between one standard deviation and two standard deviations
    elif prop_value_ratio >= 2.382 and prop_value_ratio <= 3.288:
        return '4'
    
    ### Greater than two standard deviations but less than 10 for the property value ratio
    elif prop_value_ratio >= 3.289 and prop_value_ratio < 10:
        return '5'
    
    ### Greater than 10 property value ratio
    elif prop_value_ratio >= 10:
        return '6'
        
    else:
        return '7'

        

def categorize_age(row):
    
    '''
    Creating categories for applicant's age
    '''
    
    age = row['applicant_age']
    
    if age == '<25':
        return '1'
        
    elif age == '25-34':
        return '2'
        
    elif age == '35-44':
        return '3'
        
    elif age == '45-54':
        return '4'
        
    elif age == '55-64':
        return '5'
        
    elif age == '65-74':
        return '6'
        
    elif age == '>74':
        return '7'
        
    elif age == '8888' or age == '9999':
        return '8'
    
    
def categorize_sex(row):
    
    '''
    Categorizing applicant's sex
    '''
    
    sex = row['applicant_sex']
    
    
    if sex == '1':
        return '1'
        
    elif sex == '2':
        return '2'
    
    elif sex == '3' or sex == '4':
        return '3'
        
    elif sex == '6':
        return '6'
        
        
def categorize_underwriter(row):
    
    '''
    Categorizing underwriter to see which main underwriter the lender is using 
    '''
    
    
    aus_cat = row['aus_cat']
    aus1 = row['aus_1']
    
    one_aus = ['1', '2']
    
    
    ### Desktop Underwriter
    if aus_cat in one_aus and aus1 == '1':
        return '1'
    ### Loan Prospector
    elif aus_cat in one_aus and aus1 == '2':
        return '2'
    ### Technology Open to Approved Lenders
    elif aus_cat in one_aus and aus1 == '3':
        return '3'
    ### Guaranteed Underwirting System
    elif aus_cat in one_aus and aus1 == '4':
        return '4'
    ### Other
    elif aus_cat in one_aus and aus1 == '5':
        return '5'
    ### No main AUS
    elif aus_cat == '3':
        return '6'
        
    ### Not Applicable or Exempt
    elif aus1 == '6' or aus1 == '1111':
        return '7'
    
    
def categorize_loan_term(row):
    
    '''
    Categorize loan term into more or less than 30 years or exactly 30 years
    '''
    
    loan_term = row['em_loan_term']
    
    ### 30 year mortgage
    if loan_term == 360:
        return '1'
    ### less than 30
    elif loan_term < 360:
        return '2'
    ### More than 30
    elif loan_term > 360:
        return '3'
    ### Exempts and NAs
    else:
        return '4'
        
        
def categorize_lmi(row):
    
    '''
    Categorize low-to-moderate income neighborhoods
    '''
    
    tract_msa_ratio = row['tract_msa_ratio']
    
    ### Low 
    if tract_msa_ratio > 0 and tract_msa_ratio < 50:
        return '1'
    ### Moderate
    elif tract_msa_ratio >= 50 and tract_msa_ratio < 80:
        return '2'
    ### Middle
    elif tract_msa_ratio >= 80 and tract_msa_ratio < 120:
        return '3'
    ### Upper
    elif tract_msa_ratio >= 120:
        return '4'
    ### None
    elif tract_msa_ratio == 0:
        return '5'
    
    
    
    
    