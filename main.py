from typing import List, Tuple, Optional
import random

class MatrixManager:
    """Класс для управления матрицей и поиска седловых точек"""
    
    def __init__(self):
        self.matrix: List[List[int]] = []
        self.saddle_points: List[Tuple[int, int, int]] = []
        self.has_result = False
    
    def input_matrix_manually(self) -> None:
        """Ввод матрицы вручную"""
        print("\n" + "="*50)
        print("РУЧНОЙ ВВОД МАТРИЦЫ")
        print("="*50)
        
        try:
            n = int(input("Введите количество строк (N): "))
            m = int(input("Введите количество столбцов (M): "))
            
            if n <= 0 or m <= 0:
                print("Ошибка: размеры должны быть положительными!")
                return
            
            self.matrix = []
            print(f"\nВведите элементы матрицы {n}x{m}:")
            print("Пример: 1 2 3 4 5")
            
            for i in range(n):
                while True:
                    row_input = input(f"Строка {i+1}: ").strip()
                    numbers = row_input.split()
                    
                    if len(numbers) != m:
                        print(f"Ошибка: нужно ввести ровно {m} чисел!")
                        print(f"Вы ввели {len(numbers)} чисел. Попробуйте снова.")
                        continue
                    
                    try:
                        row = [int(num) for num in numbers]
                        self.matrix.append(row)
                        break
                    except ValueError:
                        print("Ошибка: введите целые числа!")
            
            self._reset_results()
            print(f"\n✓ Матрица {n}x{m} успешно введена!")
            
        except ValueError:
            print("Ошибка: введите корректные числа!")
        except KeyboardInterrupt:
            print("\n✗ Ввод прерван")
    
    def generate_random_matrix(self, n: int = 5, m: int = 5, min_val: int = -100, max_val: int = 100) -> None:
        """Генерация случайной матрицы"""
        if n <= 0 or m <= 0:
            print("Ошибка: размеры должны быть положительными!")
            return
        
        self.matrix = []
        for i in range(n):
            row = [random.randint(min_val, max_val) for _ in range(m)]
            self.matrix.append(row)
        
        self._reset_results()
        print(f"\n✓ Сгенерирована случайная матрица {n}x{m}")
        print(f"  Диапазон значений: от {min_val} до {max_val}")
    
    def _reset_results(self) -> None:
        """Сброс результатов вычислений"""
        self.saddle_points.clear()
        self.has_result = False
    
    def _get_column(self, col_idx: int) -> List[int]:
        """Получить столбец по индексу"""
        return [row[col_idx] for row in self.matrix]
    
    def find_saddle_points(self) -> bool:
        """Поиск седловых точек (алгоритм)"""
        if not self.matrix:
            print("Ошибка: матрица не введена!")
            return False
        
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        print(f"\nПоиск седловых точек в матрице {n}x{m}...")
        
        # Очищаем предыдущие результаты
        self.saddle_points.clear()
        
        # Находим минимумы в каждой строке
        row_minimums = []
        for i in range(n):
            row_min = min(self.matrix[i])
            row_minimums.append(row_min)
        
        # Находим максимумы в каждом столбце
        col_maximums = []
        for j in range(m):
            column = self._get_column(j)
            col_max = max(column)
            col_maximums.append(col_max)
        
        # Ищем седловые точки
        for i in range(n):
            for j in range(m):
                element = self.matrix[i][j]
                # Проверяем, является ли элемент минимумом в строке и максимумом в столбце
                if element == row_minimums[i] and element == col_maximums[j]:
                    self.saddle_points.append((i, j, element))
        
        self.has_result = True
        
        print("✓ Поиск завершен!")
        print(f"  Найдено седловых точек: {len(self.saddle_points)}")
        return True
    
    def show_matrix(self) -> None:
        """Показать матрицу"""
        if not self.matrix:
            print("✗ Матрица не введена!")
            return
        
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        print(f"\n" + "="*50)
        print(f"МАТРИЦА {n}x{m}")
        print("="*50)
        
        # Определяем ширину для выравнивания
        max_val = max(max(row) for row in self.matrix)
        min_val = min(min(row) for row in self.matrix)
        max_width = max(len(str(max_val)), len(str(min_val))) + 2
        
        # Выводим индексы столбцов
        col_indices = "       "
        for j in range(m):
            col_indices += f"   {j+1:{max_width}}"
        print(col_indices)
        print("       " + "---" + "-" * (m * (max_width + 1)))
        
        # Выводим строки матрицы
        for i, row in enumerate(self.matrix):
            row_str = f"Строка {i+1:2} |"
            for val in row:
                row_str += f" {val:{max_width}}"
            print(row_str)
        
        print("="*50)
    
    def show_results(self) -> None:
        """Показать результаты"""
        if not self.matrix:
            print("✗ Матрица не введена!")
            return
        
        if not self.has_result:
            print("✗ Сначала выполните поиск седловых точек!")
            return
        
        print("\n" + "="*50)
        print("РЕЗУЛЬТАТЫ ПОИСКА СЕДЛОВЫХ ТОЧЕК")
        print("="*50)
        
        if not self.saddle_points:
            print("\n✗ Седловых точек не найдено!")
            print("\nПояснение:")
            print("Седловая точка - это элемент матрицы, который одновременно:")
            print("1. Является минимальным в своей строке")
            print("2. Является максимальным в своем столбце")
        else:
            print(f"\n✓ Найдено {len(self.saddle_points)} седловых точек:")
            for idx, (row, col, value) in enumerate(self.saddle_points, 1):
                print(f"\n{idx}. Элемент M[{row+1},{col+1}] = {value}")
                print(f"   - Минимум в строке {row+1}")
                print(f"   - Максимум в столбце {col+1}")
        
        print("\n" + "="*50)
    
    def clear_matrix(self) -> None:
        """Очистить матрицу"""
        confirm = input("\nВы уверены? Все данные будут удалены! (y/n): ").strip().lower()
        if confirm == 'y':
            self.matrix.clear()
            self.saddle_points.clear()
            self.has_result = False
            print("✓ Матрица очищена!")
        else:
            print("✗ Операция отменена")


