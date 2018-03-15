import os
import random
import tempfile
import zipfile
import time
import concurrent.futures


def timer(f):
    def inner(*args, **kwargs):
        try:
            t0 = time.time()
            return f(*args, **kwargs)#调用相应函数
        finally:
            t1 = time.time()
            print(f.__name__, 'TOOK', t1 - t0)
    return inner


@timer
def f1(fn, dest):
    with open(fn, 'rb') as f:
        zf = zipfile.ZipFile(f)
        zf.extractall(dest)

    total = 0
    for root, dirs, files in os.walk(dest):
        for file_ in files:
            fn = os.path.join(root, file_)
            total += _count_file(fn)
    return total

def _count_file(fn):
    with open(fn, 'rb') as f:
        return _count_file_object(f)


def _count_file_object(f):
    total = 0
    for line in f:
        total += len(line)
    return total

@timer
def f2(fn, dest):

    def unzip_member(zf, member, dest):
        zf.extract(member, dest)
        fn = os.path.join(dest, member.filename)
        return _count_file(fn)

    with open(fn, 'rb') as f:
        zf = zipfile.ZipFile(f)
        futures = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for member in zf.infolist():
                futures.append(
                    executor.submit(
                        unzip_member,
                        zf,
                        member,
                        dest,
                    )
                )
            total = 0
            for future in concurrent.futures.as_completed(futures):
                total += future.result()
    return total


def unzip_member_f3(zip_filepath, filename, dest):
    with open(zip_filepath, 'rb') as f:
        zf = zipfile.ZipFile(f)
        zf.extract(filename, dest)
    fn = os.path.join(dest, filename)
    return _count_file(fn)


@timer
def f3(fn, dest):
    with open(fn, 'rb') as f:
        zf = zipfile.ZipFile(f)
        futures = []
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for member in zf.infolist():
                futures.append(
                    executor.submit(
                        unzip_member_f3,
                        fn,
                        member.filename,
                        dest,
                    )
                )
            total = 0
            for future in concurrent.futures.as_completed(futures):
                total += future.result()
    return total


def run(fn):
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f1(fn, tmpdir))
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f2(fn, tmpdir))
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f3(fn, tmpdir))


if __name__ == '__main__':
    run('C:\\\\Users\\Administrator\\Desktop\\ZIP\\test.zip')
