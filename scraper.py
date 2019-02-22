# from thenewboston tutorials on YouTube

import os

# Each website crawled is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project' + directory)
        os.makedirs(directory)

# Create queue and crawled files (if they haven't already been created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete from a file
def delete_file(path):
    with open(path, 'w'):
        pass

# Convert links on file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            # Trims the added new line
            results.add(line.replace('\n', ''))
    return results

# Convert from set to file
def set_to_file(set_name, file_name):
    delete_file(file_name)
    for link in sorted(set_name):
        append_to_file(file, link)
