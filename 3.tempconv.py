def cel_to_far(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
cel_temp = float(input("Enter temp in celsius"))

far_temp = cel_to_far(cel_temp)
print(f"{cel_temp} is equal to {far_temp}")

