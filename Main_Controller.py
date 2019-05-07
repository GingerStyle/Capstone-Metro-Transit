import UI
import API_Manager

def main():
    #start the ui
    ui = UI

    #instantiate the API_Manager
    api_manager = API_Manager

    #get the currently running routes
    api_manager.get_routes()


main()