import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.proportion as stm
import scipy.stats as st
import math

headers = ["Subject_identifier", "Jitter_Percent", "Jitter_MicroSecond","Jitter_r.a.p",
           "Jitter_ppq5", "Jitter_ddp", "Shimmer_Percent","Shimmer_Db","Shimmer_apq3" ,
           "Shimmer_apq5", "Shimmer_apq11", "Shimmer_dda", "Harmonicity_correlation", 
           "Harmonicity_NHR", "Harmonicity_HNR", "Pitch_median", "Pitch_mean", "Pitch_std",
           "Pitch_min", "Pitch_max", "Pulse_number", "Pulse_periods", "Pulse_meanperiod", 
           "Pulse_stdperiod", "Voice_fraction_unvoiced_frames", "Voice_number_voice_breaks",
           "Voice_degree_voice_breaks", "UPDRS", "PD_indicator"]
df = pd.read_csv('po1_data.txt', header=None, names=headers)
df

#Identify Levels of Measurement for Columns
Nominal_data = ["Subject_identifier" , "PD_indicator"]
Ordinal_data = ["Jitter_MicroSecond","Jitter_r.a.p","Jitter_ppq5", "Jitter_ddp","Shimmer_Db",
                "Shimmer_apq3" ,"Shimmer_apq5", "Shimmer_apq11", "Shimmer_dda", "Harmonicity_correlation", 
                "Harmonicity_NHR", "Harmonicity_HNR", "Pitch_median", "Pitch_mean", "Pitch_std", "Pitch_min", 
                "Pitch_max", "Pulse_number", "Pulse_periods", "Pulse_meanperiod", "Pulse_stdperiod", 
                "Voice_fraction_unvoiced_frames", "Voice_number_voice_breaks", "Voice_degree_voice_breaks", "UPDRS"]
Interval_data = []
Ratio_data = []
Percent_data = ["Jitter_Percent", "Shimmer_Percent" ]

#Data of people with pd
with_pd = df[df["PD_indicator"] == 1]
with_pd

#Data of people without pd
without_pd = df[df["PD_indicator"] == 0]
without_pd


# Confidence level
conf_lvl = 0.95
alpha = 1 - conf_lvl


df_new1 = df
# Iterate through columns in the DataFrame
for column in df_new1.columns:
    if column in Percent_data or column in Ordinal_data:
        x_bar = df_new1[column].mean()
        s = df_new1[column].std()
        n = len(df_new1[column])
        
        # Z-score (assuming 95% Confidence Level)
        z_score = st.norm.ppf(q=1 - alpha / 2)
        
        # Compute standard error
        std_err = s / math.sqrt(n)
        
        # Compute the margin of error
        mrg_err = z_score * std_err
        
        # Get the lower and upper bound of the confidence interval
        ci_low = x_bar - mrg_err
        ci_upp = x_bar + mrg_err
        
        print(f"Column '{column}' - Mean: {x_bar:.2f}. Standard deviation: {s:.2f}. Size: {n}.")
        print(f"Confidence Interval of the mean: {ci_low:.2f} to {ci_upp:.2f}\n")
        
        
        
def t_test(group1, group2, columns):
    t_statistic, p_value = st.ttest_ind(group1[columns], group2[columns])
    return t_statistic, p_value

comparison_columns = ["Jitter_Percent","Pitch_mean", "Shimmer_Percent", "Harmonicity_correlation"]
for columns in comparison_columns:
    t_stat, p_val = t_test(without_pd, with_pd, columns)
    print(f"T-Test results for '{columns}':")
    print(f"  T-Statistic: {t_stat}")
    print(f"  P-Value: {p_val}")
    if p_val < 0.05:
        print("  Conclusion: Reject null hypothesis (significant difference)")
    else:
        print("  Conclusion: Fail to reject null hypothesis (no significant difference)")
    print()