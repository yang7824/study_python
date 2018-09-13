#!/usr/bin/env python3
import sys
import csv

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
        return float(self.config[key]) 

class UserData(object):
    def __init__(self, path):
        self.userdata = self._read_users_data(path)

    def _read_users_data(self, path):
        _userdata = {}
        with open(path) as user_file:
            for line in user_file:
                id_wages = line.split(',')
                _userdata[int(id_wages[0])] = int(id_wages[1])
        return _userdata


class lncomeTaxCalculator(object):
    def __init__(self):
        self.args = Args()
        self.config = Config(self.args.test_path)
        self.user = UserData(self.args.user_path)

    def _user_she_bao(self, wages):
        she_bao = wages*(self.config.get_config('YangLao') \
                    + self.config.get_config('YiLiao')  \
#                    + self.config.get_config('YangLao') \
                    + self.config.get_config('ShiYe')  \
                    + self.config.get_config('GongShang') \
                    + self.config.get_config('ShengYu') \
                    + self.config.get_config('GongJiJin') \
                    )
        return she_bao

    def user_tax(self, wages, she_bao):
        tax_wages = wages - she_bao - 3500
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

    def finally_wages(self, wages, she_bao, tax):
        f_wages = wages - she_bao - tax
        return f_wages


    def calc_for_all_userdata(self):
#        self.args = Args()
#        self.config = Config(self.args.test_path)
#        self.user = UserData(self.args.user_path)
        result = []
        for user_id, wages in self.user.userdata.items():
            she_bao = self._user_she_bao(wages) 
            tax = self.user_tax(wages, she_bao)            
            f_wages = self.finally_wages(wages, she_bao, tax)
            
            result.append([str(user_id), str(wages), format(she_bao, '.2f'), \
                      format(tax, '.2f'), format(f_wages, '.2f')])

#        print(result)
        return result

    def export(self, default = 'csv'):
        result = self.calc_for_all_userdata()
        with open(self.args.gongzi_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)
            print(result)

if __name__ == '__main__':

    test = lncomeTaxCalculator()
    test.export()
#    print(test.calc_for_all_userdata())






#args = Args()
#config = Config(args.test_path)
#user = UserData(args.user_path)

#print(config.get_config('JiShuL'))
#print(args.user_path)
#print(str(config.config))
#print(str(user.userdata))
#all_employee_dict = sys.argv[1:]
#for employee in all_employee_dict:
#    employee_dict = employee.split(':')
#    employee_id = employee_dict[0]
#    employee_wages = employee_dict[1]

#    print(employee_id,':',wages_final(employee_wages))
#    print("{}:{}".format(employee_id,format(wages_final(employee_wages),".2f")))

#    print("{}:{:.2f}".format(employee_id,wages_final(employee_wages)))
