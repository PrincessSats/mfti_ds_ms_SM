import numpy as np


class LossAndDerivatives:
    @staticmethod
    def mse(X, Y, w):
        """
        X : numpy array of shape (`n_observations`, `n_features`)
        Y : numpy array of shape (`n_observations`, `target_dimentionality`) or (`n_observations`,)
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return : float
            single number with MSE value of linear model (X.dot(w)) with no bias term
            on the selected dataset.

        Comment: If Y is two-dimentional, average the error over both dimentions.
        """

        return np.mean((X.dot(w) - Y) ** 2)

    @staticmethod
    def mae(X, Y, w):
        """
        X : numpy array of shape (`n_observations`, `n_features`)
        Y : numpy array of shape (`n_observations`, `target_dimentionality`) or (`n_observations`,)
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return: float
            single number with MAE value of linear model (X.dot(w)) with no bias term
            on the selected dataset.

        Comment: If Y is two-dimentional, average the error over both dimentions.
        """
      # Преобразуем все входные данные в массивы NumPy
        X = np.array(X)
        Y = np.array(Y)
        w = np.array(w)

        # Если Y или w одномерные, то приводим их к (n, 1) для единообразия
        if Y.ndim == 1:
            Y = Y.reshape(-1, 1)
        if w.ndim == 1:
            w = w.reshape(-1, 1)

        # Предсказания модели: y_pred = X.dot(w)
        y_pred = X.dot(w)

        # MAE = среднее от абсолютных ошибок (разность предсказания и истинного значения)
        mae_value = np.mean(np.abs(y_pred - Y))
        return mae_value

    @staticmethod
    def l2_reg(w):
        """
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return: float
            single number with sum of squared elements of the weight matrix ( \sum_{ij} w_{ij}^2 )

        Computes the L2 regularization term for the weight matrix w.
        """

        w = np.array(w)  # на случай, если w не NumPy-массив
        return np.sum(w ** 2)

    @staticmethod
    def l1_reg(w):
        """
        w : numpy array of shape (`n_features`, `target_dimentionality`)

        Return : float
            single number with sum of the absolute values of the weight matrix ( \sum_{ij} |w_{ij}| )

        Computes the L1 regularization term for the weight matrix w.
        """

        w = np.array(w)  # на случай, если w не NumPy-массив
        return np.sum(np.abs(w))

    @staticmethod
    def no_reg(w):
        """
        Simply ignores the regularization
        """
        return 0.0

    @staticmethod
    def mse_derivative(X, Y, w):
        """
        X : numpy array of shape (`n_observations`, `n_features`)
        Y : numpy array of shape (`n_observations`, `target_dimentionality`) or (`n_observations`,)
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return : numpy array of same shape as `w`

        Computes the MSE derivative for linear regression (X.dot(w)) with no bias term
        w.r.t. w weight matrix.

        Please mention, that in case `target_dimentionality` > 1 the error is averaged along this
        dimension as well, so you need to consider that fact in derivative implementation.
        """

        # Преобразуем входные данные в массивы
        X = np.asarray(X)
        Y = np.asarray(Y)
        w = np.asarray(w)
        
        # Если Y или w одномерные, приводим их к двумерному виду для удобства расчетов
        #  (n_observations, 1), (n_features, 1)
        was_1d = False
        if Y.ndim == 1:
            Y = Y.reshape(-1, 1)
            was_1d = True
        if w.ndim == 1:
            w = w.reshape(-1, 1)
            was_1d = True

        # Предсказание: y_pred = X.dot(w)  -> (n_observations, target_dim)
        y_pred = X.dot(w)
        residual = y_pred - Y

        # Число объектов и размер выходной размерности
        n_obs, t_dim = residual.shape

        # Формула для MSE:
        # MSE = 1/(n_obs * t_dim) * sum( (Xw - Y)^2 )
        # dMSE/dw = (2 / (n_obs * t_dim)) * X^T * (Xw - Y)
        grad = (2.0 / (n_obs * t_dim)) * X.T.dot(residual)

        # Если исходный w был одномерный, возвращаем градиент в таком же формате
        if was_1d:
            grad = grad.ravel()

        return grad

    @staticmethod
    def mae_derivative(X, Y, w):
        """
        X : numpy array of shape (`n_observations`, `n_features`)
        Y : numpy array of shape (`n_observations`, `target_dimentionality`) or (`n_observations`,)
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return : numpy array of same shape as `w`

        Computes the MAE derivative for linear regression (X.dot(w)) with no bias term
        w.r.t. w weight matrix.

        Please mention, that in case `target_dimentionality` > 1 the error is averaged along this
        dimension as well, so you need to consider that fact in derivative implementation.
        """

        X = np.asarray(X)
        Y = np.asarray(Y)
        w = np.asarray(w)
        
        # Запоминаем, был ли изначально одномерный w и/или Y
        # чтобы вернуть градиент в таком же формате
        was_1d = False
        if Y.ndim == 1:
            Y = Y.reshape(-1, 1)  # (n_observations, 1)
            was_1d = True
        if w.ndim == 1:
            w = w.reshape(-1, 1)  # (n_features, 1)
            was_1d = True

        # Предсказания модели y_pred = X.dot(w)
        # Форма (n_observations, target_dim)
        y_pred = X.dot(w)
        residual = y_pred - Y
        n_obs, t_dim = residual.shape

        # sign(residual) имеет ту же форму (n_observations, target_dim)
        sign_matrix = np.sign(residual)
        
        # Формула для производной MAE:
        #   MAE = 1/(n_obs * t_dim) * sum( |Xw - Y| )
        #   dMAE/dw = (1/(n_obs * t_dim)) * X^T dot sign(Xw - Y)
        grad = (1.0 / (n_obs * t_dim)) * X.T.dot(sign_matrix)

        # Если изначально w был одномерным, 
        # приводим градиент обратно к одномерному виду
        if was_1d:
            grad = grad.ravel()

        return grad

    @staticmethod
    def l2_reg_derivative(w):
        """
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return : numpy array of same shape as `w`

        Computes the L2 regularization term derivative w.r.t. the weight matrix w.
        """

        w = np.array(w, copy=False)  # ensure it's a NumPy array
        return 2.0 * w

    @staticmethod
    def l1_reg_derivative(w):
        """
        Y : numpy array of shape (`n_observations`, `target_dimentionality`) or (`n_observations`,)
        w : numpy array of shape (`n_features`, `target_dimentionality`) or (`n_features`,)

        Return : numpy array of same shape as `w`

        Computes the L1 regularization term derivative w.r.t. the weight matrix w.
        """

        w = np.array(w, copy=False)
        return np.sign(w)

    @staticmethod
    def no_reg_derivative(w):
        """
        Simply ignores the derivative
        """
        return np.zeros_like(w)