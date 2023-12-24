class Details:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        
    def __str__(self):
        return f"this gives details about {self.name}"
    
    @classmethod
    def get_info(cls):
        name = input("Name: ")
        duration = input("Duration: ")
        # Create and return an instance of the class using the provided inputs
        return cls(name, duration)
    
def main():
    details = Details.get_info()
    print(f"{details.name} will take {details.duration} months to master.")
    print(details)


if __name__ == "__main__":
    main()
