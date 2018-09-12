#!/usr/bin/env python3
import sys

class Args(object):

    def __init__(self):
        try:
            self.args = sys.argv[1:]
            self.test_path = self.args[self.args.index('-c') + 1]
            self.user_path = self.args[self.args.index('-d') + 1]
            self.gongzi_path = self.args[self.args.index('-o') + 1]
            self.user_path2 = 'test'
        except:
            print("input Errer!")
            sys.exit()

class Config(object):
    def __init__(self, path):
        self.config = self._read_config(path)

    def _read_config(self, path):
        config = {}
        with open(path, 'rt') as config_file:
            for line in config_file:
                key_vaule = line.split('=')
#                key_vaule[0].strip('\n')
#                key_vaule[1].strip('\n')
                key_vaule[0] = key_vaule[0].strip()
                key_vaule[1] = key_vaule[1].strip()
                config[key_vaule[0]] = key_vaule[1]
        return config

    def get_config(self, key):
        return self.config[key] 

def fax_count(wages):
    try:
        wages = int(wages)
    except:
        print("Parameter Error")
    tax_wages = wages - wages*(0.08 + 0.02 + 0.005 + 0.06)- 3500
    tax_x = 0
    tax_rate = 0.00
    if tax_wages > 0 and tax_wages <= 1500:
        tax_rate = 0.03
        tax_x = 0
    elif tax_wages > 1500 and tax_wages <= 4500:
        tax_rate = 0.10
        tax_x = 105
    elif tax_wages > 4500 and tax_wages <= 9000:
        tax_rate = 0.20
        tax_x = 555
    elif tax_wages > 9000 and tax_wages <= 35000:
        tax_rate = 0.25
        tax_x = 1005
    elif tax_wages > 35000 and tax_wages <= 55000:
        tax_rate = 0.30
        tax_x = 275
    elif tax_wages > 55000 and tax_wages <= 80000:
        tax_rate = 0.35
        tax_x = 5505
    elif tax_wages > 80000:
        tax_rate = 0.45
        tax_x = 13505
    if tax_wages > 0:    
        tax = tax_wages * tax_rate - tax_x
    else:
        tax = 0.00 
    return tax

def wages_final(wages):
    try:
        wages = int(wages)
    except:
        print("Parameter Error")
    f_wages = wages - wages*(0.08 + 0.02 + 0.005 + 0.06) - fax_count(wages)
    return f_wages

args = Args()
config = Config(args.test_path)

print(config.get_config('JiShuL'))
print(args.user_path)
print(str(config.config))
#all_employee_dict = sys.argv[1:]
#for employee in all_employee_dict:
#    employee_dict = employee.split(':')
#    employee_id = employee_dict[0]
#    employee_wages = employee_dict[1]

#    print(employee_id,':',wages_final(employee_wages))
#    print("{}:{}".format(employee_id,format(wages_final(employee_wages),".2f")))

#    print("{}:{:.2f}".format(employee_id,wages_final(employee_wages)))
