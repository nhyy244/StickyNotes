from tkinter import *
from tkinter import filedialog
if __name__ =="__main__":

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All files","*.*")])
        if file_path:
            with open(file_path,"w") as file:
                text_content = text_info.get("1.0",END)
                file.write(text_content)
    root = Tk()

    root.geometry("500x300")
    root.title("StickyNotes")
    root.minsize(width=200,height=200)
    root.maxsize(width=2000,height=3000)


    scrollbar =Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_info = Text(root, yscrollcommand=lambda *args: scrollbar.set(*args), highlightthickness=0)
    text_info.pack(fill=BOTH,expand=True)

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label="File", menu = file_menu)
    file_menu.add_command(label="Save",command=save_file)
    file_menu.add_command(label="Import")
    file_menu.add_separator()
    file_menu.add_command(label="Exit")


    root.config(menu=menu_bar)

    scrollbar.config(command=text_info.yview())



    #menu_bar.add_cascade(label="File",menu=file_menu)
    #file_menu.add_command(label="Save", command=save_file)


    root.mainloop()
