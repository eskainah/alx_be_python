current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

if current_weather == "sunny":
    msg = "Wear a t-shirt and sunglasses."  

elif current_weather == "rainy":
    msg = "Don't forget your umbrella and a raincoat."

elif current_weather == "cold":
    msg = "Make sure to wear a warm coat and a scarf."
else:
    msg = "Sorry, I don't have recommendations for this weather."

print(msg)