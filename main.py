from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon="venv\Resources\Calculator.jpg"
        self.operators=["/","*","+","-"]
        self.lastWasOperator=None
        self.lastButton=None

        mainLayout=BoxLayout(orientation="vertical")
        self.solution=TextInput(background_color="black",foreground_color="white",
                                multiline=False,halign="right", font_size=55, readonly=True)
#        self.equalButton.bind(on_press=self.on_solution)
        mainLayout.add_widget(self.solution)
        buttons=[
            ["7","8","9","/"],
            ["6","5","4","*"],
            ["1","2","3","+"],
            [".","0","C","-"],
        ]

        for row in buttons:
            h_layout=BoxLayout()
            for label in row:
                button=Button(
                    text=label,font_size=30, background_color="grey",
                    pos_hint={"center_x":0.5,"center_y":0.5}
                )
                button.bind(on_press=self.onButtonPress )
                h_layout.add_widget(button)
            mainLayout.add_widget(h_layout)

        equalButton=Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        equalButton.bind(on_press=self.on_solution)
        mainLayout.add_widget(equalButton)
        return mainLayout

    def onButtonPress(self,instance):
        current=self.solution.text
        button_text=instance.text

        if button_text=="C":
            self.solution.text=""
        else:
            if current and(
                self.lastWasOperator and button_text in self.operators):
                return
            elif current=="" and button_text in self.operators:
                return
            else:
                new_text=current + button_text
                self.solution.text=new_text
            self.lastButton=button_text
            self.lastWasOperator=self.lastButton in self.operators


    def on_solution(self,instance):
        text=self.solution.text
        if text:
            solution=str(eval(self.solution.text))
            self.solution.text=solution




if __name__ == "__main__":
    app=MainApp()
    app.run()
