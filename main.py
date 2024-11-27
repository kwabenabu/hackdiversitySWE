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

def findtheroute(session_id):
    url= "https://hackdiversity.xyz/api/navigation/routes"
    headers = {"Authorization": f"Bearer {session_id}"}
    try:
         response = requests.get(url, headers=headers)
         #erro catch
         response.raise_for_status()
         #return routes here 
         return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return []
    #dataRoutes: [{'id': '1', 'from': 'Entrance', 'to': 'Exhibit A', 'accessible': True, 'distance': 150}, {'id': '2', 'from': 'Entrance', 'to': 'Restroom', 'accessible': True, 'distance': 50}, {'id': '3', 'from': 'Exhibit A', 'to': 'Cafeteria', 'accessible': False, 'distance': 200}, {'id': '4', 'from': 'Restroom', 'to': 'Gift Shop', 'accessible': True, 'distance': 70}, {'id': '5', 'from': 'Cafeteria', 'to': 'Exhibit B', 'accessible': True, 'distance': 300}, {'id': '6', 'from': 'Entrance', 'to': 'Exhibit B', 'accessible': False, 'distance': 400}, {'id': '7', 'from': 'Exhibit B', 'to': 'Exit', 'accessible': True, 'distance': 150}, {'id': '8', 'from': 'Cafeteria', 'to': 'Restroom', 'accessible': True, 'distance': 180}, {'id': '9', 'from': 'Gift Shop', 'to': 'Exhibit C', 'accessible': False, 'distance': 220}, {'id': '10', 'from': 'Exhibit C', 'to': 'Restroom', 'accessible': True, 'distance': 130}, {'id': '11', 'from': 'Entrance', 'to': 'Exhibit C', 'accessible': True, 'distance': 500}, {'id': '12', 'from': 'Exhibit B', 'to': 'Gift Shop', 'accessible': False, 'distance': 60}, {'id': '13', 'from': 'Cafeteria', 'to': 'Entrance', 'accessible': True, 'distance': 240}, {'id': '14', 'from': 'Exhibit C', 'to': 'Exit', 'accessible': True, 'distance': 275}, {'id': '15', 'from': 'Gift Shop', 'to': 'Exit', 'accessible': True, 'distance': 95}, {'id': '16', 'from': 'Entrance', 'to': 'Exhibit D', 'accessible': True, 'distance': 430}, {'id': '17', 'from': 'Exhibit D', 'to': 'Restroom', 'accessible': False, 'distance': 85}, {'id': '18', 'from': 'Exhibit D', 'to': 'Cafeteria', 'accessible': True, 'distance': 120}, {'id': '19', 'from': 'Exhibit A', 'to': 'Exit', 'accessible': False, 'distance': 340}, {'id': '20', 'from': 'Cafeteria', 'to': 'Exhibit C', 'accessible': True, 'distance': 190}, {'id': '21', 'from': 'Lobby', 'to': 'Exhibit A', 'accessible': True, 'distance': 160}, {'id': '22', 'from': 'Lobby', 'to': 'Gift Shop', 'accessible': True, 'distance': 75}, {'id': '23', 'from': 'Exhibit C', 'to': 'Exhibit B', 'accessible': False, 'distance': 210}, {'id': '24', 'from': 'Restroom', 'to': 'Lobby', 'accessible': True, 'distance': 65}, {'id': '25', 'from': 'Cafeteria', 'to': 'Lobby', 'accessible': False, 'distance': 250}, {'id': '26', 'from': 'Exhibit B', 'to': 'Lobby', 'accessible': True, 'distance': 290}, {'id': '27', 'from': 'Gift Shop', 'to': 'Cafeteria', 'accessible': True, 'distance': 110}, {'id': '28', 'from': 'Exhibit D', 'to': 'Lobby', 'accessible': False, 'distance': 130}, {'id': '29', 'from': 'Exhibit A', 'to': 'Exhibit D', 'accessible': True, 'distance': 320}, {'id': '30', 'from': 'Lobby', 'to': 'Exit', 'accessible': True, 'distance': 180}]
    #looks lik building map distance only need accesbile routes 
    # probs gonna go insertion sort or bubble data is kinda sorted already 
def accesiblefilter (routes):
    accessible_routes = []
    #simple for loop if its accesible in the dict 
    for route in routes:
        #id accesible key exist in the each set keep that route 
        if route['accessible']:
            accessible_routes.append(route)
    return accessible_routes
# i bubble sort is way easier for implememtation doesnt veer off 
def bubble_sort(routes):
    # length of the rotues store the value of 
    length = len(routes)
    #simple for loop
    for i in range(length):
        #bubble sort copy stright 
        for j in range(0, length - i - 1):
            # Compare distances of adjacent elements
            if routes[j]['distance'] > routes[j + 1]['distance']:
                # Swap if the previous element is larger
                #creating a temp element of prev
                temp = routes[j]
                routes[j] = routes[j + 1]
                routes[j + 1] = temp
    return routes


def submit(session_id, sorted_routes):
    #just copied the start session
    url = "https://hackdiversity.xyz/api/navigation/sorted_routes"  
    headers = {"Authorization": f"Bearer {session_id}"}
    try:
        response = requests.post(url, json=sorted_routes, headers=headers)
        response.raise_for_status()
        print("W bro bro")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error {e}")


if __name__ == "__main__":
    session_id = start_session()  
    if session_id:
        routes = findtheroute("4363a3f8-8f72-43bd-8d10-f29ddb936106")  
        if routes:
            accessible_routes = accesiblefilter(routes)
            sorted_routes = bubble_sort(accessible_routes)
            for route in accessible_routes:
                print(route)
            submit(session_id, sorted_routes)
    else:
        print("im cooked")
