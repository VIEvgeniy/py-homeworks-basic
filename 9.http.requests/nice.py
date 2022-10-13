def nice_print(*args, tab=0, quot=False):
    for val in args:
        if isinstance(val, dict):
            nice_print('\t' * tab, '{', tab=tab)
            if val:
                tab += 1
                for el in val:
                    if isinstance(val[el], list):
                        nice_print('\n\t' * tab)
                    nice_print(el, quot=True)
                    nice_print(': ')
                    nice_print(val[el], quot=True)
                    nice_print(',')
                nice_print('\b')
                if isinstance(val[el], list):
                    nice_print('\n')
                tab -= 1
            nice_print('}', tab=tab)
        elif isinstance(val, list):
            nice_print('\t' * tab, '[\n', tab=tab)
            tab += 1
            for el in val[:-1]:
                nice_print('\t' * tab, el, ',\n', tab=tab)
            nice_print('\t' * tab, val[-1], '\n', tab=tab)
            nice_print('\t' * tab, ']')
        elif isinstance(val, str):
            if quot:
                print("'", sep="", end="")
            print(val, sep="", end="")
            if quot:
                print("'", sep="", end="")
        else:
            print(val, sep='', end="")
