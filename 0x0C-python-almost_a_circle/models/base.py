#!/usr/bin/python3
"""Base class Module"""
import json
import csv
import os.path



class Base:
    """base of OOP hierarchy"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        fname = cls.__name__ + ".json"
        list_elem = []

        if list_objs:
            for i in range(len(list_objs)):
                list_elem.append(list_objs[i].to_dictionary())

        lst = cls.to_json_string(list_elem)

        with open(fname, 'w', encoding='utf-8') as file:
            file.write(lst)

    @staticmethod
    def from_json_string(json_string):
        """return list of json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            nw = cls(1, 1)
        else:
            nw = cls(1)

        nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        """returns list of inst"""
        fname = "{}.json".format(cls.__name__)

        if os.path.exists(fname) is False:
            return []

        with open(fname, 'r') as file:
            lst = file.read()

        cls_lst = cls.from_json_string(lst)
        ins_lst = []

        for i in range(len(cls_lst)):
            ins_lst.append(cls.create(**cls_lst[i]))

        return ins_lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method for saving a csv file"""
        fname = "{}.csv".format(cls.__name__)
        
        if cls.__name__ == "Rectangle":
            lst_dct = [0, 0, 0, 0, 0]
            lst_ky = ['id', 'width', 'height', 'x', 'y']
        else:
            lst_dct = ['0', '0', '0', '0']
            lst_ky = ['id', 'size', 'x', 'y']

        lsts = []

        if not list_objs:
            pass
        else:
            for elem in list_objs:
                for i in range(len(lst_ky)):
                    lst_dct[i] = elem.to_dictionary()[lst_ky[i]]
                lsts.append(lst_dct[:])

        with open(fname, 'w') as wf:
            tol = csv.writer(wf)
            tol.writerows(lsts)

    @classmethod
    def load_from_file_csv(cls):
        """method to load a csv file"""
        fname = "{}.csv".format(cls.__name__)

        if not os.path.exists(fname):
            return []

        with open(fname, 'r') as rd:
            tol1 = csv.reader(rd)
            lst_csv = list(tol1)

        if cls.__name__ == "Rectangle":
            lst_ky = ['id', 'width', 'height', 'x', 'y']
        else:
            lst_ky = ['id', 'size', 'x', 'y']

        lsts = []

        for csv_elem in lst_csv:
            csv_dct = {}
            for i in enumerate(csv_elem):
                csv_dct[lst_ky[i[0]]] = int(i[1])
            lsts.append(csv_dct)

        ins = []

        for n in range(len(lsts)):
            ins.append(cls.create(**lsts[n]))

        return ins
