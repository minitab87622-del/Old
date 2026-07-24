import os
from datetime import datetime
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class AgeCalculatorApp(App):

  def build(self):
    self.title = 'Age Calculator'

    main_layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

    # Background Canvas
    with main_layout.canvas.before:
      if os.path.exists('background.png'):
        self.bg = Rectangle(
            source='background.png',
            pos=main_layout.pos,
            size=main_layout.size,
        )
      else:
        Color(0.06, 0.09, 0.16, 1)
        self.bg = Rectangle(pos=main_layout.pos, size=main_layout.size)

    main_layout.bind(pos=self.update_bg, size=self.update_bg)

    # Title Header
    title_label = Label(
        text='Age Calculator',
        font_size='24sp',
        bold=True,
        color=(0.22, 0.74, 0.97, 1),
        size_hint_y=None,
        height=50,
    )
    main_layout.add_widget(title_label)

    # Date Inputs (Day, Month, Year)
    input_card = BoxLayout(
        orientation='horizontal', spacing=10, size_hint_y=None, height=50
    )

    self.day_input = TextInput(
        hint_text='Day (1-31)',
        input_filter='int',
        multiline=False,
        halign='center',
    )
    self.month_input = TextInput(
        hint_text='Month (1-12)',
        input_filter='int',
        multiline=False,
        halign='center',
    )
    self.year_input = TextInput(
        hint_text='Year (1998)',
        input_filter='int',
        multiline=False,
        halign='center',
    )

    input_card.add_widget(self.day_input)
    input_card.add_widget(self.month_input)
    input_card.add_widget(self.year_input)
    main_layout.add_widget(input_card)

    # Calculate Button
    calc_btn = Button(
        text='Calculate Age',
        font_size='18sp',
        bold=True,
        size_hint_y=None,
        height=50,
        background_color=(0.01, 0.52, 0.78, 1),
    )
    calc_btn.bind(on_press=self.calculate_age)
    main_layout.add_widget(calc_btn)

    # Result Output
    self.result_label = Label(
        text='Enter your birth date and press Calculate',
        font_size='16sp',
        halign='center',
        color=(0.97, 0.98, 0.99, 1),
    )
    main_layout.add_widget(self.result_label)

    return main_layout

  def update_bg(self, instance, value):
    self.bg.pos = instance.pos
    self.bg.size = instance.size

  def calculate_age(self, instance):
    try:
      b_year = int(self.year_input.text)
      b_month = int(self.month_input.text)
      b_day = int(self.day_input.text)

      today = datetime.now()
      birth_date = datetime(b_year, b_month, b_day)

      if birth_date > today:
        self.result_label.text = 'Birth date cannot be in the future!'
        return

      years = today.year - birth_date.year
      months = today.month - birth_date.month
      days = today.day - birth_date.day

      if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1

        if prev_month in [1, 3, 5, 7, 8, 10, 12]:
          days_in_prev = 31
        elif prev_month in [4, 6, 9, 11]:
          days_in_prev = 30
        else:
          days_in_prev = (
              29
              if (
                  prev_year % 4 == 0
                  and (prev_year % 100 != 0 or prev_year % 400 == 0)
              )
              else 28
          )
        days += days_in_prev

      if months < 0:
        years -= 1
        months += 12

      self.result_label.text = (
          f'Age: {years} Years, {months} Months, {days} Days'
      )
    except Exception:
      self.result_label.text = 'Please enter valid numbers!'


if __name__ == '__main__':
  AgeCalculatorApp().run()
