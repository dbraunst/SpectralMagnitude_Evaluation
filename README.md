# HRTF_Estimation

HRTF Estimation of Binaural Soundsources utilizing HRTF Spectral Magnitude Precision

## Motivation
Recent developments in consumer technology have significantly increased the accessibility and popularity of Extended Reality content, and the incorporation of Spatial Audio is a critical component of that content. The perceptual ability to localize a sound source in space is dependent on a sound source’s volume, time of arrival, and spectral content<sup>[1](https://doi.org/10.1121/1.418029)</sup>, which are all affected by its position relative to the listener. Any sound source can be spatialized over headphones by modifying it’s sound cues through convolution with Head-Related Transfer Functions (HRTFs), which can accurately “fool” the listener into believing that what they’re hearing on headphones is originating at a given horizontal azimuth, vertical elevation, and distance in space <sup>[2](http://www.aes.org/e-lib/inst/browse.cfm?elib=8319)</sup>. 

Due to the way our auditory system decodes the information arriving at each ear, each set of HRTFs is entirely unique in accordance with the listener’s physiology. Obtaining an individual’s HRTFs, however, is a lengthy and expensive process<sup>[3](https://doi.org/10.1109/ISMAR.2014.6948409)</sup>, thus exists a significant body of research dedicated to finding best-fit general HRTFs and their subsequent personalization.

## Problem
Much of the existing research on HRTF personalization focuses on determination of the listener’s physical traits<sup>[4](http://www.aes.org/e-lib/browse.cfm?elib=20870)</sup> and altering the generic HRTF based on the estimated features to provide a ‘better fitting’ HRTF. That approach, however, is only valid if the personalization process happens alongside the HRTF convolution. If the audio has already been spatialized, but the HRTF was not a good match for the listener, the listener will experience a noted degradation in sound source accuracy, to the point where they may not perceive any spatialization. Identification of the HRTF used could provide a means by which to re-calculate the previously spatialized audio in a manner more plausible and accurate to the listener. 

## Proposed Method
We seek to adapt a recent method for deriving the spectral magnitude precision of a sound source given a known HRTF introduced by Crawford et al<sup>[5](http://www.aes.org/e-lib/browse.cfm?elib=20869)</sup>, which results in a feature vector they term the “Mean Opinion Score” (MOS). This method was originally intended to be used to evaluate processing effects on sound source representation to monitor for signal/location degradation. We propose that by calculating an already-processed signal’s MOS using multiple sets of HRTFs, we can predict the original HRTF used by comparing the resultant MOS vector.

This project will involve the creation of a dataset of first-order ambisonic musical examples, adapted from the existing Medley Solos DB database <sup>[6](https://doi.org/10.5281/zenodo.3464194)</sup>, spatialized using Perez-Lopez' AmbiScaper<sup>[7](https://github.com/andresperezlopez/ambiscaper)</sup>. These examples will, in turn, each be convolved with multiple sets of HRTFs, leading to the final dataset to be evaluated via MOS comparison. 

## Sources
1. Wightman, F. L., & Kistler, D. J. (1997). Monaural sound localization revisited. The Journal of the Acoustical Society of America, 101(2), 1050–1063. https://doi.org/10.1121/1.418029]

2. Jot, J.-M., Wardle, S., & Larcher, V. (1998, September 1). Approaches to Binaural Synthesis. Audio Engineering Society Convention 105. http://www.aes.org/e-lib/inst/browse.cfm?elib=8319
3. Meshram, A., Mehra, R., Yang, H., Dunn, E., Franm, J., & Manocha, D. (2014). P-HRTF: Efficient personalized HRTF computation for high-fidelity spatial sound. 2014 IEEE International Symposium on Mixed and Augmented Reality (ISMAR), 53–61. https://doi.org/10.1109/ISMAR.2014.6948409 
4. Islam, M. T., & Tashev, I. (2020, August 13). Anthropometric Features Estimation Using Integrated Sensors on a Headphone for HRTF Personalization. Audio Engineering Society Conference: 2020 AES International Conference on Audio for Virtual and Augmented Reality. http://www.aes.org/e-lib/browse.cfm?elib=20870
5. Crawford, S., Audfray, R., & Jot, J.-M. (2020, August 13). Quantifying HRTF Spectral Magnitude Precision in Spatial Computing Applications. Audio Engineering Society Conference: 2020 AES International Conference on Audio for Virtual and Augmented Reality. http://www.aes.org/e-lib/browse.cfm?elib=20869 
6. Lostanlen, V., Cella, C.-E., Bittner, R., & Essid, S. (2019). Medley-solos-DB: A cross-collection dataset for musical instrument recognition [Data set]. Zenodo. https://doi.org/10.5281/zenodo.3464194
7. López, A. P. (2020). Andresperezlopez/ambiscaper [Python]. https://github.com/andresperezlopez/ambiscaper (Original work published 2017)


##
Sam is adding this line of code in the README doc
