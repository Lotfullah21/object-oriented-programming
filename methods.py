class Details:
    def __init__(self, name, duration):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.duration = duration
        
    def __str__(self):
        return f"this gives details about {self.name}"
    # getter
    def name(self):
        return self.name
    # setter
    def name(self,value):
        self.name = value
    
    def usage(self):
        match self.name:
            case "python":
                return "good for computational thinking artificial intelligence"
            case "machine learning":
                return "good for building the future"
            case "deep learning":
                return "best of all"
            # default case
            case _:
                return "no idea"
def main():
    details = get_info()
    print(details.name)
    details.name = "calculus"
    print(details.name)
    print(details.usage())

def get_info():
    name = input("Name: ")
    duration = input("Duration: ")
    return Details(name, duration)

if __name__ == "__main__":
    main()
