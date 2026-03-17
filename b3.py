import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

vale = yf.download('VALE3.SA',
                   start='2022-01-01',
                   end='2022-01-08',
                   auto_adjust=True)
print(vale.head())

vale['retorno'] = vale['Close'].pct_change()
vale['Close'].plot(figsize=(10,5))
plt.title('Preço da ação da Vale')
plt.show()

vale = vale.dropna()


vale['Close'] = vale['Close'].astype(float)
vale['retorno'] = vale['retorno'].astype(float)


retorno_medio = float(vale['retorno'].mean())
preco_atual = float(vale['Close'].iloc[-1].item())


dias = 5
preco_justo = preco_atual * (1 + retorno_medio) ** dias

print("Preço atual:", round(preco_atual, 2))
print("Retorno médio:", round(retorno_medio, 4))
print("Preço justo:", round(preco_justo, 2))

plt.figure(figsize=(10,5))
plt.plot(vale.index, vale['Close'])


plt.axhline(preco_atual, linestyle='--')


plt.axhline(preco_justo, linestyle='--')

plt.title('Preço da VALE3 vs Valuation')
plt.xlabel('Data')
plt.ylabel('Preço (R$)')
plt.grid()

plt.show()


vale.reset_index(inplace=True)
vale['preco_justo'] = preco_justo


vale.to_csv('vale_valuation.csv', index=False)

