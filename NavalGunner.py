import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext 
import math


class NavalGunneryHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("Naval Gunnery Helper")

        self.MUZZLE_VELOCITY = 853.44
        self.GRAVITY = 9.8
        self.range = tk.DoubleVar()
        self.angle_found = False


        # Create and configure the input frame
        input_frame = ttk.LabelFrame(root, text="Enter Distance to Enemy Ship (in meters)")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Distance:").grid(row=0, column=0)
        self.distance_entry = ttk.Entry(input_frame, textvariable=self.range)
        self.distance_entry.grid(row=0, column=1)
        ttk.Button(input_frame, text="Calculate Angle", command=self.calculate_best_angle).grid(row=1, columnspan=2)


        # Create the output frame
        self.output_frame = ttk.LabelFrame(root, text="Output")
        self.output_frame.grid(row=1, column=0, padx=10, pady=10)

        self.result_label = ttk.Label(self.output_frame, text="")
        self.result_label.grid(row=0, columnspan=2)

        # Create and configure the output frame with a scrolled text widget
        output_frame = ttk.LabelFrame(root, text="Output")
        output_frame.grid(row=1, column=0, padx=10, pady=10)

        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=40, height=15)
        self.output_text.grid(row=0, column=0, columnspan=2)

        ttk.Button(output_frame, text="Clear Output", command=self.clear_output).grid(row=1, column=0)
        ttk.Button(output_frame, text="Quit", command=root.quit).grid(row=1, column=1)
        


    def calculate_best_angle(self):
        user_range = self.range.get()
        tolerance = 5.0
        self.angle_found = False
        result_text = ""

        for angle in range(1, 46):
            angle_in_radians = math.radians(2 * angle)
            calculated_range = ((self.MUZZLE_VELOCITY ** 2) * math.sin(angle_in_radians)) / self.GRAVITY

            result_text += f"With the gun at angle {angle} degrees, the projectile will travel {calculated_range:.3f} meters,\n"

            if abs(calculated_range - user_range) <= tolerance:
                result_text += f"To hit the target, the gun should be set at the angle {angle} degrees.\n\n"
                self.angle_found = True
                break
            elif not self.angle_found:
                result_text += "So the enemy ship will not be hit.\n\n"

        if not self.angle_found:
            result_text += "The enemy ship cannot be hit at this distance.\n\n"

        self.output_text.delete(1.0, tk.END)  # Clear the previous output
        self.output_text.insert(tk.INSERT, result_text)  # Update the output

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)  # Clear the output area




if __name__ == "__main__":
    root = tk.Tk()
    app = NavalGunneryHelper(root)
    root.mainloop()



















        



        
