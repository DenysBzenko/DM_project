from graph import Graph
from visualizer import visualize_graph

def print_menu():
    print("\nМеню:")
    print("1. Показати матрицю суміжності")
    print("2. Показати списки суміжності")
    print("3. Додати вершину")
    print("4. Видалити вершину")
    print("5. Додати ребро")
    print("6. Видалити ребро")
    print("7. Показати характеристики графа")
    print("8. Візуалізувати граф")
    print("9. Конвертувати матрицю в списки суміжності")
    print("10. Конвертувати списки в матрицю суміжності")
    print("11. Згенерувати випадковий граф")
    print("12. Перевірити планарність графа")
    print("13. Провести експерименти")
    print("0. Вийти")

def main():
    g = Graph(5)
    
    while True:
        print_menu()
        choice = input("\nВиберіть опцію: ")
        
        if choice == "0":
            break
            
        elif choice == "1":
            print("\nМатриця суміжності:")
            print(g.adj_matrix)
            
        elif choice == "2":
            print("\nСписки суміжності:")
            for i in range(g.V):
                print(f"Вершина {i}: {g.adj_list[i]}")
            
        elif choice == "3":
            g.add_vertex()
            print(f"\nДодано нову вершину. Всього вершин: {g.V}")
            
        elif choice == "4":
            v = int(input("Введіть номер вершини для видалення: "))
            try:
                g.remove_vertex(v)
                print(f"Вершину {v} видалено")
            except ValueError as e:
                print(f"Помилка: {e}")
            
        elif choice == "5":
            u = int(input("Введіть першу вершину: "))
            v = int(input("Введіть другу вершину: "))
            try:
                g.add_edge(u, v)
                print(f"Додано ребро між вершинами {u} та {v}")
            except ValueError as e:
                print(f"Помилка: {e}")
            
        elif choice == "6":
            u = int(input("Введіть першу вершину: "))
            v = int(input("Введіть другу вершину: "))
            try:
                g.remove_edge(u, v)
                print(f"Видалено ребро між вершинами {u} та {v}")
            except ValueError as e:
                print(f"Помилка: {e}")
            
        elif choice == "7":
            print("\nХарактеристики графа:")
            print(f"Кількість вершин: {g.V}")
            print(f"Щільність графа: {g.density:.2f}")
            print(f"Степені вершин: {g.get_all_degrees()}")
            print(f"Максимальний степінь: {g.get_max_degree()}")
            print(f"Мінімальний степінь: {g.get_min_degree()}")
            print(f"Граф зв'язний: {g.is_connected()}")
            
        elif choice == "8":
            visualize_graph(g)
            
        elif choice == "9":
            g.matrix_to_list()
            print("Конвертовано матрицю суміжності в списки суміжності")
            
        elif choice == "10":
            g.list_to_matrix()
            print("Конвертовано списки суміжності в матрицю суміжності")
            
        elif choice == "11":
            vertices = int(input("Введіть кількість вершин: "))
            density = float(input("Введіть щільність графа (від 0 до 1): "))
            if 0 <= density <= 1 and vertices > 0:
                g = Graph.generate_random(vertices, density)
                print(f"Згенеровано випадковий граф з {vertices} вершинами та щільністю {density}")
            else:
                print("Помилка: некоректні параметри")
        
        elif choice == "12":
            is_planar = g.is_planar()
            print(f"\nГраф {'є' if is_planar else 'не є'} планарним")
            
        elif choice == "13":
            from experiments import run_experiments
            print("\nПроведення експериментів...")
            run_experiments()
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
