Example_List = [
    'demo', 'style', 'configure_item', 'thread', 'thread_class',
    'theme', 'import_table', 'label_left', 'label_left_adv',
    'label_left_adv1', 'popup', 'font_add', 'font_size',
    'share', 'windows', 'list_display', 'get_value', 'add_widget', 'del_widget',
]

demo = """```css
        from dearpygui.demo import *
        show_demo ()
        start_dearpygui()```
        """

style = """```css
        from dearpygui import simple 
        show_style_editor()
        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/discussions/615>
"""

configure_item = """```css
        configure_item("Widget ID", items=["new item 1", "new item 2", "new item 3"]```
        <https://github.com/hoffstadt/DearPyGui/discussions/691>
"""

thread = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        import threading
        from time import sleep
        
        def background(sender, data):
        
            while True:
                print("Running in another thread!")
                sleep(0.5)
        
        def launcher():
            d = threading.Thread(name='daemon', target=background, daemon=True)
            d.start()
        
        with window('Main'):
            add_input_int('input')
        
        set_start_callback(launcher)

        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/discussions/657>
"""

thread_class = """```
        from dearpygui.core import *
        from dearpygui.simple import *
        import threading
        from time import sleep
        
        
        class Worker:
            def __init__(self):
                self.count = 0
        
            def run(self):
                while 1:
                    self.count += 1
                    print(self.count)
                    set_value('input', self.count)
                    sleep(0.5)
        
        
        def long_process():
            w = Worker()
            d = threading.Thread(name='daemon', target=w.run, daemon=True)
            d.start()
        
        
        with window('Main'):
            add_input_int('input')
        
        set_start_callback(long_process)
        
        start_dearpygui()```
"""

theme = """```css
        from  dearpygui.core import  *
        from  dearpygui.simple import  *
        
        with window('main'):
            add_text('Hello')
        
        set_theme('Gold')
        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/discussions/638>
"""

import_table = """```css
        Q : Can I copy some data from e.g. excel and paste it into the table?
        A : Not the current table (which is temporary). The new upcoming table will have support for this!```
        <https://github.com/hoffstadt/DearPyGui/discussions/608>  
"""

label_left = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        with window('Main Window'):
            add_text('text input 1 left label', default_value="text input 1")
            add_same_line()
            add_input_text('text input 1', label='')
        start_dearpygui(primary_window='Main Window')```
        <https://github.com/hoffstadt/DearPyGui/discussions/527>
"""

label_left_adv = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        def create_label(label):
            add_text(f'{label}_left_label', default_value=label)
            add_same_line()
        
        with window('Main Window'):
            create_label('text input 1')
            add_input_text('text input 1', label='')
        start_dearpygui(primary_window='Main Window')```
        <https://github.com/hoffstadt/DearPyGui/discussions/527>
"""

label_left_adv1 = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        def label_wrapper(widget_callable, name, **kwargs):
            add_text(f'{name}_left_label', default_value=f'{name}:')
            add_same_line()
            widget_callable(name, label='', **kwargs)
        
        with window('Main Window'):
            label_wrapper(add_input_text, name='input text 1', hint='Hello Fancy!')
        start_dearpygui(primary_window='Main Window')```
        <https://github.com/hoffstadt/DearPyGui/discussions/527>
"""

popup = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        with window("Tutorial"):
        
            add_text("Right Click Me")
        
            with popup("Right Click Me", "Popup ID", mousebutton=mvMouseButton_Right):
                add_text("A popup")
        
        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/discussions/513>
"""

font_add = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        add_additional_font("SomeFontFile.otf", 20)
        
        with window("Tutorial"):
            
            add_text("New Font")
        
        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/discussions/515>
"""
font_size = """```css
        from dearpygui.core import *
        from dearpygui.simple import *

        set_global_font_scale(1.2)

        with window("Tutorial"):

            add_text("New Font")

        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/discussions/515>
"""

share = """```css
        add_color_picker4("Widget 1", source="Color Data")
        add_slider_float4("Widget 2", source="Color Data")```
        <https://github.com/hoffstadt/DearPyGui/discussions/398>
"""

windows = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        # creating the window that the image will be drawn to
        with window('Image window'):
            pass
        
        with window('Image window2', no_title_bar=True):
            pass
        
        start_dearpygui()```
"""

list_display = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        # have a list you want to search
        list_of_items = ['a', 'ab', 'abc', 'b', 'bc', 'bcd']
        
        
        def searcher():
            # make a new list we will use to populate the listbox items parameter with
            modified_list = []
        
            # check to see if the searchbar has a value and if so we will get the items that contain the search items
            if get_value('Search'):
                for item in list_of_items:
                    if get_value('Search') in item:
                        modified_list.append(item)
        
            # set Results widget to use the new modified list
            configure_item('Results', items=modified_list)
        
        
        with window('Main Window'):
            add_input_text('Search', hint='Start typing to search', callback=searcher)
            add_listbox("Results", items=list_of_items)
        start_dearpygui(primary_window='Main Window')```
"""

get_value = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        def what_value():
            value = get_value("new slider")
            add_text(f"value is {value}", parent="Main")
        
        with window("Main", autosize=True, x_pos=400):
            add_slider_int("new slider")
            add_button("get value", callback=what_value)
        
        start_dearpygui()```
"""

add_widget = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        def add_buttons(sender, data):
            add_button("New Button", before="Delete Buttons")
            add_button("New Button 2", parent="Secondary Window")
        
        def delete_buttons(sender, data):
            delete_item("New Button")
            delete_item("New Button 2")
        
        show_debug()
        
        with window("Tutorial"):
            add_button("Add Buttons", callback=add_buttons)
            add_button("Delete Buttons", callback=delete_buttons)
        
        with window("Secondary Window"):
            pass
        
        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/wiki/Runtime-Adding-and-Deleting-Widgets>
"""

del_widget = """```css
        from dearpygui.core import *
        from dearpygui.simple import *
        
        def add_widgets(sender, data):
        
            with window("Secondary Window"): # simple
                add_button("New Button 2")
                add_button("New Button")
                add_button("New Button 3", parent="Secondary Window")
        
        def delete_widgets(sender, data):
            delete_item("Secondary Window")
            delete_item("New Button")
        
        def delete_children(sender, data):
            delete_item("Secondary Window", children_only=True)
        
        show_debug()
        
        with window("Tutorial"):
            add_button("Add Window and Items", callback=add_widgets)
            add_button("Delete Window and Children", callback=delete_widgets)
            add_button("Delete Window's Children", callback=delete_children)
        
        start_dearpygui()```
        <https://github.com/hoffstadt/DearPyGui/wiki/Runtime-Adding-and-Deleting-Widgets> 
"""
