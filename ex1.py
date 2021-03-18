open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def ex1(myStr):
    last_opened = []
    for i in myStr:
        if i in open_list:
            last_opened.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(last_opened) > 0) and
                    (open_list[pos] == last_opened[len(last_opened) - 1])):
                last_opened.pop()
            else:
                return "Unbalanced"
    if len(last_opened) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

# Driver program to test above function
print(ex1("[{()}]"))
