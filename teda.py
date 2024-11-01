import numpy as np


class TEDA:
    """Class used to detect outliers on the dataset"""
    # ------------------------------
    # CONSTRUCTOR
    #-------------------------------
    def __init__(self, threshold):
        # initialize variables
        self.k = 1
        self.variance = 0
        self.mean = 0
        self.threshold = threshold

    # ------------------------------
    # INTERNAL METHODS
    #------------------------------- 
    def __calcMean(self, x):
        return ((self.k-1)/self.k)*self.mean + (1/self.k)*x
    
    def __calcVariance(self, x):
        distance_squared = np.square(np.linalg.norm(x - self.mean))
        return ((self.k-1)/self.k)*self.variance + distance_squared*(1/(self.k - 1))
                                     
    def __calcEccentricity(self, x):
        #if(self.variance == 0):
        #    self.variance = 0.00001
            
        if(self.variance == 0):
            new_ecc = 0
            return new_ecc
     
        if (isinstance(x, float)):
            return (1 / self.k) +  (((self.mean - x)*(self.mean - x)) / (self.k *  self.variance))    
        else:
            return (1 / self.k) +  (((self.mean - x).T.dot((self.mean - x))) / (self.k *  self.variance))
            
        
    
    # ------------------------------
    # RUN METHODS
    #-------------------------------
    def run_offline(self, df, features):
        """Run the algorithm offline"""
        
        # add is_outlier column to the dataframe
        df['is_outlier'] = 0
        
        # loop through the rows in df
        for index, row in df.iterrows():
            # build the X sample numpy array
            x = np.array(row[features])
            
            # update the model metrics
            if(self.k == 1):
                self.mean = x
                self.variance = 0
            else:
                # calculate the new mean
                self.mean = self.__calcMean(x)
                # calculate the new variance
                self.variance = self.__calcVariance(x)
                # calculate the eccentricity and normalized eccentricity
                eccentricity = self.__calcEccentricity(x)
                norm_eccentricity = eccentricity/2
                # define the threshold for outlier detection
                threshold_ = (self.threshold**2 +1)/(2*self.k)
                
                # check if the point is an outlier
                isOutlier = norm_eccentricity > threshold_

                # if the point is an outlier, add it to the outlier list
                if (isOutlier):
                    df.at[index, 'is_outlier'] = 1

            # Update the timestamp
            self.k = self.k + 1
            

    def run(self, x):
        "Run the algorithm online"""

        is_outlier = 0
        
        # update the model metrics
        if(self.k == 1):
            self.mean = x
            self.variance = 0
            #is_outlier = 1
        else:
            # calculate the new mean
            self.mean = self.__calcMean(x)
            # calculate the new variance
            self.variance = self.__calcVariance(x)
            # calculate the eccentricity and nomalized eccentricity
            eccentricity = self.__calcEccentricity(x)
            norm_eccentricity = eccentricity/2
            # define the threshold for outlier detection
            threshold_ = (self.threshold**2 +1)/(2*self.k)
            
            # check if the point is an outlier
            isOutlier = norm_eccentricity > threshold_

            # if the sample is an outlier, add it to the outlier list
            if (isOutlier):
                is_outlier = 1

        # Update the timestamp
        self.k = self.k + 1

        return is_outlier