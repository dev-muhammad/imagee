# import imagee as imagee
# from io import BytesIO
# import base64

# def from_path():
#     # image_path = "images/peach.jpg"
#     image_path = "images/peach.jpg"
#     output_path = "images/min_peach.png"

#     imagee.optimize(image_path, output_path)

# def to_bufer():
#     image_path = "images/ui.png"
#     buffer = BytesIO()
#     a, b = imagee.optimize(image_path, buffer)
#     print(a, b)

# from_path()

import functools

def check_access(*args, **kwargs):
    msisdn = False
    imsi = False
    if msisdn and imsi:
        # print(f"MSISDN {msisdn} - IMSI {imsi}")

        res = {}

        if (
            len(res)>0 
            and 
            "IMSI" in res[0].keys()
            and 
            int(imsi) == int(res[0]['IMSI'])
            ):
            return True, msisdn
        else:
            print("Wrong IMSI")
            return False, msisdn
    else:
        print("MSISDN and IMSI not exist")
        return False, msisdn

def auth_required(token=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_function(*args, **kwargs):
            # check msisdn and imsi
            print("Token ", token)
            has_access, msisdn = check_access(*args, **kwargs)
            if has_access:
                kwargs['msisdn'] = msisdn
                return func(*args, **kwargs)
            else:
                return {'status': "error", 'un_authorized': True}
        return wrapper_function
    return decorator


@auth_required(token=True)
def hello():
    print('hello')

hello()