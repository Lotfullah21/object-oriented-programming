class Details:
    def __init__(self, name, duration):
        if not name:
            raise ValueError("Missing name")
        if name.lower() not in ["python", "machine learning", "deep learning"]:
            raise ValueError("Not a valid subject")
        self.name = name
        self.duration = duration
        
    def __str__(self):
        return f"this gives details about {self.name}"
    

def main():
    details = get_info()
    print(f"{details.name} will take {details.duration} months to master.")
    print(details)

def get_info():
    name = input("Name: ")
    duration = input("Duration: ")

    return Details(name, duration)

if __name__ == "__main__":
    main()
