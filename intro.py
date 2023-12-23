def main():
    subject, duration = get_info()

    print(f"{subject} will take {duration} months to master. ")
    
def get_info():
    subject = input("Subject: ")
    duration = input("Duration: ")
    return subject,duration

if __name__ == "__main__":
    main()