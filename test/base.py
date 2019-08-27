"""
Python implementation of the algorithms.
"""

import numpy as np

class BaseFoo(object):
    """Base class."""

    def __init__(self, random_state=None):
        """Construct a BaseFoo model.

        Parameters
        ----------
        random_state : int, optional (default=None)
            random_state is the seed used by the random number generator.
        """
        self._random_state = random_state
        self._result = None

    def fit(self, X):
        """Subclasses should implement this method!
        Fit the model to X.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data, where n_samples is the number of samples
            and n_features is the number of features.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
        return self

    @property
    def result_(self):
        """Estimated result.

        Returns
        -------
        result_ : array-like, shape (n_features)
            The estimated result.
        """
        return self._result
