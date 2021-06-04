import tkinter
from config import Config


class Graphic:
    def __init__(self, text):
        self.root = tkinter.Tk()
        self.root.title("The naphthalene molecule")
        self.root.geometry(Config.screen_resolution)
        self.text = text

    def get(self):
        def start_button():
            button_start.config(state=tkinter.DISABLED)
            button_start.pack_forget()

            button_orbitals.place(
                relheight=.085,
                relwidth=.2,
                relx=.0,
                rely=.0
            )

            button_energy.place(
                relheight=.085,
                relwidth=.2,
                relx=.8,
                rely=.0
            )

            label.place(
                relx=.032,
                rely=.48
            )

        button_start = tkinter.Button(
            text="Start",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            command=start_button
        )
        button_start.pack()

        button_orbitals = tkinter.Button(
            text="Molecular orbitals",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            command=self.orbitals
        )

        button_energy = tkinter.Button(
            text="Energy levels",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            command=self.energy
        )

        label = tkinter.Label(
            text=self.text,
            justify=tkinter.LEFT,
            font="Arial 13"
        )

        self.root.mainloop()

    def orbitals(self):
        print("orbitals")

    def energy(self):
        print("energy")
