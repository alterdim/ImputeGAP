import time
import numpy as np

def sssd(incomp_data, logs=True, verbose=True):
    """Impute NaN values with the mean value of the time series.
    
        Parameters
        ----------
        incomp_data : numpy.ndarray
            The input time series with contamination (missing values represented as NaNs).
        params : dict, optional
            Optional parameters for the algorithm. If None, the minimum value from the contamination is used (default is None).
    
        Returns
        -------
        numpy.ndarray
            The imputed matrix where NaN values have been replaced with the mean value from the time series."""
    
    start_time = time.time()  # Record start time
    mean_value = np.nanmean(incomp_data)
    recov_data = np.nan_to_num(incomp_data, nan=mean_value)
    end_time = time.time()

    if logs and verbose:
        print(f"\n> logs: imputation sssd - Execution Time: {(end_time - start_time):.4f} seconds\n")

    return recov_data