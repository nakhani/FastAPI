# 1.2 Introduction to API with AUTH

## Assignment 0:

1. **Run The Lord of the Rings API**
2. **Run IconFinder API**
3. **Run [D-ID.com](http://D-ID.com) API** 
4. **Run Illusion Diffusion API** 
5. **Run PlantNet API**

## Assignment 1: Plant 🌿

1. **Get a flower or plant’s name from user**
    - Use [argparse](https://docs.python.org/3/library/argparse.html) to get the plant name from the user.
2. **Use a text2image model API**
    - Utilize the [Illusion Diffusion](https://fal.ai/models/illusion-diffusion/api) API to generate an image of the flower or plant.
3. **Post generated image to Plant Recognition API**
    - Use the [PlantNet](https://my.plantnet.org/doc/openapi) API to recognize the flower or plant’s name.
4. **Print the name**
    - Output the recognized name of the plant.


## Assignment 2: FastAPI

1. **Run [FastAPI](https://fastapi.tiangolo.com/) hello world example**

## Assignment 3: Requests Module

  **Writing a Python program** to find the Requests module version, license, copyright information, author, author email, document URL, title, and description.


## Assignment 4: Using GitHub API

  **Writing a Python program** to print the count of my followers and my followings:
    ```bash
    https://api.github.com/users/{user}
    ```


## How to Run the Code
1. Clone the repository:
   ```sh
   git clone https://github.com/nakhani/FastAPI/tree/5e6e2a055c56e20eb305fa4eaa502102b6ed1fc3/Introduction_to_API_with_Auth
   ```

2. Navigate to the directory:
   ```sh
   cd Introduction_to_API_with_Auth
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Run Assignment_0 programs:
   ```sh
   python diffision.py 
   python lord.py  
   python icon.py  
   python planet.py  
   python di_id.py  
   python di_id_get.py #To get the result from di_id.py and use it in di_id_get.py, ensure that di_id.py saves the resulting URL correctly, and then di_id_get.py reads and processes this URL to retrieve the result.
   ```
5. Run Assignment_1 programs:
   ```sh
   python planet2.py "{Your Flower Or Planet's Name}"

6. Run Assignment_2 programs:
   ```sh
   python helloworld.py #For creating hello world API
   python run.py #For running hello world API

7. Run Assignment_3 programs:
   ```sh
   python request.py 

8. Run Assignment_4 programs:
   ```sh
   python github.py 
   
   

## Technologies Used
- Python 3




