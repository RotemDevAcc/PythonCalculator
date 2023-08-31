import logging
from enum import Enum

logging.basicConfig(
    level=logging.DEBUG,          # Set the minimum log level to display
    format='%(asctime)s [%(levelname)s]: %(message)s',
    filename='my_app.log',        # Log messages to a file (optional)
)


def log_action(message,case):
    if(case is None or case == ""):
        case = "DEBUG"
    
    if(message == "" or message is None):
        logging.debug("log_action received an empty message")
        return

    case = case.upper()

    if(case == "DEBUG"):
        logging.debug(message, exc_info=True)
    elif(case == "INFO"):
        logging.info(message, exc_info=True)
    elif(case == "WARNING"):
        logging.warning(message, exc_info=True)
    elif(case == "ERROR"):
        logging.error(message, exc_info=True)
    elif(case == "CRITICAL"):
        logging.critical(message, exc_info=True)
    else:
        logging.debug("log_action was not used properly case non-existent")

        
class Actions(Enum):
    ADD = 1
    REMOVE = 2
    MULTI = 3
    DIV = 4

def calculate(method):

    try: 
        x1 = input("Enter A First Number: ")
        if(not x1.isdigit()):
                raise ValueError("Action was not a number")
        x2 = input("Enter A Second Number: ")
        if(not x2.isdigit()):
            raise ValueError("Action was not a number")
        x1 = int(x1)
        x2 = int(x2)
        result = 0
        if(method == "ADD"):
            result = x1 + x2
        elif(method == "REMOVE"):
            result = x1 - x2
        elif(method == "MULTI"):
            result = x1 * x2
        elif(method == "DIV"):
            result = x1 / x2

        print(f"Result: {result}")
    except ValueError as e:
        print(e)
        log_action(f"An error occurred: {str(e)}","debug")
    except Exception as e:
        log_action(f"An error occurred: {str(e)}","debug")
    

def print_actions(actions):
    for action in actions:
        print(f"{action.name} - {action.value}")

def start_program():
    while True:
        print_actions(Actions)
        action = input(f"Choose Your Action {1} ~ {len(Actions)}: ")
        try:
            if(not action.isdigit()):
                raise ValueError("Action was not a number")
            
            
            action = Actions(int(action))
            if(action == Actions.ADD):
                calculate(Actions.ADD.name)
            elif(action == Actions.REMOVE):
                calculate(Actions.REMOVE.name)
            elif(action == Actions.MULTI):
                calculate(Actions.MULTI.name)
            elif(action == Actions.DIV):
                calculate(Actions.DIV.name)


        except ValueError as e:
            log_action(f"An error occurred: {str(e)}","debug")
        except Exception as e:
            log_action(f"An error occurred: {str(e)}","debug")



if __name__ == "__main__":
    start_program()