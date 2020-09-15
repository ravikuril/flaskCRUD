class Base:
    base=0
    hight=0
    def __init__(self,passed_based,passed_hight):
        self.base=passed_based
        self.hight=passed_hight
    def print(self):
        print(self.base,self.hight)

class Triangle():
    triagngle_base=0
    triagngle_hight=0

    def __init__(self):
        self.__length=200
    def change_price(self,new_price):
        self.__length=new_price
    def get_price(self):
        return f"Current Price:{self.__length}"

    def value_exchange(self,Base:object):
        self.triagngle_base=Base.base+10
#
# base_obj=Base(passed_based=20,passed_hight=30)
# tri_obj=Triangle()
# tri_obj.value_exchange(base_obj)
# print(tri_obj.get_price())
# tri_obj.change_price(300)
# print(tri_obj.get_price())
#

class base:
    __base_variable="Not_initiated"
    def __init__(self):
            self.__base_variable="INIT"
    def print1(self):
        return "{}".format(self.__base_variable)
class layer1(base):
    def __init__(self,shared_object_from_base):
        self._layer1_var=shared_object_from_base
    def print1(self):
        return "<l1>{}</l1>".format(self._layer1_var.print1())

class layer2(base):
    def __init__(self,shared_object_from_layer1):
        self._layer2_var=shared_object_from_layer1
    def print1(self):
        return "<l2>{}</l2>".format(self._layer2_var.print1())

class layer3(base):
    def __init__(self,shared_object_from_layer2):
        self._layer3_var=shared_object_from_layer2
    def print1(self):
        return "<l3>{}</l3>".format(self._layer3_var.print1())

#
# layered_object=layer3(layer2(layer1(base())))
# print(layered_object.print1())

# class singleton:
#     __instance_variable="uninvoked"
#     def __init__(self):
#         if singleton.__instance_variable=="uninvoked":
#             singleton.__instance_variable=self
#         else:
#             raise Exception("duplicate instance")
#     @staticmethod
#     def get_instance():
#         if singleton.__instance_variable=="uninvoked":
#             singleton()
#             return singleton.__instance_variable
#
#         else:
#             return singleton.__instance_variable
#
#
# firstTime=singleton()
# print(firstTime)
# firstTime.get_instance()
# print(firstTime.get_instance())

class language1:
    def __init__(self):
        self.__language1_list=['l1.1','l1.2','l1.3']
    def get_list(self):
        return language1().__language1_list

class language2:
    def __init__(self):
        self.__language2_list=['l2.1','l2.2','l2.3']
    def get_list(self):
        return language2().__language2_list

class language3:
    def __init__(self):
        self.__language3_list=['l3.1','l3.2','l3.3']
    def get_list(self):
        return language3().__language3_list


class language_selector:

    def __init__(self):
        self.__language_object_dict={"language1":language1,"language2":language2,"language3":language3}
    def factory(self,language:str):
        return self.__language_object_dict[language]()

print(language_selector().factory("language1").get_list())
print(language_selector().factory("language2").get_list())
print(language_selector().factory("language3").get_list())

import random


class AbstractFactory:
    """ GeeksforGeeks portal for courses """

    def __init__(self, courses_factory=None):
        """course factory is out abstract factory"""

        self.course_factory = courses_factory

    def show_course(self):
        """creates and shows courses using the abstract factory"""

        course = self.course_factory()

        print(f'We have a course named {course}')
        print(f'its price is {course.Fee()}')


class DSA:
    """Class for Data Structure and Algorithms"""

    def Fee(self):
        return 11000

    def __str__(self):
        return "DSA"


class STL:
    """Class for Standard Template Library"""

    def Fee(self):
        return 8000

    def __str__(self):
        return "STL"


class SDE:
    """Class for Software Development Engineer"""

    def Fee(self):
        return 15000

    def __str__(self):
        return 'SDE'


def random_course():
    """A random class for choosing the course"""

    return random.choice([SDE, STL, DSA])()


if __name__ == "__main__":

    course = AbstractFactory(random_course)
    for i in range(3):
        print(object)
        course.show_course()


#====================================================================
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

#=====================================================reading files
import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
    #sorts data on keys
    hdata = {
        "people": [
            {
                "website": "stackabuse.com",
                "name": "Scott",
                "from": "Nebraska",


            }
        ]
    }
    print(json.dumps(hdata, sort_keys=True, indent=4))
#===============================================================requests
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


# #-------------------------------------------------input
# input_number=input("enter numbers comma seperated")
# print(input_number)
# without_comma_list=input_number.split(",")
# tuple=tuple(without_comma_list)
# print(tuple)
# print(without_comma_list)

# input_filename=input("enterfile name: ")
# print(input_filename.split(".")[-1])

#
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

#date difference
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)


def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))

class singleton:
    __instance_variable ="uninvoked"
    def __init__(self):
        if singleton.__instance_variable=="uninvoked":
            singleton.__instance_variable=self
        else:
            raise Exception("multitime inited")

    @staticmethod
    def get_instance():
        if singleton.__instance_variable=="uninvoked":
            singleton()
            return singleton.__instance_variable
        else:
            return singleton.__instance_variable

first=singleton()
print(first)
print(first.get_instance())