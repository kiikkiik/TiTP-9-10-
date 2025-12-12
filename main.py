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
            
            for i in range(n):
                while True:
                    row_input = input(f"Строка {i+1} (через пробел, {m} чисел): ").strip()
                    numbers = row_input.split()
                    
                    if len(numbers) != m:
                        print(f"Ошибка: нужно ввести ровно {m} чисел!")
                        continue
                    
                    try:
                        row = [int(num) for num in numbers]
                        self.matrix.append(row)
                        break
                    except ValueError:
                        print("Ошибка: введите целые числа!")
            
            self._reset_results()
            print(f"\nМатрица {n}x{m} успешно введена!")
            
        except ValueError:
            print("Ошибка: введите корректные числа!")
        except KeyboardInterrupt:
            print("\nВвод прерван")
    
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
        print(f"\nСгенерирована случайная матрица {n}x{m}")
        print(f"Диапазон значений: от {min_val} до {max_val}")
    
    def _reset_results(self) -> None:
        """Сброс результатов вычислений"""
        self.saddle_points.clear()
        self.has_result = False
        print("Результаты вычислений сброшены")
    
    def _get_column(self, col_idx: int) -> List[int]:
        """Получить столбец по индексу"""
        return [row[col_idx] for row in self.matrix]
    
    def find_saddle_points(self) -> bool:
        """Поиск седловых точек"""
        if not self.matrix:
            print("Ошибка: матрица не введена!")
            return False
        
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        print(f"\nПоиск седловых точек в матрице {n}x{m}...")
        
        # Заглушка для алгоритма
        self.saddle_points = [(-1, -1, 0)]  # Временная заглушка
        self.has_result = True
        
        print("Поиск завершен!")
        return True
    
    def show_matrix(self) -> None:
        """Показать матрицу"""
        if not self.matrix:
            print("Матрица не введена!")
            return
        
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        print(f"\n" + "="*50)
        print(f"МАТРИЦА {n}x{m}")
        print("="*50)
        
        for i, row in enumerate(self.matrix):
            row_str = " | ".join(f"{val:6}" for val in row)
            print(f"Строка {i+1:2}: [{row_str}]")
        
        print("="*50)
    
    def show_results(self) -> None:
        """Показать результаты"""
        if not self.has_result:
            print("Сначала выполните поиск седловых точек!")
            return
        
        print("\n" + "="*50)
        print("РЕЗУЛЬТАТЫ ПОИСКА СЕДЛОВЫХ ТОЧЕК")
        print("="*50)
        
        if not self.saddle_points or self.saddle_points[0] == (-1, -1, 0):
            print("\nСедловых точек не найдено!")
        else:
            print(f"\nНайдено {len(self.saddle_points)} седловых точек:")
            for idx, (row, col, value) in enumerate(self.saddle_points, 1):
                print(f"{idx}. Элемент [{row+1},{col+1}] = {value}")
        
        print("\n" + "="*50)
    
    def clear_matrix(self) -> None:
        """Очистить матрицу"""
        self.matrix.clear()
        self._reset_results()
        print("Матрица очищена!")


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
    
    while True:
        show_menu()
        
        try:
            choice = input("\nВыберите действие (0-6): ").strip()
            
            if choice == '0':
                print("\nСпасибо за использование программы! До свидания!")
                break
            
            elif choice == '1':
                manager.input_matrix_manually()
            
            elif choice == '2':
                try:
                    n = int(input("Количество строк (N): "))
                    m = int(input("Количество столбцов (M): "))
                    min_val = int(input("Минимальное значение: "))
                    max_val = int(input("Максимальное значение: "))
                    
                    manager.generate_random_matrix(n, m, min_val, max_val)
                except ValueError:
                    print("Ошибка: введите целые числа!")
            
            elif choice == '3':
                manager.show_matrix()
            
            elif choice == '4':
                manager.find_saddle_points()
            
            elif choice == '5':
                manager.show_results()
            
            elif choice == '6':
                confirm = input("Вы уверены? Матрица будет удалена! (y/n): ").strip().lower()
                if confirm == 'y':
                    manager.clear_matrix()
            
            else:
                print("Неверный выбор! Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()