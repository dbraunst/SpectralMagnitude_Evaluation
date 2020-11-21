# HRTF_Estimation

HRTF Estimation of Binaural Soundsources


## Motivation
Recent developments in consumer technology have significantly increased the accessibility and popularity of Extended Reality content, and the incorporation of Spatial Audio is a critical component of that content. The perceptual ability to localize a sound source in space is dependent on a sound source’s volume, time of arrival, and spectral content [1](https://doi.org/10.1121/1.418029), which are all affected by its position relative to the listener. Any sound source can be spatialized over headphones by modifying it’s sound cues through convolution with Head-Related Transfer Functions (HRTFs), which can accurately “fool” the listener into believing that what they’re hearing on headphones is originating at a given horizontal azimuth, vertical elevation, and distance in space [2](http://www.aes.org/e-lib/inst/browse.cfm?elib=8319). 

Due to the way our auditory system decodes the information arriving at each ear, each set of HRTFs is entirely unique in accordance with the listener’s physiology. Obtaining an individual’s HRTFs, however, is a lengthy and expensive process, thus exists a significant body of research in best-fit general HRTFs and their subsequent personalization.



## Sources
1. Wightman, F. L., & Kistler, D. J. (1997). Monaural sound localization revisited. The Journal of the Acoustical Society of America, 101(2), 1050–1063. https://doi.org/10.1121/1.418029]

2. Jot, J.-M., Wardle, S., & Larcher, V. (1998, September 1). Approaches to Binaural Synthesis. Audio Engineering Society Convention 105. http://www.aes.org/e-lib/inst/browse.cfm?elib=8319


3. López, A. P. (2020). Andresperezlopez/ambiscaper [Python]. https://github.com/andresperezlopez/ambiscaper (Original work published 2017)
4. Lostanlen, V., Cella, C.-E., Bittner, R., & Essid, S. (2019). Medley-solos-DB: A cross-collection dataset for musical instrument recognition [Data set]. Zenodo. https://doi.org/10.5281/zenodo.3464194
5. Crawford, S., Audfray, R., & Jot, J.-M. (2020, August 13). Quantifying HRTF Spectral Magnitude Precision in Spatial Computing Applications. Audio Engineering Society Conference: 2020 AES International Conference on Audio for Virtual and Augmented Reality. http://www.aes.org/e-lib/browse.cfm?elib=20869 