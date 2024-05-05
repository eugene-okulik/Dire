import os
import argparse


def compare_data(file_path, text):
    results = []

    with open(file_path, 'r', encoding='utf-8', newline='') as data_file:
        lines = data_file.readlines()

    for i, line in enumerate(lines):
        pos = line.find(text)

        if pos != -1:
            before = line[:pos].split()[-5:]
            after = line[pos + len(text):].split()[:5]
            context = ' '.join(before + [text] + after)

            results.append((file_path, i + 1, context))
    return results


def find_files_in_directory(path, text):
    all_results = []

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            results = compare_data(file_path, text)
            all_results.extend(results)
    return all_results


def receiving_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path for search")
    parser.add_argument("--text", help="text for search", required=True)
    args = parser.parse_args()

    all_results = find_files_in_directory(args.path, args.text)

    for file_path, line_num, context in all_results:
        print(f"Найдено в файле {file_path}, строка {line_num}: {context} ")


receiving_data()

# path = r'D:\IT\QA\Okulik\Cource\Dire\homework\eugene_okulik\data\logs'
