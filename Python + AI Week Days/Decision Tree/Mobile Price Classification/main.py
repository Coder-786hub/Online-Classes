from tkinter import * 
import joblib 
import numpy
model = joblib.load("Mobile Price Predictor.joblib")





def check():
    input_ = input_box.get(1.0, END)
    np_df = np.asarray(input_text)
predictions = model.predict(np_df.reshape(1,-1))
if predictions == 0:
    print("Low Price")
elif predictions == 1:
    print("Medium Price")
elif predictions == 2:
    print("High Price")
else:
    print("Very High Price")


    output_label.config(text = f"The Predicted Value is { input_}")
    print(input_)


app = Tk()
app.title("Mobile Price Predector")
app.geometry("900x600+50+30")
app.config(bg = "#b0f7c3")

heading = Label(app, text = "MOBILE PRICE PREDICTOR", font = ("ROBOT", 35, "bold"), bg = "#b0f7c3", fg = "blue")
heading.pack(fill = "x", ipady = 20)

input_label = Label(app, text = "Enter Your input", font = ("ROBOT", 20, "bold"), bg = "#b0f7c3", fg = "red")
input_label.place(x = 100, y = 110)

input_box = Text(app,font = ("ROBOT", 18, "bold"), bg = "white", width = 50, height = 8)
input_box.place(x = 100, y = 150)

btn = Button(app, text = "PREDICT", font = ("ROBOT", 25, "bold"), bg = "#eb09df", fg = "green", command = check)
btn.place(x = 350, y = 400)

output_label = Label(app, text = "output",font = ("ROBOT", 18, "bold"), bg = "#b0f7c3", fg = "red")
output_label.place(x = 230, y = 500)

app.mainloop()
