__author__ = 'Abraham Yusuf <yabraham@swglobal.com>'

import re
import functools


def remove_duplicates(lst):
    def reducer(accumulator, item):
        if item not in accumulator:
            accumulator.append(item)

        return accumulator

    return functools.reduce(reducer, lst, [])


def clean(lst):
    pattern = re.compile('^(\+?)\d{10,15}$')

    return [i.strip() for i in lst if pattern.match(i.strip())]


class Task(object):
    _mobile_numbers_str = ''

    @property
    def mobile_numbers(self):
        mobile_numbers = []
        for mobile_no in [i.strip() for i in self._mobile_numbers_str.split(',')]:
            mobile_numbers.append(mobile_no)
            if not mobile_no.startswith('0'):
                mobile_numbers.append('0%s' % mobile_no)
                mobile_numbers.append('234%s' % mobile_no)
                mobile_numbers.append('+234%s' % mobile_no)
            else:
                mobile_numbers.append(mobile_no[1:])
                mobile_numbers.append('234%s' % mobile_no[1:])
                mobile_numbers.append('+234%s' % mobile_no[1:])

        return remove_duplicates(clean(mobile_numbers))


class FindInFolder(Task):
    def __init__(self, mobile_nos, folders):
        self._mobile_numbers_str = mobile_nos
        self._folders = folders

    @property
    def folders(self):
        _folders = self._folders
        tmp = [folder.strip() for folder in _folders.split(',')] if isinstance(_folders, str) else _folders

        return remove_duplicates(tmp)


class FindInDb(Task):
    def __init__(self, mobile_nos):
        self._mobile_numbers_str = mobile_nos