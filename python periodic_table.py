import csv
import sys
import re


class PeriodicTable:
    def __init__(self):
        self.load_elements()
        self.ALL_COLUMNS = [
            'Atomic Number', 'Symbol', 'Element', 'Origin of name',
            'Group', 'Period', 'Atomic weight', 'Density',
            'Melting point', 'Boiling point',
            'Specific heat capacity', 'Electronegativity',
            'Abundance in earth\'s crust'
        ]
        self.LONGEST_COLUMN = max(map(len, self.ALL_COLUMNS))

    def load_elements(self):
        self.ELEMENTS = {}
        with open('periodictable.csv', encoding='utf-8') as elementsFile:
            elementsCsvReader = csv.reader(elementsFile)
            for line in elementsCsvReader:
                element = {
                    'Atomic Number': line[0],
                    'Symbol': line[1],
                    'Element': line[2],
                    'Origin of name': line[3],
                    'Group': line[4],
                    'Period': line[5],
                    'Atomic weight': line[6] + ' u',
                    'Density': line[7] + ' g/cm^3',
                    'Melting point': line[8] + ' K',
                    'Boiling point': line[9] + ' K',
                    'Specific heat capacity': line[10] + ' J/(g*K)',
                    'Electronegativity': line[11],
                    'Abundance in earth\'s crust': line[12] + ' mg/kg'
                }
                for key, value in element.items():
                    element[key] = re.sub(r'\[(I|V|X)+\]', '', value)
                self.ELEMENTS[line[0]] = element
                self.ELEMENTS[line[1]] = element

    def display_element_data(self, symbol_or_number):
        if symbol_or_number in self.ELEMENTS:
            element_data = self.ELEMENTS[symbol_or_number]
            for key in self.ALL_COLUMNS:
                key_justified = key.rjust(self.LONGEST_COLUMN)
                print(f'{key_justified}: {element_data[key]}')
            input('Press Enter to continue...')

    def run(self):
        while True:
            print('''            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')

            print('Enter a symbol or atomic number to examine, or QUIT to quit.')
            response = input('> ').title()

            if response == 'Quit':
                sys.exit()

            self.display_element_data(response)


if __name__ == '__main__':
    periodic_table = PeriodicTable()
    periodic_table.run()
