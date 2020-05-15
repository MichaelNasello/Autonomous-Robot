from drive import drive_forwards, turn
from run_model import run_live

def autonomous_mini_cart():
    """
    Runs through full code pipeline, from images capture to drive contols.
    """
    
    response = run_live()
    
    print('Received instruction: {}'.format(response.lower()))
        
    if response == 'Right':
        
        drive_forwards(3, 100, True)
        turn('right', 1.5, True)
        drive_forwards(7, 100, True)
        
    elif response == 'Left':
        
        drive_forwards(3, 100, True)
        turn('left', 1.5, True)
        drive_forwards(7, 100, True)
        
    elif response == 'Forwards':
        
        drive_forwards(15, 100, True)
        
    # do nothing if response == 'stay'


if __name__ == '__main__':

    autonomous_mini_cart()
