#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
smtpObj.login('pablo.93.rodriguez@gmail.com', input())
mail_dict = dict(zip(mail,name))
for mail, name in mail_dict.items():
    body = "Subject: Inquiry about job offers\nHello, I'm highly motivated and intelligent. I am useful to you.)
    print('Sending email to %s...' % mail)
    sendmailStatus = smtpObj.sendmail('pablo.93.rodriguez@gmail.com', mail, body)
    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (mail,sendmailStatus))
    


# In[120]:


import tkinter, os, smtplib

from tkinter import messagebox, filedialog

from tkinter import *

class reminder_program:                        
    
    def __init__(self, parent):
        
        self.main_frame = parent 
        self.main_frame = Frame(parent, height = 300, width = 600)
        self.main_frame.grid()
    
        self.email_dict = {}
        self.sender_email = ''
        self.user_directory = ''
        self.user_email = ''
        self.reminderee_email = ''
        self.remindee_email = ''
        self.remindee_name = ''
        self.text_message_name = '' 
        
        self.login_register(parent)
        
    def login_register(self,parent):
        self.login_register = Toplevel(parent)
        
        self.login_register.wm_title('User Register / Login')
        self.login_register.wm_attributes('-topmost', True)
        
        register_label = Label(self.login_register, text = 'REGISTER e-mail')
        
        user_label = Label(self.login_register, text = 'Associate e-mail')
        register_email = StringVar()
        register_entry = Entry(self.login_register, relief = 'flat', textvariable = register_email)
        
        directory_label = Label(self.login_register, text = 'Choose Directory')
        directory_choice = StringVar()
        directory_entry = Entry(self.login_register, relief = 'flat', textvariable = directory_choice)
        
        program_folder = Label(self.login_register, text = 'Folder Name')
        folder_name = StringVar()
        directory_folder = Entry(self.login_register, relief = 'flat', textvariable = folder_name)
        
        create_button = Button(self.login_register, text = "Create", width = 12)
        
        def user_and_email(event):
            
            user_email = register_email.get() #gets the user's email
            program_directory = directory_choice.get() #registers a place to create the folder for the email
            directory_name = folder_name.get() #registers the folder's name
            
            self.email_dict[user_email] = program_directory + '\\' + directory_name #associates user_email with a directory
            
            for email, directory in self.email_dict.items():
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    os.makedirs(directory + '\\' + 'Login')
                    os.makedirs(directory + '\\' + 'Saved Texts')
                    os.makedirs(directory + '\\' + 'Peoples emails')
                    
            self.user_directory = program_directory + '\\' + directory_name  + '\\' + 'Login' + '\\'
            
            with open(self.user_directory + 'login_user.txt', 'w') as output:
                if user_email not in 'login_user.txt':
                    output.write(user_email + '\n')
            return self.email_dict
            return self.user_directory
        create_button.bind('<Button-1>', user_and_email)
        create_button.bind('<Return>', user_and_email)
            
            
        login_label = Label(self.login_register, text = 'LOGIN')
        login_email = StringVar()
        login_entry = Entry(self.login_register, relief = 'flat', textvariable = login_email)
        
        user_button = Button(self.login_register, text = 'Select')
        
        def show_registered_users(event):
            dropVar = StringVar()
            if self.user_directory != '':
                with open(self.user_directory + '/' + 'Login' + '/' +'login_user.txt', 'r') as file:
                    values = file.read()
                    dropVar.set(values)
                    
                comboentry = OptionMenu(self.login_register, dropVar,
                                 values)
                comboentry.grid(row = 17, columnspan = 2)
                
            else:
                select_dir = filedialog.askdirectory(initialdir = 'C:/Users/pablo/Documents/Personal/', 
                                       title = 'Select directory')
                self.user_directory = select_dir
                with open(select_dir + '/' + 'Login' + '/' + 'login_user.txt', 'r') as file:
                    values = file.read()
                    dropVar.set(values)
                
                def sel_user_name(value):
                    self.user_email = value
                comboentry = OptionMenu(self.login_register, dropVar,
                                       values, command = sel_user_name)
                comboentry.grid(row=17, columnspan = 2)
                    
            def read_selected(event):
                user_title = Label(self.main_frame, text = 'Welcome: ' + self.user_email)
                user_title.grid(row = 0, column = 2)

                self.login_register.destroy()
                
                self.reminderee_registry(parent)
                self.message_select(parent)
            user_button.bind('<Button-1>', read_selected)
            
        login_entry.bind('<Button-1>', show_registered_users)
        
        self.login_register.grid(baseWidth = 250, baseHeight = 400,
                                widthInc = 250, heightInc = 400)
        register_label.grid(row = 0, columnspan = 2)
        user_label.grid(row = 1, column = 0, sticky = 'e')
        register_entry.grid(row = 1, column = 1, sticky = 'w')
        directory_label.grid(row = 2, column = 0, sticky = 'e')
        directory_entry.grid(row = 2, column = 1, sticky = 'w')
        program_folder.grid(row = 3, column = 0, sticky = 'e')
        directory_folder.grid(row = 3, column = 1, sticky = 'w')
        create_button.grid(row=4, columnspan = 2, pady = 5, padx = 85)
        login_label.grid(rowspan = 16, columnspan = 2, ipadx = 85, pady = 85)
        login_entry.grid(row = 17, columnspan = 2)
        user_button.grid(row = 18, columnspan = 2)
        
    def reminderee_registry(self, parent):
        
        self.reminderee_frame = Frame(self.main_frame)
        reminderee_label0 = Label(self.reminderee_frame,
                                 text = 'Please write the person to be reminded\'s name & e-mail.'+
                                 ' Or choose the person from the list below.')
        reminderee_label1 = Label(self.reminderee_frame,
                                 text = 'reminderee\'s e-mail')
        reminderee_email = StringVar()
        reminderee_entry1 = Entry(self.reminderee_frame,
                                  relief = 'flat',
                                  textvariable = reminderee_email,
                                 width = 40)
        
        reminderee_label2 = Label(self.reminderee_frame,
                                 text = 'their name')
        reminderee_name = StringVar()
        reminderee_entry2 = Entry(self.reminderee_frame,
                                  relief = 'flat',
                                  textvariable = reminderee_name,
                                 width = 40)
        reminderee_listbox = Listbox(self.reminderee_frame, width = 40)
        
        reg_rem = Button(self.reminderee_frame, text = 'Register', width = 12)
        
        if self.remindee_email != '' and self.remindee_name != '':
            
            def add_reminderee(event):
                self.remindee_email = reminderee_email.get()
                self.remindee_name = reminderee_name.get()
                with open(self.user_directory + '/' + 'Peoples emails' + '/' +'reminderees.txt', 'a+') as file:
                    tot_rem = self.remindee_name + ', ' + self.remindee_email
                    file.write(tot_rem + '\n')
                    reminderee_listbox.insert(END, tot_rem)
                reminderee_entry1.delete(0, 'end')
                reminderee_entry2.delete(0, 'end')
            reg_rem.bind('<Button-1>', add_reminderee)
        else:
            with open(self.user_directory + '/' + 'Peoples emails' + '/' +'reminderees.txt', 'r') as output:    
                remindee = output.readlines()
                for line in remindee:
                    reminderee_listbox.insert(END, line)
    
        def remindee_mail(event):
            selected = reminderee_listbox.curselection()
            self.reminderee_email = reminderee_listbox.get(selected)
        reminderee_listbox.bind('<Double-Button>', remindee_mail)
        
        self.reminderee_frame.grid(row = 0, 
                                   pady = '5m',
                                   padx = 40,
                                   sticky = 'nwe')
        reminderee_label0.grid(row = 0, columnspan = 2, padx = 5, pady = 10, sticky = 'ne')
        
        reminderee_label1.grid(row = 1, column = 0, sticky = 'ne')
        reminderee_entry1.grid(row = 1, column = 1, sticky = 'ne')
        
        reminderee_label2.grid(row = 2, column = 0, sticky = 'se' )
        reminderee_entry2.grid(row = 2, column = 1, sticky = 'se')
        
        reminderee_listbox.grid(row = 3, column = 1, sticky = 'ne', pady = 8)
        reg_rem.grid(row = 4, column = 2)
        
    def message_select(self, parent):
        self.select_frame = Frame(self.main_frame)
        
        message_label = Label(self.select_frame,
                             text = 'Select Message')
        message_listbox = Listbox(self.select_frame, width = 40)
        
        for foldername, subfolder,filenames in os.walk(self.user_directory + '/' + 'Saved texts' + '/'):
            for files in filenames:
                message_listbox.insert(END, files)
                
        def select_message_listbox(event):
            selection = message_listbox.curselection()
            self.text_message_name = message_listbox.get(selection)

            
        message_listbox.bind('<Button-1>', select_message_listbox)
        
        new_message = Button(self.select_frame,
                            text = 'New Message')
        def new_message_button(event):
            self.new_message_button = Toplevel(parent)
            self.new_message_button.wm_title('New Reminder')
            self.new_message_button.wm_attributes('-topmost', True)
            
            new_message_label = Label(self.new_message_button,
                                      text = 'Please write your new message')
            new_message_text = Text(self.new_message_button,
                                     width = 80, height = 20)
            save_button = Button(self.new_message_button,
                                text = 'Save Message')
            def save_button_retrieve(event):
                retrieve_text = new_message_text.get('1.0', 'end-1c')
                
                self.save_retrieve = Toplevel(parent)
                self.save_retrieve.wm_title('Save this message?')
                self.save_retrieve.wm_attributes('-topmost', True)
                
                save_retrieve_label = Label(self.save_retrieve,
                                           text = 'Name of text')
                save_retrieve_string = StringVar()
                save_retrieve_entry = Entry(self.save_retrieve,
                                           textvariable = save_retrieve_string)
                
                save_retrieve_save = Button(self.save_retrieve,
                                           text = 'Save me')
                def retrieve_save(event):
                    name_pre_writ = save_retrieve_string.get()
                    with open(self.user_directory + '/' + 'Saved texts' + '/' + name_pre_writ + '.txt', 'w+') as output:
                        name_output = name_pre_writ+'.txt'
                        output.write(retrieve_text)
                        message_listbox.insert(END, name_output)
                    self.save_retrieve.destroy() 
                save_retrieve_save.bind('<Button-1>', retrieve_save)
                save_retrieve_save.bind('<Return>', retrieve_save)
                
                save_retrieve_cancel = Button(self.save_retrieve,
                                             text = 'Cancel',
                                             width = 7)
                def retrieve_cancel(event):
                    self.save_retrieve.destroy()
                save_retrieve_cancel.bind('<Button-1>', retrieve_cancel)
                save_retrieve_cancel.bind('<Return>', retrieve_cancel)
                
                save_retrieve_label.grid(row = 0, column = 0)
                save_retrieve_entry.grid(row = 0, column = 1)
                save_retrieve_save.grid(row = 1, column = 0)
                save_retrieve_cancel.grid(row = 1, column = 1)
            save_button.bind('<Button-1>', save_button_retrieve)
            save_button.bind('<Return>', save_button_retrieve)
            
            
            cancel_button = Button(self.new_message_button,
                                  text = 'Cancel', width = 12)
            def message_cancel_button(event):
                self.new_message_button.destroy()
            cancel_button.bind('<Button-1>', message_cancel_button)
            cancel_button.bind('<Return>', message_cancel_button)
            
            
            new_message_label.grid(row = 0, columnspan = 2,
                                  pady = 5, padx = 10)
            new_message_text.grid(row = 1, columnspan = 2,
                                  pady = 2, padx = 10)
            save_button.grid(row = 2, column = 0,
                            pady = 3)
            cancel_button.grid(row = 2, column = 1,
                              pady = 3)
        new_message.bind('<Button-1>', new_message_button)
        new_message.bind('<Return>', new_message_button)
            
            
        set_time = Button(self.select_frame,
                         text = 'Set Time', width = 11)
        def prepare_email(event):
            self.time_send = Toplevel(parent)
        
            self.time_send.wm_title('User Register / Login')
            self.time_send.wm_attributes('-topmost', True)
            
            email_from = Label(self.time_send, text = 'From: ' + self.sender_email)
            email_to = Label(self.time_send, text = 'To: ' + self.reminderee_email)
            with open(self.user_directory + '/' + 'Saved texts' + '/' + self.text_message_name, 'r') as file:
                email_body = file.read()
            email_text = Label(self.time_send, text = email_body)
            
            self.time_send.grid()
            email_from.grid(row = 0, column = 0)
            email_to.grid(row = 1, column = 0)
            email_text.grid(row = 2, columnspan = 2)
        
        set_time.bind('<Button-1>', prepare_email)    
        #Make email: Show it to user: and set time. 
        
        self.select_frame.grid(row = 2, columnspan = 2, sticky = 'sw', pady = '10m')
        message_label.grid(row = 0, column = 0, padx = 40)
        message_listbox.grid(row = 1, column = 0, padx = 40)
        new_message.grid(row = 3, column = 0, sticky = 'sw', padx = 40, pady = 10)
        set_time.grid(row = 3, column = 0, sticky = 'se', padx = 40, pady = 10)
test = reminder_program
root = Tk()
root.geometry('{}x{}'.format(800, 600))
myapp = reminder_program(root)
root.mainloop()

