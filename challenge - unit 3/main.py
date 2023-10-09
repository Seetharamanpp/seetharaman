def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = [
    "BMW", "KAWASAKI", "DUCATI", "BENELLI", "HAYABUSA", "HARLEY-DAVIDSON",
    "BENELLI", "BMW", "BMW"
]
target = "BMW"
result = linearSearchProduct(products, target)
print(result)