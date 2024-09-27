import multiprocessing
import zipfile
import time

def read_info(name):
    all_data = []
    try:
        with open(name, "r", encoding='utf-8') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {name} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {name}: {e}")

file_names = [f'./file{number}.txt' for number in range(1, 5)]

# start_time = time.time()
#
# for file_name in file_names:
#     read_info(file_name)
#
# end_time = time.time()
#
# final_time = end_time - start_time
# print(f"Время выполнения: {final_time:.2f} секунд.")

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    final_time = end_time - start_time
    print(f"Время выполнения: {final_time:.2f} секунд.")
