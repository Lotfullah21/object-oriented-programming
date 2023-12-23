def main():
    details = get_info()
    print(f"{details["subject"]} will take {details["duration"]} months to master. ")
    
def get_info():
    details = {}
    details["subject"] = input("Subject Name: ")
    details["duration"] = input("Time it takes: ")
    return details


def get_same():
    # directly we can return a dictionary as well.
    name = input("name of the subject: ") 
    duration = input("time it takes: ")   
    return {"name":name, "duration":duration}

if __name__ == "__main__":
    main()