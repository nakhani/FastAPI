import requests

def get_requests_info():
    info = {
        "Version": requests.__version__,
        "License": requests.__license__, 
        "Copyright": requests.__copyright__, 
        "Author": requests.__author__, 
        "Author Email": requests.__author_email__, 
        "Documentation URL": requests.__url__, 
        "Title": requests.__title__, 
        "Description": requests.__description__
    }
    return info

if __name__ == "__main__":
    info = get_requests_info()
    for key, value in info.items():
        print(f"{key}: {value}")

