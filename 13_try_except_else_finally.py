UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
    except ZeroDivisionError as e:
        return UNDEFINED
    else:                           #When other exception are raised
        op['result'] = value
        return value
    finally:
        handle.close()              #Always run after try
