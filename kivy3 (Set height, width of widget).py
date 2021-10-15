import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



class MyGridLayout(GridLayout):
    #initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set column
        self.cols = 1
        #self.col_force_default=True
        #self.col_default_width = 100
        #self.row_force_default=True
        #self.row_default_height=40
        
        #Create second GridLayout
        self.top_grid = GridLayout(
            col_force_default=True,
            col_default_width = 300,
            row_force_default=True,
            row_default_height=80
        )
        self.top_grid.cols = 2
       

        #Add widget
        self.top_grid.add_widget(Label (text="Name :"))
        #Add input box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name) 


        self.top_grid.add_widget(Label(text="Roll :"))
        #Add input box
        self.roll = TextInput(multiline=False)
        self.top_grid.add_widget(self.roll)


        self.top_grid.add_widget(Label(text="ID :"))
        #Add input box
        self.id = TextInput(multiline=False)
        self.top_grid.add_widget(self.id)


        #Add new topgrid in app
        self.add_widget(self.top_grid)


        #create a button
        self.button = Button(text="Submit",
     
        font_size=32,
        size_hint_y=None, 
        height=50, 
        size_hint_x=None,
        width=160
      
         )

        #Bind button
        self.button.bind(on_press=self.press)
        self.add_widget(self.button)
        
    
    #Create a function for button    
    def press(self, instance):
        name = self.name.text
        roll = self.roll.text
        id = self.id.text

        self.add_widget(Label(text=f"Your Name {name}, Roll {roll}, ID {id}"))

        #remove input data
        self.name.text = ""
        self.roll.text = ""
        self.id.text = ""
       
        
      



class FirstApp(App):
    def build(self):
        return MyGridLayout()


if __name__== '__main__':
    FirstApp().run()
     
