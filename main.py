import requests
def start_session():
    url = "https://hackdiversity.xyz/api/start-session"
    data = {
        "firstName": "Kwabena",  
        "lastName": "Ampomah"  
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status() 
        session_id = response.json().get("session_id")
        if session_id:
            print(f" W it works the session ID: {session_id}")
            return session_id
        else:
            print("Chat your cooked")
    except requests.exceptions.RequestException as e:
        print(f"Failed to initialize session. Error: {e}")


        #session id is 4363a3f8-8f72-43bd-8d10-f29ddb936106


if __name__ == "__main__":
    session_id = start_session()