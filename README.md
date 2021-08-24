### How we analyzed bias in mortgage denials: 

This repository contains the code and data needed to reproduce the findings featured in our stories, “main story link” and “sidebar link.”

Our methodology is described in “methodology link.”

The main federal mortgage dataset can be found on the Consumer Financial Protection Bureau’s website and any supplemental data used for the analysis can be found in the data folder. 

The Jupyter Notebooks are used to clean, categorize, and analyze the federal mortgage data.

### Installation:

Make sure you have Python 3.6+ installed, we used pyenv-virtualenv to create a Python 3.8 virtual environment.

Then install the Python packages: `pip install -r requirements.txt`

### Data:

The 2019 raw HMDA data can be downloaded from the [CFPB website](https://ffiec.cfpb.gov/data-publication/dynamic-national-loan-level-dataset/2019). We are not uploading it here because of its size. When downloading, choose the loan/application records (LAR) dataset. Note: The CFPB updated HMDA data after August 10, 2021 and added XXX records, so some of the numbers may not match ours. 

We used 2019 American Community Survey data for the racial and ethnic demographics of each Census tract in the country––table B03002. We downloaded this data through the Census API and included both the raw and cleaned data. Both of those dataset can be found in the `data/census_data/racial_ethnic_demograhics` directory.

We used 2019 American Community Survey data for the property values for each county in the country––table B25077. We downloaded the data from the Census and included the raw dataset. That dataset can be found in the `data/census_data/property_values` directory.

We used 2019 American Community Survey data for the metro area population, which we downloaded from the Census website and acquired through the Census API. We include both. Those datasets can be found in the `data/census_data/metro_area_pop` directory.


We used a Census dataset that lists all counties in the country the respective metro area that they belong to. That raw dataset is included here. We used this dataset to map counties in HMDA data to their respective metro areas, while incorporating the population categories for each metro area. That dataset is included in the `data/census_data/county_metro_crosswalk` directory. 

The Federal Housing Finance Agency puts out a dataset that accompanies the larger HMDA dataset that lists all the lenders that reported applications to the federal government and specific details about those financial institutions. We received that data as a SAS file and converted it to a CSV. We include the CSV here. We used that file to further define lenders and that standardized version is included in the `data/supplemental_hmda_data` directory. 

### Utils:

The utils directory contains all the Python functions needed to process, clean, and analyze the data. There are three Python files in this directory.

`clean_data.py`: This Python file contains all the functions that are used in the `1_clean_data.ipynb` Jupyter Notebook. The functions clean the geographic fields, the race and ethnicity columns, and action taken columns, among others. It also finds and flags co-applicants among five different fields. 

`categorize_data.py`: This Python file contains all the functions that standardizes the columns that are used in the regression, like debt-to-income ratio, combined loan-to-value ratio, among others. The functions in this Python file are mainly used in the `2_categorize_data.ipynb` notebook.

`use_regression.py`: This Python file contains all the functions needed to run the regression and other statistical tests. The functions in this Python file are mainly used in the `1_regression_analysis.ipynb`, `2_metro_by_metro_regression`, and `3_lender_by_lender_regression` notebooks.


### Notebooks:

The Jupyter Notebooks are split up into two directories: the first for notebooks that process and clean the data and the second for notebooks that analyze the data. These notebooks are intended to be run sequentially.

Process:
`1_clean_data.ipynb`: This first notebook cleans the geographic fields, the race and ethnicity columns, the credit model used columns, and the action taken columns, among others. It also creates a co-applicant field and standardizes the automated underwriter systems columns. It outputs a new dataset and the file is written into the `data/hmda_lar/clean_hmda_data` directory is located in the larger data directory

`2_categorize_data.ipynb`: This notebook categorizes the data fields that will be used in the regression analysis. It standardizes fields like debt-to-income ratio, the mortgage term, and LMI fields, among others. This notebook also brings in supplemental datasets like census data and the lender dataset. The final output is a filtered version of the larger 17 million record HMDA dataset. The output is also written into the  `data/hmda_lar/clean_hmda_data` directory.

### Analysis: 
`1_regression_analysis.ipynb`: The notebook contains the regression analysis used to assess the relationship between race and ethnicity and being denied a mortgage, while holding 17 different variables constant. This notebook outputs a filtered and smaller version of the HMDA data––one that contains only the columns and records used to analyze individual metros and lenders. That dataset also lives in the `data/hmda_lar/clean_hmda_data`.

`2_metro_by_metro_regression`: This notebook contains the code and analysis that looks at individual metros. 

`3_lender_by_lender_regression`: This notebook contains the code and analysis that looks at lending patterns for individual financial institutions. 

### Findings: 
`1_national_findings_210823.csv`: Contains the results of the regression analysis used to analyze the national dataset, while holding 17 variables constant. This CSV is found in the `findings/national_findings` directory.

`1_metro_findings_200823.csv`: Contains the results of the regression analysis used to analyze individual metros. The CSV contains the four racial and ethnic demographics of each metro, along with the categorized results column, a note indicating if the findings are reliable, a note detailing if the findings is considered a disparity, and the odds ratio. To filter for all 89 metros that produced a statistically significant disparity, filter column “reliable_note” for statistically significant disparity. This CSV is found in the `findings/metro_findings` directory.

 `1_lender_finding_file_TKTK`: Contains the results of the regression analysis used to analyze individual lenders. The dataset contains the findings only of the lenders that produced statistically significant disparities and were featured in The Markup story, “SIDEBAR Title.”  This CSV is found in the findings/lender_findings directory.
 


 

### Licensing

Copyright 2021, The Markup News Inc.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

