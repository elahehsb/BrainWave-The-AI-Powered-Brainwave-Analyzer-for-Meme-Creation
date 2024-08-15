import numpy as np
import mne

def load_eeg_data(file_path):
    raw = mne.io.read_raw_fif(file_path, preload=True)
    return raw.get_data()

def preprocess_data(eeg_data):
    # Apply band-pass filter to EEG data
    filtered_data = mne.filter.filter_data(eeg_data, sfreq=1000, l_freq=1, h_freq=50)
    return filtered_data

def extract_features(filtered_data):
    # Simple feature extraction: mean and variance
    mean = np.mean(filtered_data, axis=1)
    variance = np.var(filtered_data, axis=1)
    return np.concatenate((mean, variance))
