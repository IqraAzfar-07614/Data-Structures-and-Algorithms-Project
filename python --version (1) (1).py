from cProfile import label
import numpy as np
import geopy.distance
from geopy.geocoders import Nominatim
from helper_function import *
from hospital_finder import *
from tkinter import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("1100x700")

root['bg']='light blue'

# Create Frame
frame1 = Frame(root)
frame1.grid(pady = 5 )

label=tk.Label(root,bg='light blue', text="The Hospital Finder", font="comicsansms 25 bold", pady=1).grid(row=2, column=30)

Label(root,bg='light blue', text="Welcome to hospital finder! Here we will return you the closest hospitals in your proximity.", font="comicsansms 17", pady=1).grid(row=3, column=30)
name = Label(root,bg='light blue',font="comicsansms 10 bold", text="Name")
age = Label(root,bg='light blue',font="comicsansms 10 bold", text="Age")
gender = Label(root,bg='light blue',font="comicsansms 10 bold", text="Gender")
symptoms = Label(root,bg='light blue',font="comicsansms 10 bold", text="Symptoms")
location = Label(root,bg='light blue',font="comicsansms 10 bold", text="Location")

#Pack text for our form
name.place(x=160, y=100)
age.place(x=160, y=140)
gender.place(x=150, y=180)
symptoms.place(x=140, y=220)
location.place(x=150, y=260)

# Tkinter variable for storing entries
namevalue = StringVar()
agevalue = StringVar()
gendervalue = StringVar()
symptomsvalue = StringVar()
paymentmodevalue = StringVar()
Emergencymodevalue = StringVar()

#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
ageentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)

def commando():
    value = symptom.get()
    if value == 'Select Symptom':
        messagebox.showerror("Error", "Customer Details not found")
    else:
        hospital_update_dict = generate_hospital_dict(value)

def location_func():
    l_1 = location.get() #l_1 name of place
    loc_user = get_user_location(l_1) #coordinates for the user location

    closest_hospital = find_closest_hospital(loc_user)
    c_h_name, c_h_distance = closest_hospital[0], closest_hospital[1]

    message = 'The closest hospital to you is ' + str(c_h_name) + 'and is ' + str(c_h_distance) +'km away.\n \n'
    
    dj = dijkstra(G, l_1)
    shortest_path = get_shortest_path(l_1, c_h_name)

    ret = [i[1] for i in shortest_path]
    ret.insert(0, shortest_path[0][0])
    ret = " \u2192 ".join(ret)

    message2 = '  The path to go to the hospital is \n \n'
    message = message+message2+ ret
    
    hospital_info(c_h_name, message)

def hospital_info(x, message):
    answer = give_hospital_info(x)
    message = message+ answer
    print_message(message)

symptom = StringVar()
symptomsentry = ttk.Combobox(root, width=15, font=('comicsansms', 12), textvariable=symptom, values=['Select Symptom', 'Headache', 'Toothache', 'Cardiac problem', 'Fever', 'Stomach ache', 'Other'])
Button(text="CALL1", command=commando,font=('comicsansms', 12), bg='green', fg='white').place(x=400, y=220)

# LOCATION WALI LIST
location = StringVar()
locationentry = ttk.Combobox(root, width=15, font=('comicsansms', 12), textvariable=location, values= ['Abu Bakar Masjid', 'Agha Khan Hospital', 'Al-Shifa Homeo Clinic & Store', 'Baghpatee Group Of Companies', 'Bank Alfalah', 'Chase Up Flagship Store Johar', 'Darul Sehat Hospital', 'Dhoraji Chowrangi', 'Digital Door Intersection', 'Dr Abdul Hameed Diagnostic and Medical Center', 'Dr mashood hamid khan doraji', 'Everest Coaching Center', 'Fashion Communication', 'Flower Shop', 'Frenchies fries stall', 'Habib University', 'Hash Food Johar Branch', 'Jamal Noor Hospital', 'Johar Sweets', 'Liaquat National Hospital', 'Little Folks School', 'M.J Memorial Hospital', 'MCB Bank', 'MMQ DIAGNOSTIC AND MEDICAL CENTRE', 'MZ clothing', 'Mideast Dental Clinic', 'Millennium Bus Stop', 'My Hospital', 'Point1', 'Quetta Khyber Hotel', 'Rado Sweets & Bakers', 'Sunbeam Apartment', 'Super salateen restaurant', 'Turning1', 'Turning10', 'Turning2', 'Turning3', 'Turning4', 'Turning5', 'Turning6', 'Turning7', 'Turning8', 'Turning9'])
Button(text="FIND HOSPITAL", command=location_func,font=('comicsansms', 12), bg='green', fg='white').place(x=200, y=310)


# Packing the Entries
nameentry.place(x=220, y=100)
ageentry.place(x=220, y=140)
genderentry.place(x=220, y=180)
symptomsentry.place(x=220, y=220)
locationentry.place(x=220, y=260)

# temp function
def user_entry():
    txtarea.delete('1.0',END)
    # txtarea.insert(END, "\t\tSubmitting form\n")
    txtarea.insert(END, f" Patient Data: \n {namevalue.get()} ")
    txtarea.insert(END, f" \n {agevalue.get()} ")
    txtarea.insert(END, f" \n {gendervalue.get()} ")
    txtarea.insert(END, f" \n {symptom.get()} ")


    #txtarea.insert(END, "\nNEAREST HOSPITAL\n")
    #txtarea.insert(END, "\tHere you go..\n\n")

def print_output_shortest(s):
    txtarea.insert(END, s)

def print_message(s):
    user_entry()
    txtarea.insert(END, "\n========================================================\n")
    txtarea.insert(END, s)


def emergency_func():
    loc_user = choose1() #coordinates of the user
    closest_hospital = nearest_node(loc_user,hospital_coord)

    #create edge from user loc to nearest node in G
    create_user_edge(loc_user)
    dijkstra(G, 'Loc User')
    name = closest_hospital[0]
    shortest_path = get_shortest_path('Loc User', name)
    ret = [i[1] for i in shortest_path]
    ret.insert(0, shortest_path[0][0])

    ret = " \u2192 ".join(ret)
    message = 'Dear patient, ghabrana nahi hay, ambulance from the closest hospital,'+name+ ' is on the way.'
    print_message(message)


#Checkbox & Packing it
Button(text="EMERGENCY", command=emergency_func, bg='red', fg='white').place(x=50, y=450)

#Button & packing it and assigning it a command
#Button(text="Submit your records",bg='green',font=('comicsansms', 12), command=print_message).place(x=200, y=310)


#OUTPUT search result
F5 = LabelFrame(root, bd=10, relief=GROOVE)
F5.place(x=500, y=100, width=500, height=500)

# list title
receipt_title = Label(F5,text = 'Hospitals Nearby',font=('comicsansms', 12),bd=12,relief=GROOVE).pack(fill=X)
scroll_y = Scrollbar(F5,orient = VERTICAL)
txtarea = Text(F5,yscrollcommand=scroll_y.set)
scroll_y.pack(side = RIGHT,fill = Y)
scroll_y.config(command = txtarea.yview)
txtarea.pack(fill = BOTH, expand = 5)


root.mainloop()