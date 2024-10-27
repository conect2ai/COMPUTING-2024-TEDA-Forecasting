<p align="center">
  <img width="800" src="./figures/conecta_logo.png" />
</p> 

# TEDA-Forecasting: An Unsupervised TinyML Incremental Learning Approach for Outlier Processing and Forecasting


### ✍🏾Authors:  [Pedro Andrade](https://github.com/pedrohmeiraa), [Morsinaldo Medeiros](https://github.com/Morsinaldo), [Ivanovitch Silva](https://github.com/ivanovitchm), [Marianne Diniz](https://github.com/MarianneDiniz), and [Daniel G. Costa](https://github.com/daniel-gcosta).


# 1. Abstract/Overview

The expansion of smart systems and the Internet of Things (IoT) has increased data generation, demanding efficient real-time processing techniques. In this scenario, edge computing and TinyML, which allow the execution of machine learning models on low-power microcontrollers, emerge as promising solutions. However, there are still challenges in developing lightweight algorithms capable of processing continuous data streams on devices with limited resources. In this article, we propose TEDA-Forecasting, a time series forecasting algorithm based on the Typicality and Eccentricity Data Analytics (TEDA) technique, designed to operate on TinyML platforms. To validate this innovative algorithm, we consider different types of input data, as well as its actual embedding on a real-world edge device for more practical evaluation, efficiently enabling anomaly detection and outlier correction in the input streams. The achieved results indicate that TEDA-Forecasting offers high accuracy with energy efficiency, demonstrating its potential for applications in resource-constrained IoT systems, such as those enabled by the emerging TinyML paradigm.
  
For a better didactic exposition, the results will be presented in 9 notebooks:

 1. :notebook: Explaining the TEDA Forecasting
 2. :notebook: TEDA Forecasting on WandB
 3. :orange_book: Combination of TEDA and LSTM algorithms (TEDA-LSTM)
 4. :orange_book: TEDA-LSTM on WandB
 5. :blue_book: Combination of TEDA and KNN algorithms (TEDA-KNN)
 6. :blue_book: TEDA-KNN on WandB
 7. :closed_book: Comparison between TEDA Forecasting, TEDA-LSTM and TEDA-KNN
 8. :green_book: Comparing Freematics, Arduino, C++ e Python
 9. :ledger: Comparison with Lazy Predict

# 2. Environment Setup
First, start by cloning the repository:
```bash
git clone https://github.com/conect2ai/COMPUTING-2024-TEDA-Forecasting.git
```

We also have cloned the `Padasip` repository:
```bash
git clone https://github.com/matousc89/padasip
```
It is possible to install using `pip`:
```bash
!pip3 install padasip
```
- The **Padasip** (*Python Adaptive Signal Processing*) is a library designed to simplify adaptive signal processing tasks within Python (filtering, prediction, reconstruction, classification). More information [here](https://matousc89.github.io/padasip/).  :twisted_rightwards_arrows:

Now, we are going to install the  `WandB`: 💻

```bash
!pip3 install wandb -qU
```
 - If you want to know more about software package **WandB**, click [here](https://wandb.ai/site).  :bar_chart:
 
## 2.1 How to run on Freematics One+

1. Install [Visual Studio Code](https://code.visualstudio.com/)
2. Install [PlatformIO](https://platformio.org/) (VSCode Extension)
3. Clone this repository:

```bash
git clone https://github.com/conect2ai/ELSEVIER-2024-TEDA-Forecasting.git
```

4. Open the project folder `./Freematics/firmware_v5/telelogger` on PlatformIO, as illustrated in the figure below.

<p align="center">
  <img width="800" src="./figures/platformio.png" />
</p> 

5. Connect the Freematics One+ to your computer and turn it on using the Freematics Emulator or in the vehicle.

6. Compile, upload and monitor the serial (steps 1, 2 and 3, respectively in the figure below).

<p align="center">
  <img width="800" src="./figures/upload.png" />
</p> 


# 3. References

 [AJUSTAR]
 
 [[1]](https://www.mdpi.com/1424-8220/22/10/3838) :books: **Andrade, P.**; Silva, I.; Silva, M.; Flores, T.; Cassiano, J.; Costa, D.G. *A TinyML Soft-Sensor Approach for Low-Cost Detection and Monitoring of Vehicular Emissions*. SENSORS 2022, 22, 3838.  ![GitHub](https://img.shields.io/badge/DOI-10.3390%2Fs22103838-green)

[[2]](https://www.mdpi.com/1424-8220/21/12/4153) :books: Signoretti, G. ; Silva, M. ; **Andrade, P.**; Silva, I. ; Sisinni, E. ; Ferrari, P.; *An Evolving TinyML Compression Algorithm for IoT Environments Based on Data Eccentricity*. SENSORS 2021, v. 21, p. 4153. ![GitHub](https://img.shields.io/badge/DOI-10.3390%2Fs21124153-green)

[[3]](https://dl.acm.org/journal/tecs) :books: **Andrade, P.**; Silva, I.; Silva, M.; Flores, T.; Costa, D.G. Soares, E.; _Online Processing of Vehicular Data on the Edge Through an Unsupervised TinyML Regression Technique_. ACM TECS 2023. ![GitHub](https://img.shields.io/badge/DOI-under%20review-blue)

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# About us

The research group [**Conect2AI**](http://conect2ai.dca.ufrn.br) consists of undergraduate and graduate students from the Federal University of Rio Grande do Norte (UFRN) and aims to apply Artificial Intelligence (AI) and machine learning in emerging fields. Our expertise includes Embedded Intelligence and IoT, optimizing resource management and energy efficiency, contributing to sustainable cities. In energy transition and mobility, we apply AI to optimize energy use in connected vehicles and promote more sustainable mobility.