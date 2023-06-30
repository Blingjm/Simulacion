import random

def monteCarloIntegral(f, a, b, n):
  # Calcula la Integral

  total = 0
  for i in range(n):
    
    x = a + (b - a) * random.random()

    total += f(x)

  return total / n

def main():
  def f(x):
    return 3 * x ** 2 - 2 * x

  a = 2
  b = 3

  n = int(input("Ingrese el numero de simulaciones: "))


  mathResult = (b - a) * (3 * a ** 2 - 2 * a) / 2

  #Aproximado usando Metodo de MonteCarlo
  integral = monteCarloIntegral(f, a, b, n)

  # Calculo del porcentaje de error
  error = abs(mathResult - integral) / mathResult * 100

  # Impresion de resultados.
  print("Resultado matematico de la Integral:", mathResult)
  print("Resultado aproximado usando metodo de montecarlo:", integral)
  print("Porcentaje de error:", error, "%")

if __name__ == "__main__":
  main()