import os
import pytest


# Standard python numerical analysis imports:
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json

import warnings
warnings.filterwarnings("ignore")

# the IPython magic below must be commented out in the .py file, since it doesn't work there.

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# LIGO-specific readligo.py 
from ligotools import readligo as rl
from ligotools.utils import *

from ligotools import utils

# you might get a matplotlib warning here; you can ignore it.

eventname = ''
eventname = 'GW150914' 

make_plots = 1
plottype = "png"
fnjson = "data/BBH_events_v3.json"

events = json.load(open(fnjson,"r"))


event = events[eventname]
fn_H1 = event['fn_H1']              # File name for H1 data
fn_L1 = event['fn_L1']              # File name for L1 data
fn_template = event['fn_template']  # File name for template waveform
fs = event['fs']                    # Set sampling rate
tevent = event['tevent']            # Set approximate event GPS time
fband = event['fband'] 


strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/"+ fn_H1, 'H1')

def test_rl_load():
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/"+ fn_H1, 'H1')

def test_load_strain():
    assert type(strain_H1) == np.ndarray
    
def test_load_time():
    assert type(time_H1) == np.ndarray
    
def test_load_dict():
    assert type(chan_dict_H1) == dict
    
    
strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/"+ fn_L1, 'H1')

def test_rl_load2():
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/"+ fn_L1, 'H1')

def test_load_strain2():
    assert type(strain_L1) == np.ndarray
    
def test_load_time2():
    assert type(time_L1) == np.ndarray
    
def test_load_dict2():
    assert type(chan_dict_L1) == dict
    
def test_dq_channel_to_seglist():
    
    data_segments = 1
    if data_segments:
        # read in the data at 4096 Hz:
        # fn = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
        strain, time, chan_dict = rl.loaddata("data/"+fn_L1, 'H1')    

        # select the level of data quality; default is "DATA" but "CBC_CAT3" is a conservative choice:
        DQflag = 'CBC_CAT3'
        # readligo.py method for computing segments (start and stop times with continuous valid data):
        segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert type(segment_list[0])==slice

    
    
########## Test for Utils #########
time = time_H1
# the time sample interval (uniformly sampled!)
dt = time[1] - time[0]
make_psds = 1
if make_psds:
    # number of sample for the fast fourier transform:
    NFFT = 4*fs
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)

    # We will use interpolations of the ASDs computed above for whitening:
    psd_H1 = interp1d(freqs, Pxx_H1)
    psd_L1 = interp1d(freqs, Pxx_L1)

    # Here is an approximate, smoothed PSD for H1 during O1, with no lines. We'll use it later.    
    Pxx = (1.e-22*(18./(0.1+freqs))**2)**2+0.7e-23**2+((freqs/2000.)*4.e-23)**2
    psd_smooth = interp1d(freqs, Pxx)

if make_plots:
    # plot the ASDs, with the template overlaid:
    f_min = 20.
    f_max = 2000. 

whiten_data = 1
    
strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
strain_L1_whiten = whiten(strain_L1,psd_L1,dt)

def test_whiten():
    array_thing = whiten(np.random.uniform(size = 100), psd_H1, 2) 
    
    
def test_reqshift():
    req_mean = np.mean(reqshift(np.random.normal(0,1,100)))
    assert np.round(req_mean) == 0
    
    
def test_write():
    write_wavfile("tester", 4096, np.random.normal(0,1,100))
    assert os.path.exists("tester")
    os.remove("tester")

def test_exists():
    write_wavfile("tester", 4096, np.random.normal(0,1,100))
    confirmation = wavfile.read("tester")
    assert len(confirmation[1])==100
    
    os.remove("tester")