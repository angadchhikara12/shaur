from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
import pyttsx3

class OhioJokeApp(App):
    def build(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

        self.jokes = [
            "Where was the first upside-down car was invented? Only in Ohio!",
            "Where does medical doctors sells corn dogs? Only in Ohio!",
            "Where was ohio joke was invented? Only in Ohio!",
            "Where was Grilled Cheese Obama Sand which song was invented? Only in Ohio!",
            "Where was Yo Mama joke was invented? Only is Ohio!",
            "Where is the bringing guns to school is normal? Only in Ohio!"
        ]



        # UI layout
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Joke label
        self.joke_label = Label(text="Press the button for an Ohio joke!", font_size='20sp', halign='center')
        layout.add_widget(self.joke_label)

        # Button
        joke_button = Button(text="Tell Me a Joke", on_press=self.tell_joke, font_size='18sp')
        layout.add_widget(joke_button)

        return layout

    def tell_joke(self, instance):
        selected_joke = random.choice(self.jokes)
        self.say(selected_joke)
        self.joke_label.text = selected_joke


    def say(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

if __name__ == '__main__':
    OhioJokeApp().run()