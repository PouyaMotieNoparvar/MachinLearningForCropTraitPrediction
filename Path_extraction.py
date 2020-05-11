import h5py
import pandas as pd
with h5py.File('D:/Dave/G2F_Planting_Season_2017_v1/d._2017_genotypic_data/g2f_2017_ZeaGBSv27_Imputed_AGPv4.h5','r') as hf:
    hf.visit(print)