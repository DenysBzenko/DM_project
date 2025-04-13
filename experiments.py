import time
import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

def measure_planarity_time(vertices, density, representation='matrix', iterations=20):
    total_time = 0
    for _ in range(iterations):
        g = Graph.generate_random(vertices, density)
        if representation == 'list':
            g.matrix_to_list()
        
        start_time = time.perf_counter()
        g.is_planar()
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    
    return total_time / iterations

def print_statistics(results, vertices_sizes, densities, representations):
    print("\nСтатистика експерементів :")
    print("=" * 50)
    
    for density in densities:
        print(f"\nЩільність графа: {density}")
        print("-" * 30)
        
        for rep in representations:
            times = results[density][rep]
            print(f"\nПредставлення: {rep}")
            print(f"Мінімальний час: {min(times)*1000:.2f} мс")
            print(f"Максимальний час: {max(times)*1000:.2f} мс")
            print(f"Середній час: {np.mean(times)*1000:.2f} мс")
            print(f"Медіана часу: {np.median(times)*1000:.2f} мс")
            print(f"Стандартне відхилення: {np.std(times)*1000:.2f} мс")

def run_experiments():
    vertices_sizes = [i for i in range(30, 100, 10)]
    densities = [0.25, 0.3, 0.4, 0.5, 0.6]
    representations = ['matrix', 'list']

    total_experiments = len(vertices_sizes) * len(densities) * len(representations)
    current_experiment = 0
    
    results = {}
    print(f"\nПочаток експериментів. Всього буде проведено {total_experiments} тестів.\n")
    
    for density in densities:
        results[density] = {rep: [] for rep in representations}
        
        for size in vertices_sizes:
            for rep in representations:
                current_experiment += 1
                print(f"Експеримент {current_experiment}/{total_experiments}: "
                      f"розмір={size}, щільність={density}, представлення={rep}")
                
                time_taken = measure_planarity_time(size, density, rep)
                results[density][rep].append(time_taken)
    
    print("\nЕксперименти завершено. Формування результатів...\n")

    plt.figure(figsize=(12, 8))
    markers = ['o', 's']
    for density in densities:
        for i, rep in enumerate(representations):
            plt.plot(vertices_sizes, results[density][rep], 
                    marker=markers[i], 
                    label=f'Щільність={density}, {rep}')
    
    plt.xlabel('Кількість вершин')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Час перевірки планарності графа')
    plt.grid(True)
    plt.legend()
    plt.show()

    print("\nРезультати експериментів (час у секундах):")
    print("-" * 80)
    print("Розмір | ", end="")
    for density in densities:
        print(f"Щільність={density:<6} | ", end="")
    print()
    print("-" * 80)
    
    for i, size in enumerate(vertices_sizes):
        print(f"{size:<6} | ", end="")
        for density in densities:
            avg_time = (results[density]['matrix'][i] + results[density]['list'][i]) / 2
            print(f"{avg_time:<14.6f} | ", end="")
        print()

    print_statistics(results, vertices_sizes, densities, representations)
