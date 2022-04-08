from collections import defaultdict
import datetime

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.meta_data = []
    def add_meta_data(self, n):
        self.meta_data.append(n)
    def __str__(self):
        return 'k=' + str(self.key) + ' v=' + str(self.val) + ' meta=' + str(list(map(str, self.meta_data)))

ref = {
        'NOTE':'0',
        'HEAD':'0',
        'TRLR':'0',
        'FAM':'0',
        'INDI':'0',
        'BIRT':'1',
        'DEAT':'1',
        'MARR':'1',
        'DIV':'1',
        'HUSB':'1',
        'WIFE':'1',
        'CHIL':'1',
        'NAME':'1',
        'SEX':'1',
        'FAMC':'1',
        'FAMS':'1',
        'DATE':'2'
      }


def parse_nodes(file_name):
    f = open(file_name)
    stacks = defaultdict(list)
    stacks[-1].append(Node('DUMMY', ''))
    for l in f.readlines():
        line = l.split()
        if not line:
            continue
        if not line[0].isdigit():
            continue
        valid = 'Y' if line[1] in ref else 'N'
        level = line[0]
        tag = line[1]
        args = ' '.join(line[2:])
        #print('--> ', level, ' | ', tag, ' | ', valid, ' | ', args)
        curr_node = Node(tag, args)
        stacks[int(level)].append(curr_node)
        stacks[int(level)-1][-1].add_meta_data(curr_node)
    #print(list(map(str, stacks[-1][-1].meta_data)))
    nodes = stacks[-1][-1].meta_data
    #print(nodes[0])
    return nodes


def is_lesser_than(date1, date2):
    if date1 > date2:
        return False
    return True


def us01_check_dates_before_current_date(file_name):
    nodes = parse_nodes(file_name)
    for node in nodes:
        for first_level_meta in node.meta_data:
            if first_level_meta.key in ['BIRT', 'DEAT', 'MARR', 'DIV']:
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
                        if not is_lesser_than(date, datetime.datetime.now()):
                            return False
    return True


def us02_check_birth_before_marriage(file_name):
    nodes = parse_nodes(file_name)
    birth_date = None
    marriage_date = None
    for node in nodes:
        for first_level_meta in node.meta_data:
            if first_level_meta.key == 'BIRT':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        birth_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
            elif first_level_meta.key == 'MARR':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        marriage_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
        if not birth_date or not marriage_date:
            continue
        if not is_lesser_than(birth_date, marriage_date):

            return False
    return True

def us04_check_marriage_before_divorce(file_name):
    nodes = parse_nodes(file_name)
    marriage_date = None
    divorce_date = None
    for node in nodes:
        for first_level_meta in node.meta_data:
            if first_level_meta.key == 'MARR':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        marriage_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')

            elif first_level_meta.key == 'DIV':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        divorce_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')

        if not divorce_date or not marriage_date:
            continue
        if not is_lesser_than(marriage_date, divorce_date):
            return False
    return True

def us05_check_marriage_before_death(file_name):
    nodes = parse_nodes(file_name)
    marriage_date = None
    death_date = None
    for node in nodes:
        for first_level_meta in node.meta_data:
            if first_level_meta.key == 'MARR':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        marriage_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
            elif first_level_meta.key == 'DEAT':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        death_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
        if not death_date or not marriage_date:
            continue
        if not is_lesser_than(marriage_date, death_date):
            return False
    return True

def us08_check_birth_before_marriage_of_parents(file_name):
    nodes = parse_nodes(file_name)
    birth_date = None
    marriage_date = None
    for node in nodes:
        for first_level_meta in node.meta_data:
            if first_level_meta.key == 'BIRT':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        birth_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
            elif first_level_meta.key == 'MARR':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        marriage_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')

        if not birth_date or not marriage_date:
            continue
        if not is_lesser_than(birth_date, marriage_date):
            return False
    return True

def us09_check_birth_before_death_of_parents(file_name):
    nodes = parse_nodes(file_name)
    birth_date = None
    death_date = None
    for node in nodes:
        for first_level_meta in node.meta_data:
            if first_level_meta.key == 'BIRT':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        birth_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
            elif first_level_meta.key == 'DEAT':
                for second_level_meta_data in first_level_meta.meta_data:
                    if second_level_meta_data.key == 'DATE':
                        print(second_level_meta_data.val, first_level_meta.key)
                        death_date = datetime.datetime.strptime(second_level_meta_data.val, '%d %b %Y')
        if not birth_date or not death_date:
            continue
        if not is_lesser_than(birth_date, death_date):
            return False
    return True




#us08_check_birth_before_marriage_of_parents('Family.ged')
us09_check_birth_before_death_of_parents('Family.ged')