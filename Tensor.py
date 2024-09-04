import traceback
import os 
import time

def trace_function():
    traceback.print_stack()
import traceback

def with_traceback(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      print(f"Error in function '{func.__name__}':")
      traceback.print_exc()
      raise e  # Re-raise the exception for proper handling

  return wrapper
class private_return(void)

# Example usage (assuming you have your speech-to-text and text-to-speech code)
@with_traceback
def my_speech_to_text_function(audio_data):
  return "This is the transcribed text"

@with_traceback
def my_text_to_speech_function(text):
  print(f"Speaking: {text}")
if __name__ == "__main__":
  # Example usage:
  audio_data = # Your audio data acquisition logic (replace with your actual implementation)
  text = my_speech_to_text_function(audio_data)
  my_text_to_speech_function(text)
  
  import traceback

def trace_function():
    """
    This function prints a traceback every time it's called.

    Returns:
        None
    """
    traceback.print_stack()
import Tensor

# Call the trace_function multiple times
for _ in range(5):
    Tensor.trace_function()

