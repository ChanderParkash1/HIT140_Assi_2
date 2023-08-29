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

