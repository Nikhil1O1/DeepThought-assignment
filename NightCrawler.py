import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project '+ directory)
        os.mkdir(directory)

#storing queue for tracking upcoming pages
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    #if the directory is non existent, then first we make the dir
    if not os.path.isdir(project_name):
        os.mkdir(project_name)
    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')

#creating a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close

##create_data_files('google','https://google.com/')

#add data onto existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#delete file content
def delete_file_contents(path):
    with open(path, 'w'):
        pass

#read file and convert to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


#iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
