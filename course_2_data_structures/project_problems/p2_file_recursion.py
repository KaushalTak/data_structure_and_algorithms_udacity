import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    try:
        all_files = os.listdir(path)
        files = []
        for file in all_files:
            if os.path.isdir(os.path.join(path, file)):
                files.extend(find_files(suffix, os.path.join(path, file)))
            else:
                if file.endswith(suffix):
                    files.append(os.path.join(path, file))
        return files
    except FileNotFoundError:
        print('Path Incorrect, No such directory present!')


def test():
    # test1
    print(
        "test 1, output should be ['./testdir1/subdir1/a.c', './testdir1/subdir3/subsubdir1/b.c', './testdir1/subdir5/a.c', './testdir1/t1.c']")
    print(find_files('.c', '.'))
    print("\n----------------------------------------------------")

    # test2
    print("test 2, output should be []")
    print(find_files('.c', './testdir2'))
    print("\n----------------------------------------------------")

    # test3
    print("test 3, output should be 'Path Incorrect, No such directory present!' and None")
    print(find_files('.c', './testdir3'))


if __name__ == '__main__':
    test()
