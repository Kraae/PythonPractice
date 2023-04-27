def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
def convert_temp(scale=None, source_temp=None):
 scale = input("Select (F) or (C): ")
 source_temp = int(input("What is the temperature: "))
 if (scale == "F") or (scale == "f"):
    return 'C', (source_temp - 32.0) * (5.0/9.0)
 if (scale == "C") or (scale == "c"):
    return 'F', (source_temp * (9.0/5.0)) + 32.0
 else:
    print("Needs to be (F) or (C)!")

s, m = convert_temp(scale, source_temp)
print(source_temp, "degrees", scale.title(), "is", m, "degrees", s)

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

