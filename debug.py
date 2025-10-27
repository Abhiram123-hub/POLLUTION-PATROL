# TODO: Write to a log file.
def log(message):
    print(message)

# TODO: Write to a log file.
def log_error(message):
    # Print in red text
    print("\033[91mERROR: %s\033[0m" % message)