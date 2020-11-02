"""Get MD5, SHA256, and file information for future file integrity checks."""

from hashlib import md5, sha256
from os import path
from time import gmtime, strftime


def get_file_hash(file_with_path: str, a_hashtype: str) -> str:
    """ Returns hash string on the file specified using the hashtype."""
    hashtype_dict = {'md5': md5(), 'sha256': sha256()}
    this_hash = hashtype_dict[a_hashtype.lower()]
    with open(file_with_path, 'rb') as a_file:
        content = a_file.read()
        this_hash.update(content)
    return this_hash.hexdigest().upper()


def get_file_size(file_with_path: str) -> str:
    """ Returns the size and modified date of a file."""
    return path.getsize(file_with_path)


def get_file_modification_date(file_with_path: str) -> str:
    """ Returns the modified date of a file."""
    return strftime('%m/%d/%Y', gmtime(path.getmtime(file_with_path)))


def get_file_info(file_with_path) -> tuple:
    """ Returns a tuple of file information"""
    return (get_file_modification_date(file_with_path),
            get_file_size(file_with_path),
            file_with_path)


def main():
    userpath = input('Path to file to hash: ')
    userfile = input('Name of file to hash: ')
    checksumfile = 'checksums_' + path.splitext(userfile)[0] + '.txt'
    with open(checksumfile, 'w') as a_file:
        a_file.write('%s\t%s\t%s\n' % get_file_info(userpath + userfile))
        a_file.write('MD5\t %s \n' % get_file_hash(userpath + userfile, 'md5'))
        a_file.write('SHA256\t %s \n' %
                     get_file_hash(userpath + userfile, 'sha256'))


if __name__ == "__main__":
    main()
