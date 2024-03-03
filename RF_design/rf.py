import tkinter as tk

class User:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.channel = None
        self.cell = None

class NetworkSimulator:
    def __init__(self):
        self.users = {}
        self.channels = {}
        self.authenticated_users = set()

    def authenticate_user(self, name):
        self.authenticated_users.add(name)

    def add_user(self, name, x, y):
        if name in self.authenticated_users:
            self.users[name] = User(name, x, y)
        else:
            print("User not authenticated.")

    def assign_channel(self, user_name, channel_number):
        user = self.users.get(user_name)
        if user:
            user.channel = channel_number

    def display_users(self):
        for user in self.users.values():
            print(f"User: {user.name}, Location: ({user.x}, {user.y}), Channel: {user.channel}, Cell: {user.cell}")

    def select_channel(self, user_name):
        user = self.users.get(user_name)
        if user:
            return user.channel

    def handoff_strategy(self, user_name, new_channel):
        user = self.users.get(user_name)
        if user:
            user.channel = new_channel

    def create_cell(self, cell_name, x, y):
        self.channels[cell_name] = (x, y)

    def select_cell(self, user_name):
        user = self.users.get(user_name)
        if user:
            min_distance = float('inf')
            selected_cell = None
            for cell_name, cell_coordinates in self.channels.items():
                distance = ((user.x - cell_coordinates[0])**2 + (user.y - cell_coordinates[1])**2)**0.5
                if distance < min_distance:
                    min_distance = distance
                    selected_cell = cell_name
            return selected_cell

    def assign_user_to_cell(self, user_name, cell_name):
        user = self.users.get(user_name)
        if user:
            user.cell = cell_name

class NetworkSimulatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Network Simulator")

        # Make the window full screen
        master.attributes('-fullscreen', True)

        self.status_messages = []  # Store status messages
        self.current_user_name = None  # Initialize the variable to store the user name

        self.label = tk.Label(master, text="Welcome to Network Simulator")
        self.label.pack()

        self.authenticate_frame = tk.Frame(master)
        self.authenticate_frame.pack()

        self.authenticate_label = tk.Label(self.authenticate_frame, text="Authenticate User")
        self.authenticate_label.grid(row=0, column=0)

        self.name_label_auth = tk.Label(self.authenticate_frame, text="Name:")
        self.name_label_auth.grid(row=1, column=0)
        self.name_entry_auth = tk.Entry(self.authenticate_frame)
        self.name_entry_auth.grid(row=1, column=1)

        self.authenticate_button = tk.Button(self.authenticate_frame, text="Authenticate", command=self.authenticate_user)
        self.authenticate_button.grid(row=2, column=0)

        self.add_user_frame = tk.Frame(master)
        self.add_user_frame.pack()

        self.add_user_label = tk.Label(self.add_user_frame, text="Add User")
        self.add_user_label.grid(row=0, column=0)

        self.name_label_add = tk.Label(self.add_user_frame, text="Name:")
        self.name_label_add.grid(row=1, column=0)
        self.name_entry_add = tk.Entry(self.add_user_frame)
        self.name_entry_add.grid(row=1, column=1)

        self.x_label = tk.Label(self.add_user_frame, text="X Coordinate:")
        self.x_label.grid(row=2, column=0)
        self.x_entry = tk.Entry(self.add_user_frame)
        self.x_entry.grid(row=2, column=1)

        self.y_label = tk.Label(self.add_user_frame, text="Y Coordinate:")
        self.y_label.grid(row=3, column=0)
        self.y_entry = tk.Entry(self.add_user_frame)
        self.y_entry.grid(row=3, column=1)

        self.add_user_button = tk.Button(self.add_user_frame, text="Add User", command=self.add_user)
        self.add_user_button.grid(row=4, column=0)

        self.channel_frame = tk.Frame(master)
        self.channel_frame.pack()

        self.channel_label = tk.Label(self.channel_frame, text="Assign Channel")
        self.channel_label.grid(row=0, column=0)

        self.user_label_channel = tk.Label(self.channel_frame, text="User Name:")
        self.user_label_channel.grid(row=1, column=0)
        self.user_entry_channel = tk.Entry(self.channel_frame)
        self.user_entry_channel.grid(row=1, column=1)

        self.channel_number_label = tk.Label(self.channel_frame, text="Channel Number:")
        self.channel_number_label.grid(row=2, column=0)
        self.channel_number_entry = tk.Entry(self.channel_frame)
        self.channel_number_entry.grid(row=2, column=1)

        self.assign_channel_button = tk.Button(self.channel_frame, text="Assign Channel", command=self.assign_channel)
        self.assign_channel_button.grid(row=3, column=0)

        self.handoff_frame = tk.Frame(master)
        self.handoff_frame.pack()

        self.handoff_label = tk.Label(self.handoff_frame, text="Handoff Strategy")
        self.handoff_label.grid(row=0, column=0)

        self.user_label_handoff = tk.Label(self.handoff_frame, text="User Name:")
        self.user_label_handoff.grid(row=1, column=0)
        self.user_entry_handoff = tk.Entry(self.handoff_frame)
        self.user_entry_handoff.grid(row=1, column=1)

        self.new_channel_label = tk.Label(self.handoff_frame, text="New Channel:")
        self.new_channel_label.grid(row=2, column=0)
        self.new_channel_entry = tk.Entry(self.handoff_frame)
        self.new_channel_entry.grid(row=2, column=1)

        self.handoff_button = tk.Button(self.handoff_frame, text="Handoff Strategy", command=self.handoff_strategy)
        self.handoff_button.grid(row=3, column=0)

        self.cell_frame = tk.Frame(master)
        self.cell_frame.pack()

        self.cell_label = tk.Label(self.cell_frame, text="Create Cell")
        self.cell_label.grid(row=0, column=0)

        self.cell_name_label = tk.Label(self.cell_frame, text="Cell Name:")
        self.cell_name_label.grid(row=1, column=0)
        self.cell_name_entry = tk.Entry(self.cell_frame)
        self.cell_name_entry.grid(row=1, column=1)

        self.cell_x_label = tk.Label(self.cell_frame, text="X Coordinate:")
        self.cell_x_label.grid(row=2, column=0)
        self.cell_x_entry = tk.Entry(self.cell_frame)
        self.cell_x_entry.grid(row=2, column=1)

        self.cell_y_label = tk.Label(self.cell_frame, text="Y Coordinate:")
        self.cell_y_label.grid(row=3, column=0)
        self.cell_y_entry = tk.Entry(self.cell_frame)
        self.cell_y_entry.grid(row=3, column=1)

        self.create_cell_button = tk.Button(self.cell_frame, text="Create Cell", command=self.create_cell)
        self.create_cell_button.grid(row=4, column=0)

        self.status_label = tk.Label(master, text="Status:")
        self.status_label.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_and_show_status)
        self.quit_button.pack()

        self.network = NetworkSimulator()

    def authenticate_user(self):
        name = self.name_entry_auth.get()
        self.current_user_name = name  # Store the user name
        self.network.authenticate_user(name)
        self.update_status(f"User '{name}' authenticated.")

    def add_user(self):
        if self.current_user_name:
            name = self.current_user_name  # Use the stored user name
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            self.network.add_user(name, x, y)
            self.update_status(f"User '{name}' added at ({x}, {y}).")
        else:
            self.update_status("Please authenticate user first.")

    def assign_channel(self):
        if self.current_user_name:
            user_name = self.current_user_name  # Use the stored user name
            channel_number = int(self.channel_number_entry.get())
            self.network.assign_channel(user_name, channel_number)
            self.update_status(f"Channel {channel_number} assigned to user '{user_name}'.")
        else:
            self.update_status("Please authenticate user first.")

    def handoff_strategy(self):
        if self.current_user_name:
            user_name = self.current_user_name  # Use the stored user name
            new_channel = int(self.new_channel_entry.get())
            self.network.handoff_strategy(user_name, new_channel)
            self.update_status(f"Handoff strategy applied for user '{user_name}' to channel {new_channel}.")
        else:
            self.update_status("Please authenticate user first.")

    def create_cell(self):
        cell_name = self.cell_name_entry.get()
        x = float(self.cell_x_entry.get())
        y = float(self.cell_y_entry.get())
        self.network.create_cell(cell_name, x, y)
        self.update_status(f"Cell '{cell_name}' created at ({x}, {y}).")

    def update_status(self, message):
        self.status_messages.append(message)

        # Update the status label with the latest message
        self.status_label.config(text="Status: " + message)

    def quit_and_show_status(self):
        # Destroy the main window
        self.master.destroy()

        # Show all recorded status messages
        self.show_all_status()

    def show_all_status(self):
        # Create a new window to display all status messages
        status_window = tk.Toplevel()
        status_window.title("All Status Messages")

        # Create a text widget to display status messages
        text_widget = tk.Text(status_window, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)

        # Insert each status message into the text widget
        for message in self.status_messages:
            text_widget.insert(tk.END, message + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = NetworkSimulatorGUI(root)
    root.mainloop()
