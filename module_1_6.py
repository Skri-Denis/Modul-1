my_dict = {'Denis': 1974 , 'Sasha': 1980, 'Julia': 2008}
print('Dict: ', my_dict)
print('Existing value: ', my_dict ['Sasha'])
print('Not existing value: ', my_dict.get('Yura'))
my_dict.update({'Sveta': 1965, 'Anton': 1993})
a=my_dict.pop('Julia')
print('Deleted value: ',a)
print('Modified dictionary: ', my_dict)

my_set = {'Dog' , 'Dog', 7,8,6,7, 2.12, 2.12, True,True}
print('Set: ', my_set)
my_set_1 = {'Cat', 36}
my_set.update(my_set_1)
my_set.discard('Dog')
print('Modified set: ', my_set)