def show_menu() -> None:
    """Показать меню программы"""
    print("\n" + "="*50)
    print("ПОИСК СЕДЛОВЫХ ТОЧЕК В МАТРИЦЕ")
    print("="*50)
    print("\nГЛАВНОЕ МЕНЮ:")
    print("1. Ввести матрицу вручную")
    print("2. Сгенерировать случайную матрицу")
    print("3. Показать матрицу")
    print("4. Найти седловые точки")
    print("5. Показать результаты")
    print("6. Очистить матрицу")
    print("0. Выход из программы")
    print("-"*50)


def main() -> None:
    """Главная функция программы"""
    manager = MatrixManager()
    
    print("Добро пожаловать в программу поиска седловых точек!")
    print("Седловая точка - элемент, который является")
    print("минимумом в своей строке и максимумом в своем столбце.")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nВыберите действие (0-6): ").strip()
            
            if choice == '0':
                print("\n" + "="*50)
                print("Спасибо за использование программы! До свидания!")
                print("="*50)
                break
            
            elif choice == '1':
                manager.input_matrix_manually()
            
            elif choice == '2':
                try:
                    n = int(input("Количество строк (N): ") or "5")
                    m = int(input("Количество столбцов (M): ") or "5")
                    min_val = int(input("Минимальное значение: ") or "-100")
                    max_val = int(input("Максимальное значение: ") or "100")
                    
                    manager.generate_random_matrix(n, m, min_val, max_val)
                except ValueError:
                    print("✗ Ошибка: введите целые числа!")
            
            elif choice == '3':
                manager.show_matrix()
            
            elif choice == '4':
                if not manager.matrix:
                    print("✗ Ошибка: сначала введите матрицу!")
                else:
                    manager.find_saddle_points()
            
            elif choice == '5':
                manager.show_results()
            
            elif choice == '6':
                manager.clear_matrix()
            
            else:
                print("✗ Неверный выбор! Попробуйте снова.")
            
            # Пауза для удобства чтения
            if choice not in ['0', '3', '5']:
                input("\nНажмите Enter для продолжения...")
        
        except KeyboardInterrupt:
            print("\n\n✗ Программа прервана пользователем")
            break
        except Exception as e:
            print(f"✗ Произошла ошибка: {e}")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()