import logging
logging.basicConfig(
    level=logging.DEBUG,                  # Set the lowest level to capture (DEBUG)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
    datefmt='%Y-%m-%d %H:%M:%S',         # Date format
    filename='app.log',                  # Log file name (if logging to a file)
    filemode='a'                         # File mode ('a' for append, 'w' for overwrite)
)

i = 5
while i>0:
    try:
        if(i%2==0):
           
            logging.debug("Even number")
        else:
            logging.error("Odd number")
    except Exception as e:
        logging.exception("Exception occurred")
    i-=1
if i==0:
    logging.info("Loop executed successfully")