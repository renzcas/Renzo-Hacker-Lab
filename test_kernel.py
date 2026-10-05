from big_animal.big_animal_kernel import BigAnimalKernel


kernel = BigAnimalKernel()

# Minimal empty snapshot
snapshot = {}

result = kernel.tick(snapshot)

print("WORLD:")
print(result["world"])

print("\nMINDWAVES:")
print(result["mind"])
