#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    q = 0
    p = 0
    n = 0
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for content in lines:
                if int(content) % 2 == 0:
                    n = int(content)
                    p = int(content)/2
                    q = 2
                elif int(content) % 3 == 0:
                    n = int(content)
                    p = int(content)/3
                    q = 3
                elif int(content) % 5 == 0:
                    n = int(content)
                    p = int(content)/5
                    q = 5
                elif int(content) % 7 == 0:
                    n = int(content)
                    p = int(content)/7
                    q = 7
                else:
                    n = int(content)
                    p = int(content)/15485773
                    q = 15485773
                print("{}={}*{}".format(n, int(p), q))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
