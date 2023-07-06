def reverseList(_list) :
    _newList = []
    
    for x in _list :
        _newList.append(_list[(len(_list) - 1) - _list.index(x)])
    print(_newList)
    
_list = [1, 2, 3, 4]
reverseList(_list)