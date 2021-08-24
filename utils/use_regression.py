import pandas as pd
import numpy as np

import statsmodels.formula.api as smf

from sklearn.metrics import confusion_matrix, accuracy_score
from functools import reduce
from tqdm import tqdm



def create_dummy_vars(df, columns):
    '''
    Create dummy variables based on values being isolated in the list of dict being passed
    '''
    
    
    for column in columns:
        dummy_vars = columns[column]
        
        for dummy_var in dummy_vars:
            
            var_value = dummy_vars[dummy_var]

            df.loc[(df[column].isin(var_value)), dummy_var] = 0
            df.loc[~(df[column].isin(var_value)), dummy_var] = 1
    
    return df
    
def create_formula(independent_vars):
    '''
    Create formula from a list of variables
    '''
    
    
    dummy_vars = str(str(independent_vars)[2:-2].replace('\', \'', ' + '))
    regression_formula = ("denied ~ " + dummy_vars)
    
    return regression_formula
    

def run_regression(data, formula):
    '''
    use statsmodel to run regression
    '''
    
    model = smf.logit(data = data, formula = formula)
    
    return model
    
    
    
def calculate_vif(independet_df):
    '''
    Calculate VIF
    '''
    
    vif_list = []
    
    x_cols = independet_df.columns
    
    for x_col in tqdm(x_cols):
        
        x = independet_df[[x_col]]
        y = independet_df.drop(columns = x_col)
        
        rsq = smf.ols(formula = 'x~y', data = independet_df).fit().rsquared
        vif = round(1/(1-rsq), 2)
        
        if vif > 2.5:
            ### 1 for concern
            threshold_flag = '1'
            
        elif vif <= 2.5:
            ### 0 for no concern
            threshold_flag = '0'
        
        
        var_dict = {'independent_var': x_col, 'vif': vif, 'threshold': threshold_flag}
        vif_list.append(var_dict)
        
    vif_df = pd.DataFrame(vif_list)
    return vif_df
    
    
def calcuate_confusion_matrix(df, model, indepndent_vars, dependent_vars):
    '''
    Calculate confusion matrix
    '''
    
    
    testX = df[indepndent_vars]
    testY = df[dependent_vars]
    
    
    yhat = model.predict(testX)
    prediction = list(map(round, yhat))
    
    cm = confusion_matrix(testY, prediction)  
    print ("Confusion Matrix : \n", cm)
    
    # accuracy score of the model 
    print('Overall accuracy: ', accuracy_score(testY, prediction) * 100)
    print('Denied accuracy: ', (cm[0, 0]/(cm[0, 0] + cm[0, 1])) * 100)
    print('Loan accuracy : ', (cm[1, 1]/(cm[1, 0] + cm[1, 1])) * 100)
    

def convert_results_to_df(model):
    '''
    Convert the summary results from regression into dataframe
    '''
    
    coef_dict = {'results': dict(model.params), 'col_name': 'coefficient'}
    std_error_dict = {'results': dict(model.bse), 'col_name': 'standard_error'}
    tvalues_dict = {'results': dict(model.tvalues), 'col_name': 'z_value'}
    pvalues_dict = {'results': dict(model.pvalues), 'col_name': 'p_value'}
    oddsratio_dict = {'results': dict(np.exp(model.params)), 'col_name': 'odds_ratio'}
    
    results_dicts = [coef_dict, std_error_dict, tvalues_dict, pvalues_dict, oddsratio_dict]
    
    dfs = []    
    for results_dict in results_dicts:
        col_name = results_dict['col_name']
        df = pd.DataFrame.from_dict(results_dict['results'], orient = 'index').reset_index().rename(columns = {'index': 'variable_name', 0: col_name})
        dfs.append(df)

    
    results_df = reduce(lambda left, right: pd.merge(left, right, on = ['variable_name']), dfs)
    results_df.insert(1, 'pseudo_rsquared', model.prsquared)
    
    return results_df
        
        
        
    
        
        