import requests
import ctypes
def download_image_from_url(url, save_path):

    """
    
    
    
    """


    response = requests.get(url)
    if response.status_code == 200:
     with open(save_path, 'wb') as file:
            file.write(response.content)
     print('Success!')
    else:
     print('Fialed, Response code:',response.status_code)
     return

    
def set_desktop_background_image(image):

    """
    
    
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)