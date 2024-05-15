import sys

def trigger_exception():
    try:
        # This line will raise a ZeroDivisionError
        result = 10 / 0
        print(result)  # This line won't be executed
    except ZeroDivisionError as e:
        # Handle the exception
        print("Exception caught:", e)
        raise  # Re-raise the exception to fail the task

# Call the function to trigger the exception
trigger_exception()
