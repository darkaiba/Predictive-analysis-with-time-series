import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from datetime import datetime

# Passo 1: Leitura do arquivo CSV
# Aqui você deve substituir o caminho do arquivo pelo caminho correto do seu arquivo CSV
df = pd.read_csv('dados_fakes.csv', parse_dates=True)
print(df.head())  # Exibe as primeiras linhas do dataframe

# Passo 2: Visualização dos dados
df.plot(figsize=(10,6))
plt.title('Série Temporal')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.show()

# Passo 3: Teste de estacionariedade (Teste de Dickey-Fuller)
result = adfuller(df['Valor'])  # Substitua 'valor' pela coluna de interesse
print(f'Estacionariedade: {result[1]}')
# Se o valor de p for menor que 0.05, podemos concluir que a série é estacionária

# Passo 4: Análise de Autocorrelação (ACF e PACF)
plot_acf(df['Valor'], lags=50)
plt.title('Autocorrelação')
plt.show()

plot_pacf(df['Valor'], lags=50)
plt.title('Autocorrelação Parcial')
plt.show()

# Passo 5: Modelagem ARIMA
# Aqui, você pode usar parâmetros que achou apropriados com base nas ACF e PACF.
# Vamos usar (p=1, d=1, q=1) como exemplo.
model = ARIMA(df['Valor'], order=(1, 1, 1))
model_fit = model.fit()

# Passo 6: Previsão
forecast = model_fit.forecast(steps=10)  # Prevendo os próximos 10 passos (ajuste conforme necessário)

# Passo 7: Visualização das previsões
plt.figure(figsize=(10,6))
plt.plot(df['Valor'], label='Dados históricos')
plt.plot(pd.date_range(df.index[-1], periods=11, freq='D')[1:], forecast, color='red', label='Previsões')
plt.legend()
plt.title('Previsão de Séries Temporais com ARIMA')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.show()

print('Previsões:', forecast)
