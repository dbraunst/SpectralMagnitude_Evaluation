# MOS Utilities FILE
import numpy as np
import scipy.signal

def dB_weighted_fft(signal):

    # import numpy
    
    # Parameters
    # ----------

    # Returns
    # -------
    
    # dB-weighted magnitude FFT of signal [shape=(2,(N_FFT / 2) - 1)]
    
    sig_L_fft = 20 * np.log10(np.abs(scipy.fft.fft(signal[0])))
    sig_R_fft = 20 * np.log10(np.abs(scipy.fft.fft(signal[1])))
    
    sig_L_fft = sig_L_fft[0:int(len(sig_L_fft)/2)]
    
    sig_R_fft = sig_R_fft[0:int(len(sig_R_fft)/2)]
    
    db_weighted_signal = np.array([sig_L_fft, sig_R_fft])

    return db_weighted_signal 

def flatten_HRTF(input_HRTF):
#     '''
#     flattens the first two dimensions of the HRTF, 
#     typically indexed by [azi, ele] for the first two dimensions,
#     in order to beter work with Elastic-Net Regression
    
#     Parameters
#     ----------
#     input_HRTF : np.ndarray, [shape=(72, 12, 2, 256)
        

#     Returns
#     -------
#     flattened_HRTF : np.ndarray, [shape=(1008, 2, 256)]
    
#     '''
    idx = 0;
    flat_len = input_HRTF.shape[0] * input_HRTF.shape[1];
    
    flattened_HRTF = np.empty((flat_len, 2, 128));
    
    for i in range(0, input_HRTF.shape[0]):
        for j in range(0, input_HRTF.shape[1]):
            flattened_HRTF[idx] = input_HRTF[i, j];
            idx = idx + 1;
    
    return flattened_HRTF;

def flatten_HRTF_mono(input_HRTF):
    
    idx = 0;
    flat_len = input_HRTF.shape[0] * input_HRTF.shape[1]
    
    flattened_HRTF_L = np.empty((flat_len, 128));
    flattened_HRTF_R = np.empty((flat_len, 128));
    
    for i in range(0, input_HRTF.shape[0]):
        for j in range(0, input_HRTF.shape[1]):
            flattened_HRTF_L[idx] = input_HRTF[i, j, 0];
            flattened_HRTF_L[idx] = input_HRTF[i, j, 1];
            idx = idx + 1;
    
    return flattened_HRTF_L, flattened_HRTF_R;

def get_HRIR(HRTF, azi=0, ele=0, warnings=True, verbose=True):
    
    # Get the closest corresponding impulse response to 
    
    
    # Parameters
    # ----------
    #     HRTF   : np.array, shape(72, 12, 2, 256)
    #         HRTF to pull IR from
            
    #     azi : integer
    #         azimuth angle, either 0 < azi < 360 or -180 < azi < 180
            
    #     ele : integer
    #         elevation angle,  -75 < ele < 90
            
    #     warnings : boolean
    #         allows for warnings printout
    
    # Returns
    # -------
    #     IR_out  :  np.array, shape(n, 2)
    #         Stereo Impulse response from chosen (or closest) azimuth and elevation
    
    # Flag to print out warning if input azi/ele didn't correspond with 
    closestChoiceFlag = False;
    negAziFlag = False;
    nearestAzi = 0;
    nearestEle = 0;
    
    # Check Azimuth input, convert to 0-359 if needed
    if (azi < 0 and azi >=-180):
        negAzi = azi;
        negAziFlag = True; # Adjusts warning for legibility
        azi = azi + 360;
    elif (azi <= -180 or azi >= 360):
        print("Error: Azimuth must be between 0 and 360 or -180 and 180. Your input:", azi);
        return -1;
    elif (azi == 360):
        azi = 0;
    
    # Check desired Azimuth value against known HRIR azimuth angles
    if (azi % 5 == 0):
        chosenAzi = azi
        aziIdx = int(chosenAzi / 5)
    else:
        closestChoiceFlag = True;
        chosenAzi = ((azi - azi % 5)) + (round(azi % 5 / 5) * 5)
        aziIdx = int(chosenAzi / 5)
        
        
    # Check Elevation input
    if (ele < -75 or ele > 90):
        print("Error: Elevation must be between -75 and 90. Your input:", ele);
        return -1;
    
    # Check desired Elevation value against known HRIR elevation angles
    if (ele % 15 == 0):
        chosenEle = ele
        eleIdx = int((chosenEle + 75) / 15);
    else:
        closestChoiceFlag = True;
        chosenEle = ((ele - ele % 15)) + (round(ele % 15 / 15) * 15)
        eleIdx = int((chosenEle + 75) / 15);
        
    if(verbose == True):
        print("Azi =", chosenAzi, "deg| Ele = ", chosenEle, "deg");
        print("AziIdx =",aziIdx,"| EleIdx =", eleIdx);
    
    # printout warning
    if (warnings == True and closestChoiceFlag == True):
        if (negAziFlag == True):
            print("Warning! Chosen Azi, Ele of [", negAzi, ele, "] do not match current HRTF set.",\
             "\nUsing nearest Azi, Ele fit of [", (chosenAzi - 360), chosenEle,\
             "]\n...To disable this warning, call function with 'warnings=False' ");
        else: 
            print("Warning! Chosen Azi, Ele of [", azi, ele, "] do not match current HRTF set.",\
             "\nUsing nearest Azi, Ele fit of [", chosenAzi, chosenEle,\
             "]\n...To disable this warning, call function with 'warnings=False' ");
            
    output = HRTF[aziIdx, eleIdx]
    
    return output

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
