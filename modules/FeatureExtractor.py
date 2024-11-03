import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

class FeatureExtractor:
    def __init__(self, df, target_col):
        self.df = df.copy()
        self.target_col = target_col
        
    def create_lag_features(self, lags=[1, 3, 7, 28]):
        """Create lag features"""
        for lag in lags:
            self.df[f'lag_{lag}'] = self.df[self.target_col].shift(lag)
        return self
    
    def create_rolling_features(self, windows=[1, 3, 7, 28]):
        """Create rolling statistics features"""
        for win in windows:
            self.df[f'rolling_mean_{win}'] = self.df[self.target_col].rolling(window=win).mean()
            self.df[f'rolling_std_{win}'] = self.df[self.target_col].rolling(window=win).std()
        return self
    
    def create_expanding_features(self):
        """Create expanding window statistics"""
        self.df['expanding_mean'] = self.df[self.target_col].expanding().mean()
        self.df['expanding_std'] = self.df[self.target_col].expanding().std()
        self.df['expanding_max'] = self.df[self.target_col].expanding().max()
        self.df['expanding_min'] = self.df[self.target_col].expanding().min()
        self.df['expanding_sum'] = self.df[self.target_col].expanding().sum()
        self.df['expanding_median'] = self.df[self.target_col].expanding().median()
        self.df['expanding_skew'] = self.df[self.target_col].expanding().skew()
        self.df['expanding_kurt'] = self.df[self.target_col].expanding().kurt()
        self.df['expanding_quantile_25'] = self.df[self.target_col].expanding().quantile(0.25)
        self.df['expanding_quantile_75'] = self.df[self.target_col].expanding().quantile(0.75)
        return self
    
    def create_date_features(self):
        """Create date-based features"""
        self.df['day'] = self.df.index.day
        self.df['month'] = self.df.index.month
        self.df['quarter'] = self.df.index.quarter
        self.df['year'] = self.df.index.year
        self.df['dayofweek'] = self.df.index.dayofweek
        self.df['dayofyear'] = self.df.index.dayofyear
        self.df['weekofyear'] = self.df.index.isocalendar().week
        self.df['is_month_start'] = self.df.index.is_month_start
        self.df['is_month_end'] = self.df.index.is_month_end
        self.df['season'] = self.df['month'].apply(self._determine_season)
        self.df['is_weekend'] = self.df['dayofweek'].apply(lambda x: 1 if x in [5, 6] else 0)
        self.df['is_weekday'] = self.df['dayofweek'].apply(lambda x: 1 if x not in [5, 6] else 0)
        return self
    
    def create_cyclical_features(self):
        """Create cyclical features"""
        self.df['day_sin'] = np.sin(2 * np.pi * self.df['day']/31)
        self.df['day_cos'] = np.cos(2 * np.pi * self.df['day']/31)
        self.df['month_sin'] = np.sin(2 * np.pi * self.df['month']/12)
        self.df['month_cos'] = np.cos(2 * np.pi * self.df['month']/12)
        self.df['quarter_sin'] = np.sin(2 * np.pi * self.df['quarter']/4)
        self.df['quarter_cos'] = np.cos(2 * np.pi * self.df['quarter']/4)
        self.df['season_sin'] = np.sin(2 * np.pi * self.df['season']/2)
        self.df['season_cos'] = np.cos(2 * np.pi * self.df['season']/2)
        self.df['dayofweek_sin'] = np.sin(2 * np.pi * self.df['dayofweek']/6)
        self.df['dayofweek_cos'] = np.cos(2 * np.pi * self.df['dayofweek']/6)
        self.df['weekofyear_sin'] = np.sin(2 * np.pi * self.df['weekofyear']/52)
        self.df['weekofyear_cos'] = np.cos(2 * np.pi * self.df['weekofyear']/52)
        self.df['dayofyear_sin'] = np.sin(2 * np.pi * self.df['dayofyear']/366)
        self.df['dayofyear_cos'] = np.cos(2 * np.pi * self.df['dayofyear']/366)
        return self
    
    def create_decomposition_features(self, period=30):
        """Create decomposition features"""
        result = seasonal_decompose(self.df[self.target_col], model='additive', period=period)
        self.df['trend'] = result.trend
        self.df['seasonal'] = result.seasonal
        self.df['residual'] = result.resid
        return self
    
    def _determine_season(self, month):
        """Helper method to determine season"""
        if month in [11, 12, 1, 2, 3]:
            return 0
        elif month in [4, 5, 6, 7, 8, 9, 10]:
            return 1
    
    def fill_missing_values(self):
        """Fill missing values"""
        self.df['trend'].fillna(self.df['trend'].median(), inplace=True)
        self.df['residual'].fillna(self.df['residual'].mean(), inplace=True)
        self.df.fillna(0, inplace=True)
        return self
    
    def get_features(self):
        """Return the dataframe with all features"""
        return self.df