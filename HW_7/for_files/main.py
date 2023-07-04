from for_files import create_file, delete_file, copy_file, move_file

create_file('test.txt')
copy_file('test.txt', 'backup.txt')
move_file('test.txt', 'new_location/test.txt')
delete_file('test.txt')