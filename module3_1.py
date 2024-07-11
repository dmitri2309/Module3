calls = 0
def string_info(string):
    count_calls()
    my_str = len(string)
    str_upper = string.upper()
    str_lower = string.lower()
    my_string = (my_str,str_upper,str_lower)
    return my_string
#def is_contain(list, list_to_search):
def is_contain(string, list_):
    count_calls()
    if string.lower() in [i.lower() for i in list_]:
    #list = list.lower()
    #list_to_search = [word.lower() for word in list_to_search]
    #if list in list_to_search:
        return True
    else:
        return False
def count_calls():
    global calls
    calls = calls + 1
    #return calls

my_string = string_info("Capybara")
print(my_string)
my_string = string_info("Armageddon")
print(my_string)
b = is_contain('urban',['ban','BaNaN','urBAN'])
print(b)
b = is_contain("cycle",['recycling','cyclic'])
print(b)
print(calls)

