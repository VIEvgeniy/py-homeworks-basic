input_files = [{'name': '1.txt', 'str_count': 0}, {'name': '2.txt', 'str_count': 0}, {'name': '3.txt', 'str_count': 0}]
output_file_name = 'out.txt'

for input_file in input_files:
    with open(input_file['name']) as f:
        input_file['str_count'] = len(f.readlines())

input_files.sort(key=lambda k: k['str_count'])

with open(output_file_name, 'w') as output_file:
    for input_file in input_files:
        with open(input_file['name']) as f:
            output_file.write(f"{input_file['name']}\n")
            output_file.write(f'{input_file["str_count"]}\n')
            output_file.writelines(f.readlines())
            if input_file != input_files[-1]:
                output_file.write('\n')

