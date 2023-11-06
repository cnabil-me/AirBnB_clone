import json

class Engine:
    def __init__(self, file_name):
        self.file_name = file_name

    def store_to_file(self, my_instance):
        # Convert an instance to a serializable data structure (dictionary)
        my_dict = my_instance.to_json()

        # Convert the data structure to a JSON string
        my_string = json.dumps(my_dict)

        # Write the JSON string to a file on disk
        with open(self.file_name, 'w') as file:
            file.write(my_string)

    def retrieve_from_file(self, MyObject):
        # Read a string from a file on disk
        with open(self.file_name, 'r') as file:
            my_string = file.read()

        # Convert the JSON string to a data structure (dictionary)
        my_dict = json.loads(my_string)

        # Convert the data structure back to an instance of MyObject
        my_instance = MyObject(my_dict)

        return my_instance
