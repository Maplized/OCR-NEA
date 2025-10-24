developermode = 0
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import urllib.request
import webbrowser
from time import sleep

# Scientific Calculator System
# --------------------------------------------------------

# Libraries ---
import customtkinter as ctk # The Fundemental UI
import tkinter as tk # For misc. parts of the code
from PIL import Image # Images
from tkinter import messagebox # Messageboxes

import math # Complex mathematical processes
import re # Complex mathematical processing

import statistics # Statistical processes

import matplotlib.pyplot as plt # Graph drawing
import numpy as np # Equation processing

import random # Probabilities
from random import randint # Random Number Generation

# ---

ctk.set_appearance_mode("System") # Theme configuration (my
root = ctk.CTk()                  # system is dark themed)
root.geometry("760x420+60+40")
root.title("Calculator")
root.resizable(0,0)

tabview = ctk.CTkTabview(root, width=780, height=423, segmented_button_selected_color=
                         "deepskyblue4")
tabview.place(x=3,y=-7) # Tab widget

calculate = tabview.add("Calculate") # Tabs
stat = tabview.add("Statistics") #     |
graph = tabview.add("Graph & Table") # |
conv = tabview.add("Conversion") #     |
box = tabview.add("Math Box") #        |
tabview.set("Calculate") # "set("Calculate")" makes the calculate
                         # tab be a default mode when opening the
                         # calculator

# Misc. Functions ---

def shutdown(): # Closes calculator
    closeprompt = messagebox.askyesno("Confirm Exit",("Are you sure you want to exit the calculator?"))
    if closeprompt:
        root.destroy()

def pasteinx(): # Pastes the CALCULATE answer to x
    ans = inputoutput.get()
    xentry.delete("1.0", ctk.END)
    xentry.insert(index=(1.0), text=ans)

def pasteiny(): # Pastes the dCALCULATE value to y
    ans = inputoutput.get()
    yentry.delete("1.0", ctk.END)
    yentry.insert(index=(1.0), text=ans)

idnum = randint(10000,99999)
def information(): # Help & Info
    global rootinfo
    try: # Prevent duplicate windows
        if rootinfo.winfo_exists():
            return
    except:
        pass

    rootinfo = ctk.CTkToplevel()
    rootinfo.geometry("500x650+1020+40")
    rootinfo.title("Software Information")
    rootinfo.resizable(0,0)
    
    def viewoptions_callback(values, exclude): # Displays which section of information is shown
        for widget in rootinfo.winfo_children():
            if widget != exclude: # this is to keep the CTkOptionWidget open
                widget.place_forget()
        
        if values == "Introduction":
            # The General User Manual
            nextview = ctk.CTkLabel(rootinfo, text=" Attribution → ", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            nextview.place(x=365,y=80)
            banner_i = ctk.CTkLabel(rootinfo, text="  Introduction", font=("segoe ui bold", 35),
                                     height=70, width=320, fg_color="deepskyblue4", anchor="w")
            banner_i.place(x=0,y=0)
            banner_i2 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue3", height=70,
                                      width=100)
            banner_i2.place(x=319,y=0)
            banner_i3 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue2", height=70,
                                      width=100)
            banner_i3.place(x=418,y=0)

            # The entire text content ↓ ↓ ↓
            introtext = """Welcome to the Scientific Calculator!
This calculator is like your convential 
physical scientific calculator, but now in digital form.
There are (currently) 4 modes available! With them
ranging from CALCULATE, STATISTICS, GRAPH & TABLE & CONVERSION!

It is generally recommended to use an attached
keyboard to insert mathematical expressions, but
if this isn't possible, the calculator will
provide an on-screen keyboard or number pad to
do this.

All modes contain a set of miscellaneous
buttons. Use the X button to close the calculator
and then confirming this and the i button to
display the information window (Which is what you
are currently seeing right now, obviously).
Specific modes will also have their unique
miscellaneous button(s) that have their own
purpose for that mode.

This calculator relies on the Windows Operating
System, and can be used for any Edition you are
on (i.e. Home Edition, Education Edition)

———————————————————————————

• CALCULATE
The core mode of the calculator.
Calculate mathematical expressions ranging from 
trigonometric functions, inverse trigonometry, 
logarithms, algerbra... or even just basic calculations really..

You are also able to store answers from inputs or 
outputs in your very own notebook! Your notebook
is able to store many forms of data that you could
use later! Use the yellow insert button to insert 
any data from the input or output into your notebook! 
Then you can copy values to use them at any
time and paste them to wherever you want!
To clear your notebook, press the very top icon
on the right!

Lets talk about the buttons:

[0-9] Pretty self-explanatory
[+ - × ÷ ( ) ] Also pretty self-explanatory
[Fractions] Quickly insert the value ( / ), replicating
a fraction
[Square Root] Calculate the square root of a value
[Power of..?] Calculate a value to the power of something
[!] Calculate the Factorial of something
[x & y] Insert algerbra into the mathematical expression
[Sin x...] Insert Trigonometeric functions
[Cos⁻¹ x...] Insert inverse Trigonometric functions
[Log x] Insert logarithm with the base number of 10
[Ln x] Insert the natural logarithm
[Logn x] Insert logarithm with a base number of something
[Pi & e] Gives the value of pi and e

Use these buttons insert a particular mathematical
expression (such as 3+0, which we all know what the
answer is...), and the calculator will, unsuprisingly,
output an answer of 3!

What else can you do with this cheeky answer of 3?
Well, you can store it in an x or y variable! On
the right you see 4 buttons, but on the top middle
button, you can define an x or y variable! You can
paste the output (or input) value of, in this case,
3 into the entry feild and thus defining that
variable!

——————————————————————————


• STATISTICS
Introducing statistics! Ever have large data sets
that you want to evaluate from? Well now
you can! Insert data into the program (optionally 
with the frequency) and you will be able to find
the mean, mode, range, median, the sum of the 
data, the number of data or more!

You could also consider having another chunk of 
data with the y peice of data and you can
simultaneously calculate both chunks of data sets!

If you don't have a keyboard attached, you can open a 
seperate window with a number pad that includes all 
the numbers and the x and y variables.

You can only enter numbers and variables into
the entries; no extranous text such as
operators, letters or just random symbols.

Now... to use STATISTICS, you will need to
configure it's settings. You can have the
frequency enabled! This allows you to repeatedly
insert values into the data.
You can also use 2 variables, allow you to
simultanously insert 2 peices of data at
onces.
Or, you can have these both enabled!
Or, just have nothing enabled. We'll
assume x data has a frequency of 1!

To insert a row of data, fill in all the blank
entries. You may leave some blank, but the
calculator will make assumptions to these
blank entries. 
After that, you should then press the insert
button to insert the data into the data
columns.

Once you confirm everything is correct, you may
click the execute button; a seperate window will
appear containing all the results of (if enabled)
both sets of data along with their (if enabled)
frequencies.

Use the Delete ALL button to clear all data
once you finished using this.

———————————————————————————

• GRAPH & TABLE
Thanks to matplotlib, you can now draw out the
graph of a certain equation you have in mind! Or if
you ever wanted to substitute some values of x
into the equation, you can just do that with the
Table function!

This mode has basically 2 mini-like modes which
are sort've combined together, like a pair of a
synergy!

With GRAPH, you may insert an equation you'd
like to draw! Starting with y=...? You can
insert a numerical expression that can be in
terms of x, or not..
Press the execute button and the calculator 
will draw and display the equation in a
seperate window for you to observe.

You can hover around the graph, and the
calculator will display the coordinates
based on your cursour's position on the
graph

You can also zoom! Press the zoom button
and select an area you'd like to zoom
into.

Move the graph using the move button, click,
hold and drag your cursor around to move
the graph around!

To go back to the previous view, use the
undo version, but if you'd like to reset
the view of the graph, use the cheeky
home button!

Now with TABLE! Table is slightly similar
to the STATISTICS mode, but you can now
substitute x values into a function 
(defined by an equation)

How do we define an equation? Use the
define button to carefully define a function
using your 3 previously drawn out
equations! You can define up to 2 different
types of functions: f(x) and g(x)

After a function(s) is defined, insert a
value of x, then press the execute button to
allow the calculator to use your x value,
substitute and output the function's result!

———————————————————————————

• CONVERSION
With this mode, you can converted different
types of units! Here, you can convert the
length, area, weight, volume, temperature
and speed.

First off, choose a conversion topic! You will
need to press the choose topic button to
display the conversio topic window. After
that, you may choose a topic. The window will
display all the available units for that 
conversion topic!

After selecting an conversion topic, you can
now select a measure unit and input a value
into one of the two entries. Either entry
will input or output the values.

———————————————————————————

• MATH BOX
This mode is pretty unique, essentially being
a random probability based mode.
Playing board games?
Betting heads or tails?
Need to select which team goes first?
This mode has you covered!

In COIN, you are able to toss a fair or biased
coin, consisting the outputs of heads & tails!
A fair coin is a simple 50/50 equal chance.
A biased coin however lets you change the probability
of each side

In DICE, a fixed probaility includes many different
sides. You can select a number of pre-set sides
ranging from 3, the normal 6, 10 and up to 100!
Or you can set a custom amount of dice sides, with
a limit of 1000 sides.
"""            
                      
            text_i = ctk.CTkTextbox(rootinfo, font=("Montserrat medium", 17), height=530, width=490,
                                    fg_color="grey14", wrap="word")
            text_i.place(x=5, y=115)
            text_i.insert("1.0", introtext)
            text_i.configure(state="disabled") # Prevents the user from editing the text
            closeimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
            close = ctk.CTkButton(rootinfo, text=None, image=closeimg,
                                  hover_color="red4", fg_color="grey14", corner_radius=
                                  0, width=40, height=40, command=rootinfo.destroy)
            close.place(x=440,y=600) # To close the information window

        elif values == "Attribution":
            # Crediting

            def viewatt_callback(values):
                text_at.configure(state="normal")
                text_at.delete("1.0", ctk.END)
                if values == "Attribution":
                    licensetext = """This project uses the following fonts under the SIL Open 
Font License (OFL):

• Source Code Pro - Copyright © 2010-2012 Adobe Systems 
Incorporated

• STIX Two Text - Copyright © 2001-2021 The STIX Fonts 
Project Authors

• Noto Sans Math - Copyright © 2012 Google Inc.

• Montserrat - Copyright © 2011 The Montserrat Project 
Authors

Each font is licensed under the SIL Open Font License.
See the included OFL for details. For more information,
visit https://openfontlicense.org

——————————————————————————————————————————————————————————

This project uses Google Material Icons, which are
licensed under the Apache License 2.0 (AL 2.0).

See the included AL 2.0 for details.
You may obtain a copy of the License at
https://www.apache.org/licenses/LICENSE-2.0
            """

                elif values == "OFL":
                    licensetext = """----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
----------------------------------------------------------

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded, 
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting -- in part or in whole -- any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are
not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.
"""

                elif values == "AL 2.0":
                    licensetext = """Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.
"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.
"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.
"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.
"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.
"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.
"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.
"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).
"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.
"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."
"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:
You must give any other recipients of the Work or Derivative Works a copy of this License; and
You must cause any modified files to carry prominent notices stating that You changed the files; and
You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and
If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License.
You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.
END OF TERMS AND CONDITIONS
"""
                text_at.insert("1.0", licensetext)
                text_at.configure(state="disabled")

            nextview = ctk.CTkLabel(rootinfo, text=" Credits → ", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            nextview.place(x=365,y=80)

            prevview = ctk.CTkLabel(rootinfo, text=" ← Introduction", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            prevview.place(x=35,y=80)
            banner_at = ctk.CTkLabel(rootinfo, text="  Attribution", font=("segoe ui bold", 35),
                                     height=70, width=320, fg_color="deepskyblue4", anchor="w")
            banner_at.place(x=0,y=0)
            banner_at2 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue3", height=70,
                                      width=100)
            banner_at2.place(x=319,y=0)
            banner_at3 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue2", height=70,
                                      width=100)
            banner_at3.place(x=418,y=0)

            licensetext = """This project uses the following fonts under the SIL Open 
Font License (OFL):

• Source Code Pro - Copyright © 2010-2012 Adobe Systems 
Incorporated

• STIX Two Text - Copyright © 2001-2021 The STIX Fonts 
Project Authors

• Noto Sans Math - Copyright © 2012 Google Inc.

• Montserrat - Copyright © 2011 The Montserrat Project 
Authors

Each font is licensed under the SIL Open Font License.
See the included OFL for details. For more information,
visit https://openfontlicense.org

——————————————————————————————————————————————————————————

This project uses Google Material Icons, which are
licensed under the Apache License 2.0 (AL 2.0).

See the included AL 2.0 for details.
You may obtain a copy of the License at
https://www.apache.org/licenses/LICENSE-2.0
            """
            text_at = ctk.CTkTextbox(rootinfo, font=("Source Code Pro", 13), height=500, width=490,
                                    fg_color="grey14", wrap="word")
            text_at.place(x=5, y=115)
            text_at.insert("1.0", licensetext)
            text_at.configure(state="disabled")

            view_att = ctk.CTkOptionMenu(rootinfo, values=["Attribution","OFL","AL 2.0"],
                                        fg_color="grey20", font=("Source Code Pro", 16),
                                        button_color="grey14", dropdown_fg_color="grey12",
                                        dropdown_font=("Source Code Pro", 13), 
                                        dropdown_hover_color="deepskyblue4",
                                        button_hover_color="grey14",
                                        width=150, command=viewatt_callback)
            view_att.set("Attribution")
            view_att.place(x=36,y=612)

            view_atticon_img = ctk.CTkImage(Image.open("\images\multipage.png"))
            view_atticon = ctk.CTkLabel(rootinfo, image=view_atticon_img, text=None)
            view_atticon.place(x=10,y=611)

            closeimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
            close = ctk.CTkButton(rootinfo, text=None, image=closeimg,
                                  hover_color="red4", fg_color="grey14", corner_radius=
                                  0, width=40, height=40, command=rootinfo.destroy)
            close.place(x=440,y=600)

        elif values == "Credits":
            nextview = ctk.CTkLabel(rootinfo, text=" Updates → ", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            nextview.place(x=365,y=80)

            prevview = ctk.CTkLabel(rootinfo, text=" ← Attribution", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            prevview.place(x=35,y=80)

            banner_au = ctk.CTkLabel(rootinfo, text="  Credits", font=("segoe ui bold", 35),
                                     height=70, width=320, fg_color="deepskyblue4", anchor="w")
            banner_au.place(x=0,y=0)
            banner_au2 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue3", height=70,
                                      width=100)
            banner_au2.place(x=319,y=0)
            banner_au3 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue2", height=70,
                                      width=100)
            banner_au3.place(x=418,y=0)
            
            sillymeimg = ctk.CTkImage(Image.open("\images\sillyme.png"), size=(84,80))
            sillyme = ctk.CTkLabel(rootinfo, image=sillymeimg, text=None)
            sillyme.place(x=20, y=128)

            quotation = "Heyo! I'm Daniel!\nThe developer behind this stupid\ncalculator..."
            qoute = ctk.CTkLabel(rootinfo, text=quotation, font=("Montserrat italic", 18),
                                 anchor="w")
            qoute.place(x=122,y=125)

            sillymallumimg = ctk.CTkImage(Image.open("\images\sillymallum.png"), size=(80,80))
            sillymallum = ctk.CTkLabel(rootinfo, image=sillymallumimg, text=None)
            sillymallum.place(x=400, y=200)

            quotation2 = "I helped daniel tren with modifying\n and improving his cheeky calculator..."
            quote2 = ctk.CTkLabel(rootinfo, text=quotation2, font=("Montserrat italic", 18),
                                  anchor="e")
            quote2.place(x=30,y=215)
            desc_au = """Non-examative Assessment
OCR - H446 Specification
A-Level Computer Science

[Developer] → Daniel Chen
The main programmer behind this calculator

[Feedback Assistant] → Callum Huddlestone
The user feedback lead"""
            text_au = ctk.CTkTextbox(rootinfo, font=("Montserrat medium", 17), height=356, width=490,
                                    fg_color="grey14")
            text_au.place(x=5, y=290)
            text_au.insert("1.0", desc_au)
            text_au.configure(state="disabled")
            closeimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
            close = ctk.CTkButton(rootinfo, text=None, image=closeimg,
                                  hover_color="red4", fg_color="grey14", corner_radius=
                                  0, width=40, height=40, command=rootinfo.destroy)
            close.place(x=440,y=600)
        elif values == "Updates":
            # Update Logs
            def closeinfo():
                fullversion.place_forget()
                reduceinfo.place_forget()
                version.place(x=20,y=350)                
                updateinfo.place(x=20,y=520)
            def displayinfo():
                global fullversion
                global reduceinfo
                version.place_forget()
                updateinfo.place_forget()

                upttext = """v1.0 | Starting a great journey!

CORE RELEASE v1.0! The calculator has succesfully
come out of the BETA Stage!
All things have been succesfully developed, but
expect new QOL updates (with one of them being
a massive update) for further polishing!

Here's what this core release has to offer...

• The 4th, and maybe final? mode!
CONVERSION is now OUT! Convert values of a
measure unit to any desired means!

• We're open to WIDE USER FEEDBACK!
As the calculator has come out of the
BETA stage, we are now looking for 
polishing suggestions! Lookout
for a Google Form!

• Developer Mode adjustments
Debugging modes

• Bug fixes and error handling
Fixed some common issues with the
calculator

• User Interface changes
Some minor UI adjustments

———————————————————————————
                
Update v0.2.3! A Quality Of Life Update!

Hey fellas, this QOL update introduces some new things!

• The 3rd Core mode, GRAPH & TABLE!
Graph your way using equations to visually
represent drawnings thanks to Matplotlib!
Or use the Table to insert x values and substitute
equations!

• Our biggest QOL update yet!
! ! STATISTICS Info added ! ! Made some user directions
towards this as well!

! ! NEW ! ! ERROR HANDLING!!!
Error handling has ARRIVED!!!!! One of our
most significant QOL update yet!
The calculator will now stop doing operations
and respond with an error for calculations that,
well, result in an error!

• Interface adjustments
Tiny interface adjustments (you probably will not
notice this 😊)

———————————————————————————                

Introducing v0.2.0! The ORANGE version!

• This version releases 2nd core\nmode, STATISTICS!
Calculating such means of the mean, the sum and more!

• Improved interface visuals
Grey Textboxes are properly recoloured

• Developer Mode adjustments
Debugging tools + one of Finlay's\nsuggestions

• Information added in the Introduction
Information for CALCULATE has been
added! STATISTICS will be coming soon...

• Minor Bug Fixes
Gotta have them fixed, really..

• Recoloured UI
Based on the feedback we've recieved

---

WARNING! This software is still in 
it's BETA stage; expect bugs, glitches and all
sorts of stuff 
""" 
                fullversion = ctk.CTkTextbox(rootinfo, font=("Montserrat", 17), height=240, width=490,
                                            fg_color="grey14")
                fullversion.place(x=5,y=350)
                fullversion.insert("1.0", upttext)
                fullversion.configure(state="disabled")
                reduceinfo = ctk.CTkButton(rootinfo, text="Close", border_color="white",
                                       fg_color="grey14", corner_radius=18, border_width=1,
                                       font=("segoe ui", 15), hover_color="grey26",
                                       command=closeinfo)
                reduceinfo.place(x=20,y=605)

            nextview = ctk.CTkLabel(rootinfo, text=" Application → ", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            nextview.place(x=365,y=80)

            prevview = ctk.CTkLabel(rootinfo, text=" ← Credits", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            prevview.place(x=35,y=80)

            banner_u = ctk.CTkLabel(rootinfo, text="  Updates", font=("segoe ui bold", 35),
                                     height=70, width=320, fg_color="deepskyblue4", anchor="w")
            banner_u.place(x=0,y=0)
            banner_u2 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue3", height=70,
                                      width=100)
            banner_u2.place(x=319,y=0)
            banner_u3 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue2", height=70,
                                      width=100)
            banner_u3.place(x=418,y=0)

            versioniconimg = ctk.CTkImage(Image.open("/images/1.0.png"), size=(170,170))
            versionicon = ctk.CTkLabel(rootinfo, text=None, font=("segoe ui bold", 65),
                                   image=versioniconimg)
            versionicon.place(x=20, y=140)

            status = ctk.CTkLabel(rootinfo, text="Version up to date!",
                                  font=("Montserrat bold", 35))
            status.place(x=20, y=300)

            versiontext = """v1.0 | Windows 11 | CORE RELEASE
            
The calculator has been FULLY RELEASED!
Finishing off with the new CONVERSION Mode!
We're not done yet though... Expect more
QOL updates on the way, with one MASSIVE
update!"""
            version = ctk.CTkLabel(rootinfo, text=versiontext, font=("Montserrat", 16),
                                   text_color="grey50", justify="left")
            version.place(x=20,y=350)
            version.configure(state="disabled")

            updateinfo = ctk.CTkButton(rootinfo, text="About this Version", border_color="white",
                                       fg_color="grey14", corner_radius=18, border_width=1,
                                       font=("segoe ui", 15), hover_color="grey26",
                                       command=displayinfo)
            updateinfo.place(x=20,y=520)
            
            closeimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
            close = ctk.CTkButton(rootinfo, text=None, image=closeimg,
                                  hover_color="red4", fg_color="grey14", corner_radius=
                                  0, width=40, height=40, command=rootinfo.destroy)
            close.place(x=440,y=600)
        elif values == "Application":
            # General summary of the program
            def devdisable():
                rootinfo.destroy()
                choice = messagebox.askokcancel("Developer Console",("Disabling Developer Mode will require software shutdown"))
                if choice:
                    root.destroy()
                else:
                    information()
            
            prevview = ctk.CTkLabel(rootinfo, text=" ← Updates", font=("Montserrat italic", 13),
                                    fg_color="grey12", corner_radius=6)
            prevview.place(x=35,y=80)

            banner_ap = ctk.CTkLabel(rootinfo, text="  Application", font=("segoe ui bold", 35),
                                     height=70, width=320, fg_color="deepskyblue4", anchor="w")
            banner_ap.place(x=0,y=0)
            banner_ap2 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue3", height=70,
                                      width=100)
            banner_ap2.place(x=319,y=0)
            banner_ap3 = ctk.CTkLabel(rootinfo, text=None, fg_color="deepskyblue2", height=70,
                                      width=100)
            banner_ap3.place(x=418,y=0)

            appiconimg = ctk.CTkImage(Image.open("\images\windowicon.png"), size=(150,150))
            appicon = ctk.CTkLabel(rootinfo, image=appiconimg, text=None)
            appicon.place(x=174,y=200)

            apptitle = ctk.CTkLabel(rootinfo, text="Calculator", font=("Montserrat bold", 50))
            apptitle.place(x=120,y=340)

            appdetails = ctk.CTkLabel(rootinfo, text="v1.0 |  Windows 11", font=("Montserrat", 21))
            appdetails.place(x=152,y=405)

            label = ctk.CTkLabel(rootinfo, text="Software ID: ", font=("segoe ui", 16),
                                 text_color="grey50", justify="right")
            label.place(x=185,y=620)

            softwareid = ctk.CTkLabel(rootinfo, text=idnum, font=("segoe ui", 16),
                                         text_color="grey50", justify="left")
            softwareid.place(x=275,y=620)
            
            if developermode == 1:
                softwareid.place(x=275,y=570)
                label.place(x=185,y=570)

                devoff = ctk.CTkButton(rootinfo, text="Disable Developer Mode",
                                       font=("segoe ui bold", 15), fg_color="red4", corner_radius=18,
                                       hover_color="brown4", command=devdisable)
                devoff.place(x=149,y=540)
        
        if developermode == 1:
            warnarea = ctk.CTkLabel(rootinfo, text="", fg_color="saddle brown",
                                    height=50, width=700)
            warnarea.place(x=0,y=600)
            
            warn = ctk.CTkLabel(rootinfo, text="            Developer Mode is enabled",
                                font=("segoe ui bold",15), fg_color="saddle brown",
                                height=50)
            warn.place(x=0,y=600)                
            
            warniconimg = ctk.CTkImage(Image.open("\images\warning.png"), size=(30,30))
            warnicon = ctk.CTkLabel(rootinfo, text=None, image=warniconimg,
                                    fg_color="saddle brown", height=20)
            warnicon.place(x=10,y=610)

                                                     # ↓ ↓ ↓ All the available options through an option menu
    
    viewoptions = ctk.CTkOptionMenu(rootinfo, values=["Introduction", "Attribution", "Credits", "Updates",
                                                      "Application"],
                                    command=lambda value: viewoptions_callback(value, viewoptions),
                                    fg_color="deepskyblue4", font=("segoe ui bold", 16),
                                    button_color="grey14", dropdown_fg_color="grey12",
                                    dropdown_font=("Montserrat italic", 13), dropdown_hover_color="deepskyblue4")
    viewoptions.set("Introduction") # Default option
    viewoptions_callback("Introduction", viewoptions) # Default view of option  
    viewoptions.place(x=180,y=80)

    rootinfo.attributes("-topmost", True)

# Keyboard Shortcuts ---

    root.focus_get()
 


# [CALCULATE] -------



# Functions ---

x = 0
y = 0
# Converts to what the program can understand
c_functions = { # Dictionary to swap something to this
"π" : math.pi, # i.e., pi is swapped to math.pi
"el" : math.e,
"sqrt" : math.sqrt,
"sin" : math.sin,
"cos" : math.cos,
"tan" : math.tan,
"isin" : math.asin,
"icos" : math.acos,
"itan" : math.atan,
"ln" : math.log,
"log" : math.log10,
"clog" : math.log,
"factorial" : math.factorial
}

def evaluate_c(): # Converts to what the program can understand
    global answer
    if solve == "√•(420,•69)": # Easter egg from Jacob's "Skibidi Code"
        messagebox.showwarning("Developer Console",("[WARNING] Developer mode is on!"))
        confirm = messagebox.askyesno("Developer Console",("""[Operation SQRT]
You are about to perform an operation that involves developer use only!
Are you sure you want to proceed further with this?
[YES] -> I know what I'm doing
[NO] -> Deactivate Developer Mode and solve √•(420,•69)"""))
        if confirm:
            confirm2 = messagebox.askyesno("Developer Console",("""[Operation SQRT]
Are you absolutely sure? By proceeding, you understand that this is used for developer use only and will be responsible for any outcomes.
Developer Mode cannot be disabled until the program is closed.
[YES] -> Activate this operation
[NO] -> Abort and deactivate Developer Mode"""))
            if confirm2:
                print("active")
                answer = 1.0914858393463176
                external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
                res = DbIpCity.get(external_ip, api_key="free")
                ipadd = f"• IP Address: {res.ip_address}"
                locate = f"• Location:\n{res.city},\n{res.region},\n{res.country}"
                coord = f"• Coordinates:\nLat:\n{res.latitude},\nLng:\n{res.longitude}"
                nbicon.place_forget()
                mininb.configure(state="normal")
                mininb.insert(index=(1.0), text=ipadd + "\n")
                mininb.insert(index=(1.0), text=locate + "\n")
                mininb.insert(index=(1.0), text=coord + "\n")
                mininb.configure(state="disabled")
                clearnbimg = ctk.CTkImage(Image.open("\images\clearnb_disabled.png"))
                clearnb = ctk.CTkButton(calculate, image=clearnbimg, # disables clear notebook
                        height=40, width=40, text=None, command=lambda: messagebox.showerror("Developer Console",("[Operation SQRT] Error: Developer Mode is on!")),
                        fg_color="grey12", hover_color="grey12", corner_radius=0)
                clearnb.place(x=708, y=208)
                execute_c.place_forget()
                zero_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=178, text_color="white", text="0",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "0"),
                    hover_color="grey19")           
                zero_c.place(x=220,y=330)     
                messagebox.showwarning("Developer Console",("[Operation SQRT] Active"))
                global developermode
                developermode = 1
            else:
                answer = 1.0914858393463176
        else:
            answer = 1.0914858393463176

    else:
        solve_step1 = re.sub(r"(\d+)!", lambda x: f"factorial({x.group(1)})", solve) # !
        solve_step2 = solve_step1.replace("e","el")
        solve_step3 = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", solve_step2) # x, y and e
        solve_step4 = solve_step3.replace("√(", "sqrt(") # √
        solve_step5 = solve_step4.replace("sin⁻¹", "isin") # ---
        solve_step6 = solve_step5.replace("cos⁻¹", "icos") # Inverse Trig
        solve_step7 = solve_step6.replace("tan⁻¹", "itan") # ---
        solve_step8 = solve_step7.replace("×", "*") # ×  
        solve_step9 = solve_step8.replace("^","**") # ^
        solve_step10 = solve_step9.replace("log•","clog") # log
        solve_step11 = solve_step10.replace("√•(","") #     n√
        solve_step12 = solve_step11.replace(",•","**(1/")#  |   

        if solve_step11 == "": # If there's nothing in the input, 
            answer = ""        # the program will do nothing
            return
        
        # ---
        pastinput.configure(state="normal")
        try: # Solving and error handling
            answer = eval(solve_step12, {**globals(), **c_functions}, locals())
            inputoutput.delete(0, ctk.END)
            inputoutput.insert(0, str(answer))
            pastinput.insert(index=(1.0), text=solve)
            pastinput.configure(state="disabled")

        except SyntaxError: # Syntax error (i.e. "sin(+)")
            messagebox.showerror("Error",("""[Syntax ERROR]
The calculator couldn't process your mathematical expression! Try:
• Checking if operators are correctly used
• No blank feilds are left out"""))
            pastinput.insert(index=(1.0), text="⚠ Syntax ERROR")
            pastinput.configure(state="disabled")
        
        except ZeroDivisionError: # Division by zero (i.e. 32423/0)
            messagebox.showerror("Error",("""[Math ERROR]
You are attempting to perform an illegal mathematical operation! Try:
• Not dividing something by 0 😊👌"""))
            pastinput.insert(index=(1.0), text="⚠ Math ERROR")
            pastinput.configure(state="disabled")

        except OverflowError: # Python's overflow error
            messagebox.showerror("Error",("""[Math ERROR]
The calculator recieved a very large result, in which it can't handle! Try:
• Shortening down the mathematical expression"""))
            pastinput.insert(index=(1.0), text="⚠ Math ERROR")
            pastinput.configure(state="disabled")

        except NameError: # Syntax error for extranous data (i.e. 4+fg)
            messagebox.showerror("Error",("""[Syntax ERROR]
The calculator recieved extranous data! Try:
• Removing extranous data
• Using x instead
• Using y instead"""))
            pastinput.insert(index=(1.0), text="⚠ Syntax ERROR")
            pastinput.configure(state="disabled")

        except: # For every other error
            messagebox.showerror("Error", ("""[Syntax ERROR]
The calculator couldn't process your mathematical expression!
• Check error logs"""))
            pastinput.insert(index=(1.0), text="⚠ Other ERROR")
            pastinput.configure(state="disabled")


# Functions ---

def clearall_nb(): # Clears notebook
    nbprompt = messagebox.askyesno("Clear Notebook?",("Erase all contents in your Notebook?"))
    
    if nbprompt:
        mininb.configure(state="normal")
        mininb.delete("1.0", ctk.END)
        mininb.configure(state="disabled")
    nbicon.place(x=566,y=130)

def clearall(): # Clears everything (except notebook)
    inputoutput.delete(0, ctk.END)
    pastinput.configure(state="normal")
    pastinput.delete("1.0", ctk.END)
    pastinput.configure(state="disabled")

def store(): # Stores the CALCULATE value in the notebook
    answer = 0
    answer = inputoutput.get()
    
    if answer == "":
        return

    mininb.configure(state="normal")
    mininb.insert(index=(1.0), text=answer+"\n")
    mininb.configure(state="disabled")
    nbicon.place_forget()

def backspace_c(): # Deletes a value
    expression = inputoutput.get()
    inputoutput.delete(len(expression)-1, ctk.END)

def editvariable(): # Edit the x and y variables
    global xentry
    global yentry
    global rootxy
    try:
        if rootxy.winfo_exists():
            return
    except:
        pass

    def confirmvar():
        xdata = xentry.get("1.0","end")
        ydata = yentry.get("1.0","end")
        global x
        global y
        x = float(xdata)
        y = float(ydata)
        rootxy.destroy()
    def clearvar():
        xentry.delete("1.0", ctk.END)
        yentry.delete("1.0", ctk.END)
    
    rootxy = ctk.CTkToplevel()
    rootxy.geometry("550x130+250+385")
    rootxy.title("Edit Variables")
    rootxy.resizable(0,0)

    xlabel = ctk.CTkLabel(rootxy, font=("STIX Two Text italic", 25), text="x =")
    xlabel.place(x=3, y=23)
    xentry = ctk.CTkTextbox(rootxy, font=("segoe ui", 21), height=15,
                          width=450, fg_color="white", text_color="black")
    xentry.place(x=45, y=20) # Entry for x
    xentry.insert("1.0", text=x)

    ylabel = ctk.CTkLabel(rootxy, font=("STIX Two Text italic", 25), text="y =")
    ylabel.place(x=3, y=73)
    yentry = ctk.CTkTextbox(rootxy, font=("segoe ui", 21), height=15,
                          width=450, fg_color="white", text_color="black")
    yentry.place(x=45, y=70) # Entry for y
    yentry.insert("1.0", text=y)

    xpasteimg = ctk.CTkImage(Image.open("\images\paste.png"))
    xpaste = ctk.CTkButton(rootxy, text=None, image=xpasteimg,
                           width=40, height=40, fg_color="white",
                           hover_color="grey60", command=pasteinx,
                           corner_radius=0, border_width=2, border_color="black")
    xpaste.place(x=450,y=22) # Pastes the CALCULATE value into x

    ypasteimg = ctk.CTkImage(Image.open("\images\paste.png"))
    ypaste = ctk.CTkButton(rootxy, text=None, image=ypasteimg,
                           width=40, height=40, fg_color="white",
                           hover_color="grey60", command=pasteiny,
                           corner_radius=0, border_width=2, border_color="black")
    ypaste.place(x=450,y=73) # Pastes the CALCULATE value into y

    confirmcancelarea = ctk.CTkLabel(rootxy, text=None, height=120,
                                     width=100, fg_color="grey12",
                                     corner_radius=8)
    confirmcancelarea.place(x=505,y=5.5)

    canceleditsimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
    canceledits = ctk.CTkButton(rootxy, text=None, image=canceleditsimg,
                                width=40, height=40, fg_color="grey12",
                                hover_color="red4", command=rootxy.destroy,
                                corner_radius=0)
    canceledits.place(x=508, y=82) # Cancels edits

    confirmeditsimg = ctk.CTkImage(Image.open("\images\ctick.png"))
    confirmedits = ctk.CTkButton(rootxy, text=None, image=confirmeditsimg,
                                 width=40, height=40, fg_color="grey12",
                                 hover_color="grey26", command=confirmvar,
                                 corner_radius=0)
    confirmedits.place(x=508,y=44) # Confirms edits

    eraseeditsimg = ctk.CTkImage(Image.open("\images\clear_wh.png"))
    eraseedits = ctk.CTkButton(rootxy, text=None, image=eraseeditsimg,
                                 width=40, height=40, fg_color="grey12",
                                 hover_color="grey26", command=clearvar,
                                 corner_radius=0)
    eraseedits.place(x=508,y=6) # Clears x and y entries

    rootxy.attributes("-topmost", True) # <-- this is to keep the window ontop of the main
                                        # calculator window

def execute(): # Function to process and output the answer
    global solve # to the mathematical expression
    global answer
    pastinput.configure(state="normal")
    pastinput.delete("1.0", ctk.END)
    pastinput.configure(state="disabled")
    answer = 0
    solve = inputoutput.get()
    evaluate_c() # Converted to the expression
               # that allows Python to understand

def insertsqrt(): # Inserting a square root with a custom index number
    global index
    global rootsqrt
    try:
        if rootsqrt.winfo_exists():
            return
    except:
        pass
    def pasteinindex(): # Pasting the answer value into the index value
        paste = inputoutput.get()
        indexinput.delete(0, ctk.END)
        indexinput.insert(0, str(paste))

    def pasteinvalue(): # Pasting the answer value into tne value
        paste = inputoutput.get()
        valueinput.delete(0, ctk.END)
        valueinput.insert(0, str(paste))

    def confirmsqrt(): # Inserts the n-th root of...
        global index
        index = indexinput.get()
        value = valueinput.get()
        insert = "√•(" + value + ",•" + index + ")"
        inputoutput.insert(ctk.INSERT, str(insert))
        rootsqrt.destroy()

    rootsqrt = ctk.CTkToplevel()
    rootsqrt.geometry("345x200+1020+40")
    rootsqrt.title("Insert Square Root")
    rootsqrt.resizable(0,0)

    miscbox_t = ctk.CTkLabel(rootsqrt, # an area for misc buttons
                            height=88, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_t.place(x=300,y=101)

    closewindow = ctk.CTkButton(rootsqrt, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootsqrt.destroy)
    closewindow.place(x=303,y=145)

    confirminsertimg = ctk.CTkImage(Image.open("\images\ctick.png"))
    confirminsert = ctk.CTkButton(rootsqrt, image=confirminsertimg, text=None,
                                  fg_color="grey12", hover_color="grey26",
                                  corner_radius=0, width=40, height=40, command=confirmsqrt)
    confirminsert.place(x=303, y=105)
    
    # ---

    sqrticonimg = ctk.CTkImage(Image.open("\images\sqrt_boxless.png"), size=(200,100))
    sqrticon = ctk.CTkLabel(rootsqrt, text=None, image=sqrticonimg)
    sqrticon.place(x=45,y=45)

    valueinput = ctk.CTkEntry(rootsqrt, font=("segoe ui", 30), border_width=0,
                         width=120, height=80, fg_color="white", text_color="black")
    valueinput.place(x=117,y=65) # Value input

    indexinput = ctk.CTkEntry(rootsqrt, font=("segoe ui", 18), border_width=0,
                         width=45, height=40, fg_color="white", text_color="black")
    indexinput.place(x=52, y=50) # Index input

    valuepasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    valuepaste = ctk.CTkButton(rootsqrt, image=valuepasteimg, fg_color="grey14",
                              hover_color="grey26", text=None, width=40, height=40,
                              corner_radius=0, command=pasteinvalue)
    valuepaste.place(x=237,y=85)

    indexpasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    indexpaste = ctk.CTkButton(rootsqrt, image=indexpasteimg, fg_color="grey14",
                              hover_color="grey26", text=None, width=40, height=40,
                              corner_radius=0, command=pasteinindex)
    indexpaste.place(x=11,y=50)
    
def insertlog(): # Inserting a logarithm with a custom base number
    global rootlog
    try:
        if rootlog.winfo_exists():
            return
    except:
        pass
    
    def pasteinbase(): # Pasting the answer value into the base
        paste = inputoutput.get() #               number of log
        baseinput.delete(0, ctk.END)
        baseinput.insert(0, str(paste))

    def pasteinvalue(): # Pasting the answer value into the value
        paste = inputoutput.get()
        valueinput.delete("1.0", ctk.END)
        valueinput.insert(index=(1.0), text=paste)

    def confirmlog(): # Inserts the logarithm
        base = baseinput.get()
        value = valueinput.get()
        insert = "log•(" + value + "," + base + ")"
        inputoutput.insert(ctk.INSERT, str(insert))
        rootlog.destroy()
    
    rootlog = ctk.CTkToplevel()
    rootlog.geometry("345x200+1020+40")
    rootlog.title("Insert Logarithm")
    rootlog.resizable(0,0)

    miscbox_t = ctk.CTkLabel(rootlog, # an area for misc buttons
                            height=88, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_t.place(x=300,y=101)

    closewindow = ctk.CTkButton(rootlog, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootlog.destroy)
    closewindow.place(x=303,y=145) 

    confirminsertimg = ctk.CTkImage(Image.open("\images\ctick.png"))
    confirminsert = ctk.CTkButton(rootlog, image=confirminsertimg, text=None,
                                  fg_color="grey12", hover_color="grey26",
                                  corner_radius=0, width=40, height=40, command=confirmlog)
    confirminsert.place(x=303, y=105)

    # ---

    loglabel = ctk.CTkLabel(rootlog, text="Log", font=("segoe ui", 80))
    loglabel.place(x=20,y=20)

    baseinput = ctk.CTkEntry(rootlog, font=("segeo ui", 18), text_color="black",
                             fg_color="white", width=50, height=40, border_width=0)
    baseinput.place(x=150,y=100) # Base number input

    valueinput = ctk.CTkEntry(rootlog, font=("segeo ui", 20), text_color="black",
                             fg_color="white", width=80, height=70, border_width=0)
    valueinput.place(x=205,y=50) # Value number input

    basepasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    basepaste = ctk.CTkButton(rootlog, image=basepasteimg, fg_color="grey14",
                              hover_color="grey26", text=None, width=40, height=40,
                              corner_radius=0, command=pasteinbase)
    basepaste.place(x=155.5,y=140) # Base pasting

    valuepasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    valuepaste = ctk.CTkButton(rootlog, image=valuepasteimg, fg_color="grey14",
                              hover_color="grey26", text=None, width=40, height=40,
                              corner_radius=0, command=pasteinvalue)
    valuepaste.place(x=225.5,y=120) # Value pasting

def misc_c():
    global close_windowimg
    miscbox_c = ctk.CTkLabel(calculate, # an area for misc buttons
                            height=167.5, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=705,y=205)

    close_windowimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
    close_window_c = ctk.CTkButton(calculate, height=40, width=40, text=None,
                                 fg_color="grey12", image=close_windowimg, command=shutdown,
                                 hover_color="red4", corner_radius=0)
    close_window_c.place(x=708,y=328) # Close window

    infoimg = ctk.CTkImage(Image.open("\images\info.png"))
    info = ctk.CTkButton(calculate, image=infoimg,
                         height=40, width=40, text=None, corner_radius=0,
                         fg_color="grey12", hover_color="grey26", command=information)
    info.place(x=708, y=288) # Help & Info

    xyimg = ctk.CTkImage(Image.open("\images\cvariables.png"))
    xy_c = ctk.CTkButton(calculate, image=xyimg,
                       height=40, width=40, text=None, command=editvariable,
                       fg_color="grey12", hover_color="grey26", corner_radius=0)
    xy_c.place(x=708,y=248) # Edit x and y variables
misc_c()

# ---

clearnbimg = ctk.CTkImage(Image.open("\images\clearnb.png"))
clearnb = ctk.CTkButton(calculate, image=clearnbimg, # clears the notebook
                        height=40, width=40, text=None, command=clearall_nb,
                        fg_color="grey12", hover_color="grey26", corner_radius=0)
clearnb.place(x=708, y=208)

inputoutput = ctk.CTkEntry(calculate, # input/output mathematical expressions
                            height=80, width=415, font=("Noto Sans Math", 40),
                            fg_color="grey14", border_color="grey14")
inputoutput.place(x=2,y=5)

pastinput = ctk.CTkTextbox(calculate, # answer to mathematical expression
                           height=33, width=415, font=("Montserrat bold", 16),
                           fg_color="grey14", text_color="gray65", corner_radius=0,
                           state="disabled")
pastinput.place(x=2, y=72)

buttonbox = ctk.CTkButton(calculate, # an area for the buttons
                          height=262, width=525, text="",
                          fg_color="grey14", border_color=None, hover_color="grey14")
buttonbox.place(x=2,y=110)

clear_cimg = ctk.CTkImage(Image.open("\images\clear.png"))
clear_c = ctk.CTkButton(calculate, image=clear_cimg, # [B] Clear button
                        height=48, width=52, text_color="red", text=None,
                        fg_color="grey14", border_color="red2", hover_color="red4",
                        border_width=2, command=clearall)  
clear_c.place(x=422,y=5)

storenbimg = ctk.CTkImage(Image.open("\images\storenb.png"))
storenb = ctk.CTkButton(calculate, # [B] Insert Ans. into textbook button
                        height=48, width=52, text_color="goldenrod1", image=storenbimg,
                        fg_color="grey14", border_color="goldenrod1", hover_color="goldenrod4",
                        border_width=2, text=None, command=store)  
storenb.place(x=478,y=5)

bksp_imgc = ctk.CTkImage(Image.open("\images\down.png"))
bksp_c = ctk.CTkButton(calculate, # [B] Backspace Button
                       height=48, width=108, text="", image=bksp_imgc,
                       fg_color="grey19", hover_color="red4", command=backspace_c)
bksp_c.place(x=422,y=57)

mininb = ctk.CTkTextbox(calculate, font=("Montserrat", 15), # an area for user note taking
                        height=366, width=165, text_color="black",
                        fg_color="goldenrod1", state="disabled")
mininb.place(x=535,y=5)

iconimg = ctk.CTkImage(Image.open("\images\cnotestack.png"), size=(100,100))
nbicon = ctk.CTkLabel(calculate, image=iconimg, text=None,
                      fg_color="goldenrod1", corner_radius=0)
nbicon.place(x=566,y=130)

# Num Pad ---

one_c = ctk.CTkButton(calculate, font=("segoe ui", 21), # 1
                    height=37, width=87, text_color="white", text="1",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "1"),
                    hover_color="grey19", bg_color="grey14")
one_c.place(x=130,y=210)

two_c = ctk.CTkButton(calculate, font=("segoe ui", 21), # 2 etc...
                    height=37, width=87, text_color="white", text="2",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "2"),
                    hover_color="grey19", bg_color="grey14")
two_c.place(x=220,y=210)

three_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="3",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "3"),
                    hover_color="grey19", bg_color="grey14")
three_c.place(x=310,y=210)

# etc..

four_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="4",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "4"),
                    hover_color="grey19", bg_color="grey14")
four_c.place(x=130,y=250)

five_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="5",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "5"),
                    hover_color="grey19", bg_color="grey14")
five_c.place(x=220,y=250)

six_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="6",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "6"),
                    hover_color="grey19", bg_color="grey14")
six_c.place(x=310,y=250)

seven_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="7",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "7"),
                    hover_color="grey19", bg_color="grey14")
seven_c.place(x=130,y=290)

eight_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="8",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "8"),
                    hover_color="grey19", bg_color="grey14")
eight_c.place(x=220,y=290)

nine_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="9",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "9"),
                    hover_color="grey19", bg_color="grey14")
nine_c.place(x=310,y=290)

zero_c = ctk.CTkButton(calculate, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="0",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "0"),
                    hover_color="grey19", bg_color="grey14")
zero_c.place(x=220,y=330)

dec_c = ctk.CTkButton(calculate, font=("segoe ui", 21), # decimal
                    height=37, width=87, text_color="white", text=".",
                    fg_color="grey26", command=lambda: inputoutput.insert(ctk.INSERT, "."),
                    hover_color="grey19", bg_color="grey14")
dec_c.place(x=130,y=330)

execute_cimg = ctk.CTkImage(Image.open("\images\equalsign.png"))
execute_c = ctk.CTkButton(calculate, # button to execute mathematical equation
                    height=37, width=87, text=None,
                    image=execute_cimg, bg_color="grey14",
                    fg_color="deepskyblue4", command=execute)
execute_c.place(x=310,y=330)

# Left buttons ---

x_variable = ctk.CTkButton(calculate, font=("STIX Two Text italic", 21), # x
                           height=50, width=58, text_color="white", text="x",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "x"),
                            hover_color="grey26", bg_color="grey14")
x_variable.place(x=7,y=317)

y_variable = ctk.CTkButton(calculate, font=("STIX Two Text italic", 21), # y
                           height=50, width=58, text_color="white", text="y",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "y"),
                           hover_color="grey26", bg_color="grey14")
y_variable.place(x=69,y=317)

close_brak = ctk.CTkButton(calculate, font=("segoe ui", 21), # )
                           height=50, width=58, text_color="white", text=")",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, ")"),
                           hover_color="grey26", bg_color="grey14")
close_brak.place(x=69,y=263)

open_brak = ctk.CTkButton(calculate, font=("segoe ui", 21), # (
                           height=50, width=58, text_color="white", text="(",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "("),
                           hover_color="grey26", bg_color="grey14")
open_brak.place(x=7,y=263)

factorial = ctk.CTkButton(calculate, font=("segoe ui", 21), # !
                           height=50, width=58, text_color="white", text="!",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "!"),
                           hover_color="grey26", bg_color="grey14")
factorial.place(x=7,y=209)

power_n_img = ctk.CTkImage(Image.open("\images\sqaren.png"), size=(30,30))
power_n = ctk.CTkButton(calculate, image=power_n_img, # ^...
                           height=50, width=58, text_color="white", text="",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "^"),
                           hover_color="grey26", bg_color="grey14")
power_n.place(x=69,y=209)

# Right Buttons ---

multiply = ctk.CTkButton(calculate, font=("segoe ui", 24), # *
                           height=50, width=58, text_color="white", text="×",
                           fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "×"),
                           hover_color="grey26", bg_color="grey14")
multiply.place(x=401,y=317)

divide = ctk.CTkButton(calculate, font=("segoe ui", 24), # /
                       height=50, width=58, text_color="white", text="÷",
                       fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "/"),
                           hover_color="grey26", bg_color="grey14")
divide.place(x=463,y=317)

add = ctk.CTkButton(calculate, font=("segoe ui", 24), # +
                       height=50, width=58, text_color="white", text="+",
                       fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "+"),
                       hover_color="grey26", bg_color="grey14")
add.place(x=401,y=263)

subtract = ctk.CTkButton(calculate, font=("segoe ui", 24), # -
                       height=50, width=58, text_color="white", text="-",
                       fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "-"),
                           hover_color="grey26", bg_color="grey14")
subtract.place(x=463,y=263)
                                      # Image path
fractionimg = ctk.CTkImage(Image.open("\images\cfraction.png"), size=(22,32))
# ↑ ↑ ↑ Using the pillow library, we define a variable with an image

                                    # ↓ ↓ ↓ "fractionimg" is then implemented into the widget
fraction = ctk.CTkButton(calculate, image=fractionimg, # .../...
                       height=50, width=58, text=None,
                       fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "(/)"),
                           hover_color="grey26", bg_color="grey14")
fraction.place(x=401,y=209)

sqrtimg = ctk.CTkImage(Image.open("\images\sqrt.png"), size=(30,30))
sqrt = ctk.CTkButton(calculate, image=sqrtimg, # √ 
                       height=50, width=58, text=None,
                       fg_color="grey19", hover_color="grey26", command=lambda:
                       inputoutput.insert(ctk.INSERT, "√("), bg_color="grey14")
sqrt.place(x=463,y=209)

# Top Functions ---

sin = ctk.CTkButton(calculate, font=("segoe ui", 18), # trigonometry..
                    height=43, width=81, text_color="white", text="Sin",
                    fg_color="grey19", hover_color="grey26", command=lambda: 
                    inputoutput.insert(ctk.INSERT, "sin("), bg_color="grey14")
sin.place(x=7,y=115)

cos = ctk.CTkButton(calculate, font=("segoe ui", 18),
                    height=43, width=81, text_color="white", text="Cos",
                    fg_color="grey19", hover_color="grey26", command=lambda: 
                    inputoutput.insert(ctk.INSERT, "cos("), bg_color="grey14")
cos.place(x=92,y=115)

tan = ctk.CTkButton(calculate, font=("segoe ui", 18),
                    height=43, width=81, text_color="white", text="Tan",
                    fg_color="grey19", hover_color="grey26", command=lambda: 
                    inputoutput.insert(ctk.INSERT, "tan("), bg_color="grey14")
tan.place(x=177,y=115)

log = ctk.CTkButton(calculate, font=("segoe ui", 18), # logarithms
                    height=43, width=81, text_color="white", text="Log",
                    fg_color="grey19", hover_color="grey26", command=lambda:
                    inputoutput.insert(ctk.INSERT, "log("), bg_color="grey14")
log.place(x=271,y=115)

n_sqrtimg = ctk.CTkImage(Image.open("\images\cnsqrt.png"), size=(30,25))
n_sqrt = ctk.CTkButton(calculate, image=n_sqrtimg, # n√
                    height=43, width=81, text=None, bg_color="grey14",
                    fg_color="grey19", hover_color="grey26", command=insertsqrt)
n_sqrt.place(x=356,y=115)

pi_c = ctk.CTkButton(calculate, font=("STIX Two Text", 23), # 3.14...
                    height=43, width=81, text_color="white", text="π",
                    fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "π"), 
                    hover_color="grey26", bg_color="grey14")
pi_c.place(x=441,y=115)

inv_sin = ctk.CTkButton(calculate, font=("segoe ui", 18), # inv sin
                    height=43, width=81, text_color="white", text="Sin⁻¹",
                    fg_color="grey19", hover_color="grey26", command=lambda: 
                    inputoutput.insert(ctk.INSERT, "sin⁻¹("), bg_color="grey14")
inv_sin.place(x=7,y=162)

inv_cos = ctk.CTkButton(calculate, font=("segoe ui", 18), # inv cos
                    height=43, width=81, text_color="white", text="Cos⁻¹",
                    fg_color="grey19", hover_color="grey26", command=lambda: 
                    inputoutput.insert(ctk.INSERT, "cos⁻¹("), bg_color="grey14")
inv_cos.place(x=92,y=162)

inv_tan = ctk.CTkButton(calculate, font=("segoe ui", 18), # inv tan
                    height=43, width=81, text_color="white", text="Tan⁻¹",
                    fg_color="grey19", hover_color="grey26", command=lambda: 
                    inputoutput.insert(ctk.INSERT, "tan⁻¹("), bg_color="grey14")
inv_tan.place(x=177,y=162)

ln = ctk.CTkButton(calculate, font=("segoe ui", 18), # natural logarithm
                    height=43, width=81, text_color="white", text="Ln",
                    fg_color="grey19", hover_color="grey26", command=lambda:
                    inputoutput.insert(ctk.INSERT, "ln("), bg_color="grey14")
ln.place(x=271,y=162)

log_n_img = ctk.CTkImage(Image.open("\images\logbasen.png"), size=(58,25)) # custom base logarithm
log_n = ctk.CTkButton(calculate, image=log_n_img, text=None, font=("segoe ui", 18),
                    height=43, width=81, text_color="white", bg_color="grey14",
                    fg_color="grey19", hover_color="grey26", command=insertlog)
log_n.place(x=356,y=162)

e_c = ctk.CTkButton(calculate, font=("STIX Two Text", 20), # 2.71...
                    height=43, width=81, text_color="white", text="e",
                    fg_color="grey19", command=lambda: inputoutput.insert(ctk.INSERT, "e"), 
                    hover_color="grey26", bg_color="grey14")
e_c.place(x=441,y=162)



# [STATISTICS] -------



# These are just banners - user interface cosmetic
banner_s = ctk.CTkLabel(stat, text="  Statistics", font=("segoe ui bold", 35),
                         height=70, width=420, fg_color="deepskyblue4", anchor="w")
banner_s.place(x=0,y=0)
banner_s2 = ctk.CTkLabel(stat, text=None, fg_color="deepskyblue3", height=70,
                          width=160)
banner_s2.place(x=419,y=0)
banner_s3 = ctk.CTkLabel(stat, text=None, fg_color="deepskyblue2", height=70,
                          width=160)
banner_s3.place(x=578,y=0)

x_array = [] # The x data
y_array = [] # The y data
def evaluate_s():
    if x_array: # Checks if the arrays have any values or not
        pass
    else:
        messagebox.showerror("Error",("""[Array ERROR]
There is no data entered"""))
        return # ← This stops the function
        
    # ---
    
    rootstat = ctk.CTkToplevel() # Opens a new window for the results
    rootstat.geometry("500x420+1020+40")
    rootstat.title("Results")
    rootstat.resizable(0,0)

    miscbox_c = ctk.CTkLabel(rootstat, # an area for misc buttons
                            height=49, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=455,y=362)

    closewindow = ctk.CTkButton(rootstat, image=close_windowimg,
                            height=40, width=40, text=None, # Closes the results window
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootstat.destroy)
    closewindow.place(x=458,y=367)
    
    # ---

    # Below is where are all the calculations are performed.
    global mode
    try: # Checks if there is any mode in x_array
        xmode = statistics.mode(x_array)
    except statistics.StatisticsError:
        xmode = "N/A"
    
    xsum_array = [sumx**2 for sumx in x_array]#
    try:
        xtext = (
        "Σx = " + str(sum(x_array)) + "\n"
        "Σx² = " + str(sum(xsum_array)) + "\n"
        "nx = " + str(len(x_array)) + "\n"
        "sx = " + str(statistics.stdev(x_array)) + "\n"
        "s²x = " + str(statistics.variance(x_array)) + "\n"
        "σx = " + str(statistics.pstdev(x_array)) + "\n"
        "σ²x = " + str(statistics.pvariance(x_array)) + "\n"
        "x̄ = " + str(statistics.mean(x_array)) + "\n"
        "x Mode = " + str(xmode) + "\n"
        "x Median = " + str(statistics.median(x_array)) + "\n"
        "x Range = " + str((max(x_array) - min(x_array))) + "\n"
        "x Max = " + str(max(x_array)) + "\n"
        "x Min = " + str(min(x_array)) + "\n"
        )
        
        if stat_setting == 2 or stat_setting == 3: # When 2var or both are enabled
            try: # Checks if there is any mode in y_array
                ymode = statistics.mode(y_array)
            except statistics.StatisticsError:
                ymode = "N/A"
            
            ysum_array = [sumy**2 for sumy in x_array]
            ytext = (
            "Σy = " + str(sum(y_array)) + "\n"
            "Σx² = " + str(sum(ysum_array)) + "\n"
            "ny = " + str(len(y_array)) + "\n"
            "sy = " + str(statistics.stdev(y_array)) + "\n"
            "s²y = " + str(statistics.variance(y_array)) + "\n"
            "σy = " + str(statistics.pstdev(y_array)) + "\n"
            "σ²y = " + str(statistics.pvariance(y_array)) + "\n"
            "ȳ = " + str(statistics.mean(y_array)) + "\n"
            "y Mode = " + str(ymode) + "\n"
            "y Median = " + str(statistics.median(y_array)) + "\n"
            "y Range = " + str((max(y_array) - min(y_array))) + "\n"
            "y Max = " + str(max(y_array)) + "\n"
            "y Min = " + str(min(y_array)) + "\n"
            )
    except statistics.StatisticsError:
        rootstat.destroy()
        messagebox.showerror("Error",("""[Array Error]
There is only one peice of data set. Try:
• Inserting more than 1 data peice"""))
    xresults = ctk.CTkTextbox(rootstat, font=("segoe ui", 17),
                            fg_color="grey14", height=412, width=440)
   
    if stat_setting == 0 or stat_setting == 1: # Results for just x data
        xresults.place(x=5, y=5)
        xresults.insert(index=(1.0), text=xtext)
        xresults.configure(state="disabled")
    
    elif stat_setting == 2 or stat_setting == 3: # Results for x AND y data when 2var or both are enabled
        xresults.place(x=5, y=5)
        xresults.configure(width=210) # Results for x data
        xresults.insert(index=(1.0), text=xtext)
        xresults.configure(state="disabled")
        
        line = ctk.CTkLabel(rootstat, text=None, fg_color="white", height=412, width=1, corner_radius=1)
        line.place(x=222,y=5) # This is just a line

        yresults = ctk.CTkTextbox(rootstat, font=("segoe ui", 17),
                                fg_color="grey14", height=412, width=210)
        yresults.place(x=232,y=5) # Results for y data
        yresults.insert(index=(1.0), text=ytext)
        yresults.configure(state="disabled")

    rootstat.attributes("-topmost", True)

# Stat setting is a variable that detects what setting is enabled
stat_setting = 0

focusbutton = "x"

def errorcheckJL():
    global developermode
    one = xinput_s.get()
    two = yinput_s.get()
    three = freqinput.get()

    # Easter
    # Egg

    if one == "Jonas" and two == "Leeks" and three == "Reels": # Easter egg from Finlay
        messagebox.showwarning("Developer Console",("[WARNING] Developer mode is on!"))
        confirm = messagebox.askyesno("Developer Console",("""[Operation REELS]
You are about to perform an operation that involves developer use only!
Are you sure you want to proceed further with this?
[YES] -> I know what I'm doing
[NO] -> Cancel and return back to normal settings"""))
        if confirm:
            confirm2 = messagebox.askyesno("Developer Console",("""[Operation REELS]
Are you absolutely sure? By proceeding, you understand that this is used for developer use only and will be responsible for any outcomes.
Developer Mode cannot be disabled until the program is closed.
[YES] -> I understand, now activate this operation
[NO] -> Abort and deactivate Developer Mode"""))
            if confirm2:
                root.destroy()
                developermode = 1
                messagebox.showwarning("Developer Console",("[Operation REELS] Active"))
                messagebox.showinfo("?????",("[REDACTED]! [REDACTED][REDACTED]?"))

                reels = ctk.CTk()
                reels.geometry("400x300+600+300")
                reels.title("?????")
                reels.resizable(0,0)

                redactedimg = ctk.CTkImage(Image.open("\images\sigmastaples.jpg"), size=(225,225))
                redacted = ctk.CTkLabel(reels, image=redactedimg, text=None)
                redacted.place(x=90,y=20)

                redacted2 = ctk.CTkLabel(reels, text="[REDACTED]", font=("Sixtyfour Convergence close", 20))
                redacted2.place(x=105,y=250)

                reels.mainloop()
            else:
                pass
        
        else:
            pass

    else:
        pass
                
def opennumpad_s(): # Number pad
    errorcheckJL()
    if developermode == 1:
        return
    
    global select
    global focusoption
    global focustyping
    global rootnum
    global focus
    try:
        if rootnum.winfo_exists():
            return
    except:
        pass
    rootnum = ctk.CTkToplevel() # Opens a new window
    rootnum.geometry("345x185+1020+335")
    rootnum.title("Statistics Number Keyboard")
    rootnum.resizable(0,0)

    miscbox_c = ctk.CTkLabel(rootnum, # an area for misc buttons
                            height=130, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=300,y=46)

    closewindow = ctk.CTkButton(rootnum, image=close_windowimg,
                            height=40, width=40, text=None, # Closes the number pad
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootnum.destroy)
    closewindow.place(x=303,y=130)

    pasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    paste = ctk.CTkButton(rootnum, image=pasteimg, # Pastes the value from [CALCULATE] into here
                      height=40, width=40, text=None, command=lambda: 
                      focus.insert(ctk.INSERT, inputoutput.get()),
                      fg_color="grey12", hover_color="grey26", corner_radius=0)
    paste.place(x=303, y=90)

    select = ctk.CTkImage(Image.open("\images\ctypingcursor.png"), size=(25,25))
    focusoption = ctk.CTkButton(rootnum, # Focus typing on another entry
                      height=40, width=40, text=None, image=select,
                      fg_color="grey12", hover_color="grey26", corner_radius=0)
    focusoption.place(x=303,y=50)

    xtype_image = ctk.CTkImage(Image.open("/images/xtype.png"))
    ytype_image = ctk.CTkImage(Image.open("/images/ytype.png"))
    freqtype_image = ctk.CTkImage(Image.open("/images/freqtype.png"), size=(21,20))
    def focustyping(): # Change the typing cursor focus (typing in x? y? frequency?)
        global focusbutton
        global focus
        global focusbutton
        if stat_setting == 0: # Nothing enabled
            focusoption.configure(image=xtype_image)
            focus = xinput_s
        elif stat_setting == 1: # Freq. enabled
            if focusbutton == "x": # Focus on freq.
                focusoption.configure(image=freqtype_image) # Change image
                focus = freqinput
                focusbutton = "f"
            elif focusbutton == "f": # Focus on x
                focusoption.configure(image=xtype_image)
                focus = xinput_s
                focusbutton = "x"
        elif stat_setting == 2: # 2var enabled
            if focusbutton == "x": # Focus on y
                focusoption.configure(image=ytype_image)
                focus = yinput_s
                focusbutton = "y"
            elif focusbutton == "y": # Focus on x
                focusoption.configure(image=xtype_image)
                focus = xinput_s
                focusbutton = "x"
        elif stat_setting == 3: # Both enabled
            if focusbutton == "x": # Focus on y
                focusoption.configure(image=ytype_image)
                focus = yinput_s
                focusbutton = "y"
            elif focusbutton == "y": # Focus on freq. 
                focusoption.configure(image=freqtype_image)
                focus = freqinput
                focusbutton = "f"
            elif focusbutton == "f": # Focus back on x
                focusoption.configure(image=xtype_image)
                focus = xinput_s
                focusbutton = "x"
    focusoption.configure(command=focustyping)
    focustyping()

    num1 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 1
                    height=37, width=87, text_color="white", text="1",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "1"))
    num1.place(x=24,y=15)

    num2 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 2
                    height=37, width=87, text_color="white", text="2",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "2"))
    num2.place(x=114,y=15)

    num3 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 3 etc.
                    height=37, width=87, text_color="white", text="3",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "3"))
    num3.place(x=204,y=15)

    num4 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="4",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "4"))
    num4.place(x=24,y=55)

    num5 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="5",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "5"))
    num5.place(x=114,y=55)

    num6 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="6",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "6"))
    num6.place(x=204,y=55)

    num7 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="7",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "7"))
    num7.place(x=24,y=95)

    num8 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="8",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "8"))
    num8.place(x=114,y=95)

    num9 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # ...7, 8, 9
                    height=37, width=87, text_color="white", text="9",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "9"))
    num9.place(x=204,y=95)

    decimal = ctk.CTkButton(rootnum, font=("segoe ui", 21), # decimal
                    height=37, width=87, text_color="white", text=".",
                    fg_color="grey19", hover_color="grey26",
                    command=lambda: focus.insert(ctk.INSERT, "."))
    decimal.place(x=24,y=135)

    num0 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 0
                    height=37, width=87, text_color="white", text="0",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus.insert(ctk.INSERT, "0"))
    num0.place(x=114,y=135)

    x_variable = ctk.CTkButton(rootnum, font=("STIX Two Text italic", 21), height=37,
                           width=42, text_color="white", text="x", # x variable
                           fg_color="grey19", hover_color="grey26",
                           command=lambda: focus.insert(ctk.INSERT, "x"))
    x_variable.place(x=204, y=135)

    y_variable = ctk.CTkButton(rootnum, font=("STIX Two Text italic", 21), height=37,
                           width=42, text_color="white", text="y", # y variable
                           fg_color="grey19", hover_color="grey26",
                           command=lambda: focus.insert(ctk.INSERT, "y"))
    y_variable.place(x=248, y=135)
    rootnum.attributes("-topmost", True)
rootnum = ctk.CTkToplevel()
rootnum.destroy()

def misc_s():
    miscbox_c = ctk.CTkLabel(stat, # an area for misc buttons
                            height=167.5, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=705,y=205)

    close_windowimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
    close_window_c = ctk.CTkButton(stat, height=40, width=40, text=None, # closes the calculator
                                 fg_color="grey12", image=close_windowimg, command=shutdown,
                                 hover_color="red4", corner_radius=0)
    close_window_c.place(x=708,y=328)

    infoimg = ctk.CTkImage(Image.open("\images\info.png"))
    info = ctk.CTkButton(stat, image=infoimg, # software info
                         height=40, width=40, text=None, corner_radius=0,
                         fg_color="grey12", hover_color="grey26", command=information)
    info.place(x=708, y=288)

    xyimg = ctk.CTkImage(Image.open("\images\cvariables.png"))
    xy_s = ctk.CTkButton(stat, image=xyimg, # edit x and y variables 
                       height=40, width=40, text=None, command=editvariable,
                       fg_color="grey12", hover_color="grey26", corner_radius=0)
    xy_s.place(x=708,y=248)

    numpadimg = ctk.CTkImage(Image.open("\images\cnumbers.png"))
    numpad = ctk.CTkButton(stat, image=numpadimg, command=opennumpad_s,
                           height=40, width=40, text=None, # opens the number pad
                           fg_color="grey12", hover_color="grey26", corner_radius=0)
    numpad.place(x=708, y=208)
misc_s()

def frequencyactive(): # Frequency enabled
    global frequencyicon
    global frequencyicon_on
    global freqcol_on
    global freqlabel_on
    global data_s
    global stat_setting
    global focusbutton
    global focus
    value = freq_var.get()
    if value == "on":
        if stat_setting == 0: # If nothing is enabled, stat setting is set to 1
            check1 = xdata_s.get("1.0","end").strip()
            if check1 == "":
                stat_setting = 1
            else:
                prompt = messagebox.askokcancel("Clear all?",("Switching settings will clear all data.\nContinue?"))
                if prompt:
                    xdata_s.configure(state="normal")
                    xdata_s.delete("1.0", ctk.END)
                    xdata_s.configure(state="disabled")
                    x_array.clear()
                    y_array.clear()
                    stat_setting = 1
                else:
                    return
        elif stat_setting == 2: # If 2 variables is enabled, stat seeting is set to 3
            check2a = xdata_s.get("1.0","end").strip()
            check2b = ydata_s.get("1.0","end").strip()
            if check2a == "" or check2b == "":
                stat_setting = 3
            else:
                prompt = messagebox.askokcancel("Clear all?",("Switching settings will clear all data.\nContinue?"))
                if prompt:
                    xdata_s.configure(state="normal")
                    xdata_s.delete("1.0", ctk.END)
                    xdata_s.configure(state="disabled")
                    ydata_s.configure(state="normal")
                    ydata_s.delete("1.0", ctk.END)
                    ydata_s.configure(state="disabled")
                    x_array.clear()
                    y_array.clear()
                    stat_setting = 3
                else:
                    return
        stat_rearrange()

        frequencyicon.place_forget()
        # Frequency widgets:
        frequencyimg = ctk.CTkImage(Image.open("\images\stack3on.png"), size=(50,50))
        frequencyicon_on = ctk.CTkLabel(stat, image=frequencyimg, text=None)
        frequencyicon_on.place(x=42, y=173)

        freqcol_off.place_forget() # Frequency Column (ON)
        freqcol_on.place(x=633,y=120)

        freqlabel_off.place_forget() # Frequency toggle icon (ON)
        freqlabelimg_on = ctk.CTkImage(Image.open("\images\stack3on.png"), size=(45,45))
        freqlabel_on = ctk.CTkLabel(stat, text=None, image=freqlabelimg_on)
        freqlabel_on.place(x=644,y=73)

    elif value == "off":
        checkoff = xdata_s.get("1.0","end").strip()
        if checkoff == "":
            pass
        else:
            prompt = messagebox.askokcancel("Clear all?",("Switching settings will clear all data.\nContinue?"))
            if prompt:
                xdata_s.configure(state="normal")
                xdata_s.delete("1.0", ctk.END)
                xdata_s.configure(state="disabled")
                freqcol_on.configure(state="normal")
                freqcol_on.delete("1.0", ctk.END)
                freqcol_on.configure(state="disabled")               
                x_array.clear()
                y_array.clear()
            else:
                return        
        if stat_setting == 1: # If 2 variables is NOT enabled, stat setting set to 0
            stat_setting = 0
        elif stat_setting == 3: # If 2 variables is enabled, stat setting set to 2
            stat_setting = 2
        stat_rearrange()
        frequencyicon_on.place_forget()
        frequencyicon.place(x=42,y=173) # Frequency toggle icon (OFF)
        
        freqcol_on.configure(state="normal")
        freqcol_on.delete("1.0", ctk.END)
        freqcol_on.configure(state="normal")
        freqcol_on.place_forget()
        freqcol_off.place(x=633,y=120) # Frequency column (OFF)

        freqlabel_on.place_forget()
        freqlabel_off.place(x=644,y=73)
    
    if rootnum.winfo_exists():
        focusoption.configure(image=select) # Num pad typing cursor focus reset

frequencyimg = ctk.CTkImage(Image.open("\images\stack3off.png"), size=(50,50))
freq_var = ctk.StringVar(value="off") # Frequency selection button
frequency = ctk.CTkSwitch(stat, text="Frequency", command=frequencyactive,
                        variable=freq_var, onvalue="on", offvalue="off",
                        font=("segoe ui bold",18))
frequency.place(x=5,y=220)
frequencyicon = ctk.CTkLabel(stat, image=frequencyimg, text=None)
frequencyicon.place(x=42, y=173)

freqcol_on = ctk.CTkTextbox(stat, font=("Montserrat", 15),
                       height=250, width=70, text_color="black", state="disabled",
                       fg_color="white", border_color="grey17", border_width=5)
freqcol_on.place_forget()

# Frequency Column (OFF)
freqcol_off = ctk.CTkTextbox(stat, font=("Montserrat", 15),
                       height=250, width=70, text_color="black",
                       fg_color="grey25", border_color="grey17", border_width=5)
freqcol_off.place(x=633,y=120)
freqcol_off.configure(state="disabled") # <- Disables editing
freqlabelimg_off = ctk.CTkImage(Image.open("\images\stack3off.png"), size=(45,45))
freqlabel_off = ctk.CTkLabel(stat, text=None, image=freqlabelimg_off)
freqlabel_off.place(x=644,y=73)

def twovaractive():
    global two_variableicon
    global two_variableicon_on
    global ydata_s
    global ylabel_s
    global stat_setting
    global focusbutton
    global focus
    value = two_variable.get()
    if value == "on":
        if stat_setting == 0: # If nothing is enabled, stat setting is 2
            check1 = xdata_s.get("1.0","end").strip()
            if check1 == "":
                stat_setting = 2
            else:
                prompt = messagebox.askokcancel("Clear all?",("Switching settings will clear all data.\nContinue?"))
                if prompt:
                    xdata_s.configure(state="normal")
                    xdata_s.delete("1.0", ctk.END)
                    xdata_s.configure(state="disabled")
                    freqcol_on.configure(state="normal")
                    freqcol_on.delete("1.0", ctk.END)
                    freqcol_on.configure(state="disabled")                    
                    x_array.clear()
                    y_array.clear()
                    stat_setting = 2
                else:
                    return
        elif stat_setting == 1: # If frequency is enabled, stat setting is set to 3
            check2a = xdata_s.get("1.0","end").strip()
            check2b = freqcol_on.get("1.0","end").strip()
            if check2a == "" or check2b == "":
                stat_setting = 3
            else:
                prompt = messagebox.askokcancel("Clear all?",("Switching settings will clear all data.\nContinue?"))
                if prompt:
                    xdata_s.configure(state="normal")
                    xdata_s.delete("1.0", ctk.END)
                    xdata_s.configure(state="disabled")
                    ydata_s.configure(state="normal")
                    ydata_s.delete("1.0", ctk.END)
                    ydata_s.configure(state="disabled")
                    freqcol_on.configure(state="normal")
                    freqcol_on.delete("1.0", ctk.END)
                    freqcol_on.configure(state="disabled")
                    x_array.clear()
                    y_array.clear()
                    stat_setting = 3
                else:
                    return   
        stat_rearrange()
        two_variableicon.place_forget()
        two_variableimg = ctk.CTkImage(Image.open("\images\columnaddon.png"), size=(50,50))
        two_variableicon_on = ctk.CTkLabel(stat, image=two_variableimg, text=None)
        two_variableicon_on.place(x=45,y=263)
        # Y column (ON)
        xdata_s.configure(width=83)
        xlabel_s.place(x=485,y=77)
        ydata_s.place(x=548,y=120) # inserted y data
        ylabelimg = ctk.CTkImage(Image.open("/images/y.png"), size=(30,40))
        ylabel_s = ctk.CTkLabel(stat, text=None, image=ylabelimg)
        ylabel_s.place(x=570,y=76)

    elif value == "off":
        checkoff = xdata_s.get("1.0","end").strip()
        if checkoff == "":
            pass
        else:
            prompt = messagebox.askokcancel("Clear all?",("Switching settings will clear all data.\nContinue?"))
            if prompt:
                xdata_s.configure(state="normal")
                xdata_s.delete("1.0", ctk.END)
                xdata_s.configure(state="disabled")
                x_array.clear()
                y_array.clear()
            else:
                return
        if stat_setting == 2: # If frequency is NOT enabled, stat setting is set to 2
            stat_setting = 0
        elif stat_setting == 3: # If frequency is enabled, stat setting is set to 3
            freqinput.place_forget()
            stat_setting = 1
        stat_rearrange()
        two_variableicon.place(x=45,y=263)
        two_variableicon_on.place_forget()
        # Y column (OFF)
        xdata_s.configure(width=170)
        xlabel_s.place(x=530,y=77)
        ydata_s.place_forget()
        ylabel_s.place_forget()
    
    if rootnum.winfo_exists():
        focusoption.configure(image=select) # Num pad typing cursor focus reset

twovar_var = ctk.StringVar(value="off")
two_variableimg = ctk.CTkImage(Image.open("\images\columnaddoff.png"), size=(50,50))
two_variable = ctk.CTkSwitch(stat, text="Two\nVariables", command=twovaractive,
                             variable=twovar_var, onvalue="on", offvalue="off",
                             font=("segoe ui bold",18))
two_variable.place(x=5,y=310) # Use 2 variables (x and y) instead of 1
two_variableicon = ctk.CTkLabel(stat, image=two_variableimg, text=None)
two_variableicon.place(x=45,y=263)

ydata_s = ctk.CTkTextbox(stat, font=("Montserrat", 15),
                        height=250, width=83, text_color="black",
                        fg_color="white", state="disabled")
ydata_s.place_forget()

xdata_s = ctk.CTkTextbox(stat, font=("Montserrat", 15),
                        height=250, width=170, text_color="black",
                        fg_color="white", state="disabled")
xdata_s.place(x=460,y=120) # inserted x data
xlabelimg = ctk.CTkImage(Image.open("/images/x.png"), size=(35,35))
xlabel_s = ctk.CTkLabel(stat, text=None, image=xlabelimg)
xlabel_s.place(x=530,y=77)

# ---

# 0 → No 2 variables or frequency
# 1 → Frequency enabled
# 2 → 2 variables enabled
# 3 → Both enabled
yinput_s = ctk.CTkEntry(stat, # y entry box
                        height=37, width=434, font=("Noto Sans Math", 20),
                        fg_color="grey14", border_color="grey14")
freqinput = ctk.CTkEntry(stat, # a freq. entry box
                        height=80, width=102, font=("Noto Sans Math", 40),
                        fg_color="grey14", border_color="grey14")

def stat_rearrange():
    global xinput_s
    global xlabel_s
    global freqline
    global freqlabel
    global freqinput
    global yinput_s
    global yinputlabel
    if stat_setting == 0: # Nothing enabled
        # place_forgets every entry input widget and icons/labels
        if "xinput_s" in globals(): #   |
            xinput_s.place_forget() #   |
        if "freqlabel" in globals(): #  ↓
            freqlabel.place_forget()
        if "freqinput" in globals():
            freqinput.place_forget()
        if "freqline" in globals():
            freqline.place_forget()
        if "yinputlabel" in globals():
            yinputlabel.place_forget()
        if "yinput_s" in globals():
            yinput_s.place_forget()
        xinput_s = ctk.CTkEntry(stat, # entry box
                        height=80, width=435, font=("Noto Sans Math", 40),
                        fg_color="grey14", border_color="grey14")
        xinput_s.place(x=20,y=75)
        xinputlabelimg = ctk.CTkImage(Image.open("/images/x.png"), size=(15,15))
        xinputlabel = ctk.CTkLabel(stat, text=None, image=xinputlabelimg)
        xinputlabel.place(x=0,y=73)

    elif stat_setting == 1: # Freq. enabled - this is where a
        if "xinput_s" in globals(): #         frequency entry
            xinput_s.place_forget() #         input is added
        if "freqlabel" in globals():
            freqlabel.place_forget()
        if "freqinput" in globals():
            freqinput.place_forget()
        if "freqline" in globals():
            freqline.place_forget()
        if "yinputlabel" in globals():
            yinputlabel.place_forget()
        if "yinput_s" in globals():
            yinput_s.place_forget()
        xinput_s = ctk.CTkEntry(stat, # entry box
                        height=80, width=300, font=("Noto Sans Math", 40),
                        fg_color="grey14", border_color="grey14")
        xinput_s.place(x=20,y=75)

        freqline = ctk.CTkLabel(stat, text=None, fg_color="white", width=1, height=77, 
                         corner_radius=1)
        freqline.place(x=325,y=77) # This is just a line

        freqinput = ctk.CTkEntry(stat, # a freq. entry box
                        height=80, width=102, font=("Noto Sans Math", 40),
                        fg_color="grey14", border_color="grey14")
        freqinput.place(x=353,y=75)
        freqlabelimg = ctk.CTkImage(Image.open("\images\stack3on.png"), size=(15,15))
        freqlabel = ctk.CTkLabel(stat, text=None, image=freqlabelimg)
        freqlabel.place(x=332,y=73)

    elif stat_setting == 2: # 2 variables enabled - this is where a
        if "xinput_s" in globals(): #               y entry input
            xinput_s.place_forget() #               is added
        if "freqlabel" in globals():
            freqlabel.place_forget()
        if "freqinput" in globals():
            freqinput.place_forget()
        if "freqline" in globals():
            freqline.place_forget()
        if "yinputlabel" in globals():
            yinputlabel.place_forget()
        if "yinput_s" in globals():
            yinput_s.place_forget()
        xinput_s = ctk.CTkEntry(stat, # x entry box
                        height=37, width=434, font=("Noto Sans Math", 20),
                        fg_color="grey14", border_color="grey14")
        xinput_s.place(x=20,y=75)      
        
        yinput_s = ctk.CTkEntry(stat, # y entry box
                        height=37, width=434, font=("Noto Sans Math", 20),
                        fg_color="grey14", border_color="grey14")
        yinput_s.place(x=20,y=117)
        yinputlabelimg = ctk.CTkImage(Image.open("/images/y.png"), size=(15,15))
        yinputlabel = ctk.CTkLabel(stat, text=None, image=yinputlabelimg)
        yinputlabel.place(x=0,y=114)       

    elif stat_setting == 3: # Both enabled - where both entry inputs
        if "xinput_s" in globals(): #        are added
            xinput_s.place_forget()
        if "freqlabel" in globals():
            freqlabel.place_forget()
        if "freqinput" in globals():
            freqinput.place_forget()
        if "freqline" in globals():
            freqline.place_forget()
        if "yinputlabel" in globals():
            yinputlabel.place_forget()
        if "yinput_s" in globals():
            yinput_s.place_forget()
        xinput_s = ctk.CTkEntry(stat, # x entry box
                        height=37, width=300, font=("Noto Sans Math", 20),
                        fg_color="grey14", border_color="grey14")
        xinput_s.place(x=20,y=75)      
        
        yinput_s = ctk.CTkEntry(stat, # y entry box
                        height=37, width=300, font=("Noto Sans Math", 20),
                        fg_color="grey14", border_color="grey14")
        yinput_s.place(x=20,y=117)
        yinputlabelimg = ctk.CTkImage(Image.open("/images/y.png"), size=(15,15))
        yinputlabel = ctk.CTkLabel(stat, text=None, image=yinputlabelimg)
        yinputlabel.place(x=0,y=114) 

        freqline = ctk.CTkLabel(stat, text=None, fg_color="white", width=1, height=77, 
                         corner_radius=1)
        freqline.place(x=325,y=77) # this is just a line

        freqinput = ctk.CTkEntry(stat, # freq. entry box
                        height=80, width=102, font=("Noto Sans Math", 40),
                        fg_color="grey14", border_color="grey14")
        freqinput.place(x=353,y=75)
        freqlabelimg = ctk.CTkImage(Image.open("\images\stack3on.png"), size=(15,15))
        freqlabel = ctk.CTkLabel(stat, text=None, image=freqlabelimg)
        freqlabel.place(x=332,y=73) 
    else:
        print("Test end")
stat_rearrange()
focus = xinput_s # For the numpad
                 # Focuses where the typing cursor is

def xyf_entryclear(): # Deletes all text in entries
    global yinput_s
    global freqinput
    global freqcol_off
    if "yinput_s" in globals(): # If yinput_s is mapped on the UI
        yinput_s.delete(0, ctk.END) # Erases everything in the (yinput_s) entry
    if "freqinput" in globals(): # If freqinput is mapped on the UI
        freqinput.delete(0, ctk.END)
    xinput_s.delete(0, ctk.END)

def xyfentry_clear():
    global yinput_s
    global freqinput
    prompt = messagebox.askyesno("Clear all?",("Are you sure you want to clear all inserted data and entry values?"))
    if prompt:
        xinput_s.delete(0, ctk.END) # Clears the entry
        xdata_s.configure(state="normal") # Enables editing for the program
        xdata_s.delete("1.0", ctk.END) # Clears the columns
        xdata_s.configure(state="disabled") # then disables editing for the user
        if "yinput_s" in globals(): # Same thing again, but in yinput_s (if mapped)
            yinput_s.delete(0, ctk.END)
            ydata_s.configure(state="normal")
            ydata_s.delete("1.0", ctk.END)
            ydata_s.configure(state="disabled")
        if "freqinput" in globals():
            freqinput.delete(0, ctk.END)
        if "freqcol_off" in globals():
            freqcol_off.configure(state="normal")
            freqcol_off.delete("1.0", ctk.END)
            freqcol_off.configure(state="disabled")
        if "freqcol_on" in globals():
            freqcol_on.configure(state="normal")
            freqcol_on.delete("1.0", ctk.END)
            freqcol_on.configure(state="disabled")  
        x_array.clear() # ← Deletes any data in the two arrays
        y_array.clear() # ←

def backspace_s(): # Deletes a value based on the typing cursor
    expression = root.focus_get().get()
    root.focus_get().delete(len(expression)-1, ctk.END)

xinsert = 0
yinsert = 0
finsert = 0
def insertdata():
    global yinput_s
    global freqinput
    global freqcol_on
    global yinsert
    global finsert
    global xinsert
    global x
    global y
    xinsert = xinput_s.get()
    if xinsert == "": # Error handing - checks if xinput_s is empty
        xprompt = messagebox.askokcancel("Insert 0?",("""You haven't entered anything in the X entry.
If you continue, the calculator will assume you've put 0"""))
        if xprompt:
            xinsert = 0
        else:
            return # this cancels the insertdata operation
    if yinput_s.winfo_ismapped(): # Error handling - checks if yinput_s is empty (if mapped)
        yinsert = yinput_s.get()
        if yinsert == "":
            prompty = messagebox.askokcancel("Insert 0?",("""You haven't entered anything in the Y entry.
If you continue, the calculator will assume you've put 0"""))
            if prompty:
                yinsert = 0
            else:
                return
    if "freqinput" in globals(): # Error handling - checks if freqinput is empty (if mapped)
        finsert = freqinput.get()
        if finsert == "":
            if stat_setting == 3:
                promptf1 = messagebox.askokcancel("Insert 1?",("""You haven't tied any frequency values to X and Y.
If you continue, the calculator will assume those X and Y values have a frequency of 1"""))
                if promptf1:
                    finsert = 1
                else:
                    return
            elif stat_setting == 1:
                promptf2 = messagebox.askokcancel("Insert 1?",("""You haven't tied any frequnecy values to X.
If you continue, the calculator will assume that the X value has a frequency of 1"""))
                if promptf2:
                    finsert = 1
                else:
                    return

    # Array ---

    if "x" in str(xinsert) or "y" in str(xinsert):
        xinsert = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", xinsert))
    if "x" in str(yinsert) or "y" in str(yinsert):
        yinsert = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", yinsert))
    if "x" in str(finsert) or "y" in str(finsert):
        finsert = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", finsert))

    try: # Attempts to insert data into the array
        if not ydata_s.winfo_ismapped() and not freqcol_on.winfo_ismapped(): # Disabled
            x_array.append(float(xinsert)) # Inserts data into the x array
        
        elif ydata_s.winfo_ismapped() and not freqcol_on.winfo_ismapped(): # 2var enabled
            x_array.append(float(xinsert))
            y_array.append(float(yinsert)) # Inserts data into the y array
        
        elif freqcol_on.winfo_ismapped() and not ydata_s.winfo_ismapped(): # Freq. enabled
            for i in range(int(finsert)): # Using a loop, the frequency will repeatedly insert data
                x_array.append(float(xinsert)) #                                 based on "finsert"

        elif ydata_s.winfo_ismapped() and freqcol_on.winfo_ismapped(): # Both enabled
            for i in range(int(finsert)):
                x_array.append(float(xinsert))
                y_array.append(float(yinsert))
    
    except: # If an error is encountered...
        messagebox.showerror("Error",("""[Array ERROR]
The calculator couldn't insert the data. Try:
• Checking if your data is correct
• No extranous data is entered"""))
        return

    # Columns & Entries ---
    xdata_s.configure(state="normal") # These parts enable editing for the program
    xdata_s.insert(index=(1.0), text=str(xinsert) + "\n") #         ↓↓↓
    xdata_s.configure(state="disabled") # then are disabled so it can't be edited by the user
    xinput_s.delete(0, ctk.END) # Resets the entries
    if "ydata_s" in globals(): # Same thing again but with different entries (if they're mapped)
        ydata_s.configure(state="normal")
        ydata_s.insert(index=(1.0), text=str(yinsert) + "\n")
        ydata_s.configure(state="disabled")
        yinput_s.delete(0, ctk.END)
    if "freqinput" in globals():
        freqcol_on.configure(state="normal")
        freqcol_on.insert(index=(1.0), text=str(finsert) + "\n")
        freqcol_on.configure(state="disabled")
        freqinput.delete(0, ctk.END)
    print("x_array: ", x_array)
    print("y_array: ", y_array)

clear_simg = ctk.CTkImage(Image.open("\images\clear_wh.png"), size=(25,25))
clear_s = ctk.CTkButton(stat, image=clear_simg, font=("segoe ui bold", 15),
                        height=65, width=150, text_color="white", text=" Clear Entries",
                        fg_color="grey14", border_color="red2", hover_color="red4",
                        border_width=2, command=xyf_entryclear)
clear_s.place(x=305,y=161) # Clear entry box

insert_simg = ctk.CTkImage(Image.open("\images\insert.png"), size=(25,25))
insert_s = ctk.CTkButton(stat, image=insert_simg, font=("segoe ui bold", 15), height=65, width=150,
                       text_color="white", fg_color="deepskyblue4", text="          Insert",
                       command=insertdata)
insert_s.place(x=305,y=230) # Inserts into x (and y) data

execute_simg = ctk.CTkImage(Image.open("\images\evalstat.png"), size=(50,50))
execute_s = ctk.CTkButton(stat, text=None, font=("segoe ui", 40), height=70, width=303,
                          text_color="white", fg_color="deepskyblue4", image=execute_simg,
                          command=evaluate_s)
execute_s.place(x=151,y=301) # Finds the results of x (and y) data

cleardata_simg = ctk.CTkImage(Image.open("\images\deleteforever.png"), size=(25,25))
cleardata_s = ctk.CTkButton(stat, image=cleardata_simg, text="   Clear ALL ", border_color="red2",
                          border_width=2, text_color="red2", hover_color="red4", font=
                          ("segoe ui bold", 15), height=64, width=150, fg_color="grey14",
                          command=xyfentry_clear)
cleardata_s.place(x=151,y=161) # Clears everything

bksp_simg = ctk.CTkImage(Image.open("\images\down.png"), size=(25,25))
bksp_s = ctk.CTkButton(stat, image=bksp_simg, text="    Backspace", font=("segoe ui bold", 15),
                       hover_color="red4", fg_color="grey14", height=65, width=150,
                       border_color="deepskyblue4", border_width=2, command=backspace_s)
bksp_s.place(x=151,y=230) # Entry backspace

statline1 = ctk.CTkLabel(stat, text=None, fg_color="white", width=1, height=208, 
                         corner_radius=1)
statline1.place(x=143,y=161) # This is just a line



# [GRAPH/TABLE] -------



# These are just banners - user interface cosmetic
banner_g = ctk.CTkLabel(graph, text="  Graph & Table", font=("segoe ui bold", 35),
                         height=70, width=420, fg_color="deepskyblue4", anchor="w")
banner_g.place(x=0,y=0)
banner_g2 = ctk.CTkLabel(graph, text=None, fg_color="deepskyblue3", height=70,
                          width=160)
banner_g2.place(x=419,y=0)
banner_g3 = ctk.CTkLabel(graph, text=None, fg_color="deepskyblue2", height=70,
                          width=160)
banner_g3.place(x=578,y=0)

def opennumpad_gt(): # Number pad
    global focus_g
    global rootnum
    try:
        if rootnum.winfo_exists():
            return
    except:
        pass
    rootnum = ctk.CTkToplevel()
    rootnum.geometry("345x185+1020+335")
    rootnum.title("Graph & Table Number Keyboard")
    rootnum.resizable(0,0)

    miscbox_c = ctk.CTkLabel(rootnum, # an area for misc buttons
                            height=88, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=300,y=86)

    closewindow = ctk.CTkButton(rootnum, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootnum.destroy)
    closewindow.place(x=303,y=130) # Button to close the numpad

    pasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    paste = ctk.CTkButton(rootnum, image=pasteimg, # Pastes the CALCULATE value into
                      height=40, width=40, text=None, #                    the entry
                      fg_color="grey12", hover_color="grey26", corner_radius=0,
                      command=lambda: focus_g.insert(ctk.INSERT, inputoutput.get()))
    paste.place(x=303, y=90)

    num1 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 1
                    height=37, width=87, text_color="white", text="1",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "1"))
    num1.place(x=24,y=15)

    num2 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 2
                    height=37, width=87, text_color="white", text="2",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "2"))
    num2.place(x=114,y=15)

    num3 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 3
                    height=37, width=87, text_color="white", text="3",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "3"))
    num3.place(x=204,y=15)

    num4 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 4 etc...
                    height=37, width=87, text_color="white", text="4",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "4"))
    num4.place(x=24,y=55)

    num5 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="5",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "5"))
    num5.place(x=114,y=55)

    num6 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="6",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "6"))
    num6.place(x=204,y=55)

    num7 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="7",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "7"))
    num7.place(x=24,y=95)

    num8 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="8",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "8"))
    num8.place(x=114,y=95)

    num9 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="9",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "9"))
    num9.place(x=204,y=95)

    decimal = ctk.CTkButton(rootnum, font=("segoe ui", 21), # decimal
                    height=37, width=87, text_color="white", text=".",
                    fg_color="grey19", hover_color="grey26",
                    command=lambda: focus_g.insert(ctk.INSERT, "."))
    decimal.place(x=24,y=135)

    num0 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 0
                    height=37, width=177, text_color="white", text="0",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: focus_g.insert(ctk.INSERT, "0"))
    num0.place(x=114,y=135)

    rootnum.attributes("-topmost", True)

def misc_gt():
    miscbox_c = ctk.CTkLabel(graph, # an area for misc buttons
                            height=127.5, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=705,y=245)
    # ---
    close_windowimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
    close_window_c = ctk.CTkButton(graph, height=40, width=40, text=None,
                                 fg_color="grey12", image=close_windowimg, command=shutdown,
                                 hover_color="red4", corner_radius=0)
    close_window_c.place(x=708,y=328)

    infoimg = ctk.CTkImage(Image.open("\images\info.png"))
    info = ctk.CTkButton(graph, image=infoimg,
                         height=40, width=40, text=None, corner_radius=0,
                         fg_color="grey12", hover_color="grey26", command=information)
    info.place(x=708, y=288)

    numpadimg = ctk.CTkImage(Image.open("\images\cnumbers.png"))
    numpad = ctk.CTkButton(graph, image=numpadimg,
                           height=40, width=40, text=None, command=opennumpad_gt,
                           fg_color="grey12", hover_color="grey26", corner_radius=0)
    numpad.place(x=708, y=248)
misc_gt()

def backspace_g():
    expression = equationinput.get()
    equationinput.delete(len(expression)-1, ctk.END)

def backspace2_g():
    expression = xinput_g.get()
    equationinput.delete(len(expression)-1, ctk.END)

fx_formula = ""
gx_formula = ""

def fgdefine():
    global fx_formula
    global gx_formula
    global equation_op1
    global equation_op2
    global equation_op3
    global rootdef
    global deselectcolour
    try:
        if rootdef.winfo_exists():
            return
    except:
        pass
    rootdef = ctk.CTkToplevel()
    rootdef.geometry("345x200+1020+40")
    rootdef.title("Define f(x) & g(x)")
    rootdef.resizable(0,0)

    definefocus = tk.IntVar(value="0")

    miscbox_t = ctk.CTkLabel(rootdef, # an area for misc buttons
                            height=49, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_t.place(x=300,y=140)

    closewindow = ctk.CTkButton(rootdef, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootdef.destroy)
    closewindow.place(x=303,y=145)

    def deselectcolour(): # Resets the highlight colour of all buttons
        equation_op1.configure(fg_color="grey14")
        equation_op1.configure(hover_color="dodgerblue4")

        equation_op2.configure(fg_color="grey14")
        equation_op2.configure(hover_color="dodgerblue4")
        
        equation_op3.configure(fg_color="grey14")
        equation_op3.configure(hover_color="dodgerblue4")

    def define_op1(): # Define f(x) or g(x) with option 1 (equation_op1)
        global fx_formula
        global gx_formula
        deselectcolour()
        function = definefocus.get()
        if function == 0: # If no function is chosen...
            messagebox.showerror("No function chosen",("A function hasn't been selected"))
        
        else:  # ↓ ↓ ↓ ↓ ↓ or "equation_op2" or "equation_op3"
            if equation_op1.cget("text") == " ": # If the button option has no equation...
                messagebox.showinfo("No equation",("""This option dosen't contain an equation.
Consider going to Graph and evaluating an equation - you will see
all your evaluated equations here after they're drawn!"""))

            elif function == 1: # Defining f(x)
                fx_formula = equation_history0 # ← ← ←
                equation_op1.configure(fg_color="deepskyblue4")    # Button option is highlighted
                equation_op1.configure(hover_color="deepskyblue4") # to display to the user that
                                                                   # this equation is selected to define
                                                                   # the selected function
            elif function == 2: # Defining g(x) 
                gx_formula = equation_history0 # ← ← ←
                equation_op1.configure(fg_color="deepskyblue4")
                equation_op1.configure(hover_color="deepskyblue4")

    # ↓ ↓ ↓ These are the same as above, but with the variable of "equation_op2" or "equation_op3"
    def define_op2():
        global fx_formula
        global gx_formula
        deselectcolour()
        function = definefocus.get()
        if function == 0:
            messagebox.showerror("No function chosen",("A function hasn't been selected"))
        
        else:
            if equation_op2.cget("text") == " ":
                messagebox.showinfo("No equation",("""This option dosen't contain an equation.
Consider going to Graph and evaluating an equation - you will see
all your evaluated equations here after they're drawn!"""))

            elif function == 1: # Defining f(x)
                fx_formula = equation_history1
                equation_op2.configure(fg_color="deepskyblue4")
                equation_op2.configure(hover_color="deepskyblue4")
            elif function == 2: # Defining g(x)
                gx_formula = equation_history1
                equation_op2.configure(fg_color="deepskyblue4")
                equation_op2.configure(hover_color="deepskyblue4")
        
    def define_op3():
        global fx_formula
        global gx_formula
        deselectcolour()
        function = definefocus.get()
        if function == 0:
            messagebox.showerror("No function chosen",("A function hasn't been selected"))
        
        else:
            if equation_op3.cget("text") == " ":
                messagebox.showinfo("No equation",("""This option dosen't contain an equation.
Consider going to Graph and evaluating an equation - you will see
all your evaluated equations here after they're drawn!"""))
            elif function == 1: # Defining f(x)
                fx_formula = equation_history2
                equation_op3.configure(fg_color="deepskyblue4")
                equation_op3.configure(hover_color="deepskyblue4")
            elif function == 2: # Defining g(x)
                gx_formula = equation_history2
                equation_op3.configure(fg_color="deepskyblue4")
                equation_op3.configure(hover_color="deepskyblue4")
        
    def functionfocus():
        functionview = definefocus.get()
        deselectcolour()

        if functionview == 1: # f(x) chosen
            if fx_formula == equation_op1.cget("text"):
                equation_op1.configure(fg_color="deepskyblue4")
                equation_op1.configure(hover_color="deepskyblue4")
            elif fx_formula == equation_op2.cget("text"):
                equation_op2.configure(fg_color="deepskyblue4")
                equation_op2.configure(hover_color="deepskyblue4")
            elif fx_formula == equation_op3.cget("text"):                
                equation_op3.configure(fg_color="deepskyblue4")
                equation_op3.configure(hover_color="deepskyblue4")
            else:
                pass
        
        elif functionview == 2: # g(x) chosen
            if gx_formula == equation_op1.cget("text"):
                equation_op1.configure(fg_color="deepskyblue4")
                equation_op1.configure(hover_color="deepskyblue4")
            elif gx_formula == equation_op2.cget("text"):
                equation_op2.configure(fg_color="deepskyblue4")
                equation_op2.configure(hover_color="deepskyblue4")
            elif gx_formula == equation_op3.cget("text"):                
                equation_op3.configure(fg_color="deepskyblue4")
                equation_op3.configure(hover_color="deepskyblue4")
            else:
                pass
            
    define_fx = ctk.CTkRadioButton(rootdef, text=" f(x)", # Define f(x) with...
                                   font=("STIX Two Text bold italic", 30),
                                   variable=definefocus, value="1", command=functionfocus)
    define_fx.place(x=40,y=5)

    define_gx = ctk.CTkRadioButton(rootdef, text=" g(x)", # Define g(x) with...
                                   font=("STIX Two Text bold italic", 30),
                                   variable=definefocus, value="2", command=functionfocus)
    define_gx.place(x=160,y=5)

    equation_op1 = ctk.CTkButton(rootdef, text=equation_history0,
                                 font=("STIX Two Text italic", 23), fg_color="grey14",
                                 border_color="deepskyblue4", border_width=2, 
                                 hover_color="dodgerblue4", width=290,
                                 command=define_op1) # Option 1
    equation_op1.place(x=5,y=55)

    equation_op2 = ctk.CTkButton(rootdef, text=equation_history1,
                                 font=("STIX Two Text italic", 23), fg_color="grey14",
                                 border_color="deepskyblue4", border_width=2,
                                 hover_color="dodgerblue4", width=290,
                                 command=define_op2) # Option 2
    equation_op2.place(x=5,y=102)

    equation_op3 = ctk.CTkButton(rootdef, text=equation_history2,
                                 font=("STIX Two Text", 23), fg_color="grey14",
                                 border_color="deepskyblue4", border_width=2,
                                 hover_color="dodgerblue4", width=290,
                                 command=define_op3) # Option 3
    equation_op3.place(x=5, y=149)

# Stores the equation for the Table's use
equation_history0 = " " # Top option
equation_history1 = " " # Mid option
equation_history2 = " " # Bottom option
history = 0

def drawingspecial():
    webbrowser.open("https://www.google.com/maps/place/skibidi+toilet/@-33.3884525,-70.6601704,839m/data=!3m1!1e3!4m16!1m9!3m8!1s0x9662c75ee297d2b7:0xb3a63836bedcce17!2sskibidi+toilet!8m2!3d-33.3884525!4d-70.6575901!9m1!1b1!16s%2Fg%2F11ltw_pnbx!3m5!1s0x9662c75ee297d2b7:0xb3a63836bedcce17!8m2!3d-33.3884525!4d-70.6575901!16s%2Fg%2F11ltw_pnbx?entry=ttu&g_ep=EgoyMDI0MTAxMy4wIKXMDSoASAFQAw%3D%3D")
    sleep(3)
    webbrowser.open("https://www.instagram.com/p/DATcK2JyLFe/")
    sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=BtOB3XHWLi8")
    sleep(3)
    for i in range(10):
        webbrowser.open("https://www.youtube.com/watch?v=At8v_Yc044Y")
        sleep(0.6)

def evaluate_g():
    global gx_formula
    global fx_formula
    global equation_history0
    global equation_history1
    global equation_history2
    global equation_op1
    global equation_op2
    global equation_op3
    global history
    global developermode
    expression = equationinput.get()
    
    if expression == "show me skibidi toilet fanum taxing looksmaxxing capabilities":
        messagebox.showwarning("Developer Console",("[WARNING] Developer Mode is on!"))
        confirm = messagebox.askyesno("Developer Console",("""[Operation MAPS]
You are about to perform an operation that involves developer use only!
Would you like to proceed further with this?
[YES] -> Yep. I'd like to
[NO] -> No, cancel and disable developer mode"""))
        if confirm:
            confirm2 = messagebox.askyesno("Developer Console",("""[Operation MAPS]
Are you absolutely sure? By proceeding, you understand that this is used for developer use only and will be responsible for any outcomes.
Developer Mode cannot be disabled until the program is closed.
[YES] -> I am absolutely, 100 percent, fingers crossed, sure! 
[NO] -> Absolutely not! Cancel this operation"""))
            if confirm2:
                drawingspecial()
                messagebox.showwarning("Developer Console",("[Operation MAPS] Active"))
                developermode = 1
                return
            else:
                return
        else:
            return
    else:
        pass    

    # Converting the equation into what python can understand
    expression_step1 = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", expression)
    # ↑ Like factorial, this allows the calculator to understand "nx" phrases
    expression_step2 = expression_step1.replace("²","**2") # x squared
    expression_step3 = expression_step2.replace("³","**3") # x cubed
    equation = expression_step3.replace("^","**") # power of..?

    # Equation Processing ---
    xplot = np.linspace(-40, 40, 400)
    try: # Attempts to process the equation
        if "x" in equation:
            yplot = eval(equation, {"x": xplot, "np": np})
    
        elif "x" not in equation:
            yeval = eval(equation, {"np": np})
            yplot = np.full_like(xplot, yeval)
    
    except SyntaxError or ValueError: # General syntax error
        messagebox.showerror("Error",("""[Syntax Error]
The calculator couldn't process your mathematical expression! Try:
• Checking if operators are correctly used
• No blank feilds are left out"""))
        return

    except NameError: # Extranous data (i.e. random letters/symbols
                                            #       in the equation)
        messagebox.showerror("Error",("""[Syntax ERROR]
The calculator received extranous data. Try:
• Removing extranous data
• Only using x"""))
        return

    except OverflowError: # Very large results of data
        messagebox.showerror("Error",("""[Math ERROR]
    The calculator recieved a very large result, in which it can't handle! Try:
    • Shortening down the equation"""))
        return

    except: # For all other errors encountered
        messagebox.showerror("Error",("""[Other ERROR]
The calculator couldn't process your equation! Try:
• Check error logs"""))
        return


    # Plotting ---
    plt.subplots(figsize=(10,4))
    plt.plot(xplot, yplot)
    
    plt.title(expression)
    plt.xlabel("x")
    plt.ylabel("y")

    # Stores the expression when needed in Table ---
    if history == 0: # Saved on the top option
        equation_history0 = expression
        history = 1
        try:
            if equation_op1:
                equation_op1.configure(text=equation_history0)
        except:
            pass # In case the function define window is not opened,
                # there wont be need to configure the button

    elif history == 1: # Saved on the mid option
        equation_history1 = expression
        history = 2
        try:
            if equation_op2:
                equation_op2.configure(text=equation_history1)
        except:
            pass

    elif history == 2: # Saved on the bottom option
        equation_history2 = expression
        history =  0 # Loops back to the top option
        try:
            if equation_op3:
                equation_op3.configure(text=equation_history2)
        except:
            pass

    # Resets functions when a new equation is added
    gx_formula = ""
    fx_formula = ""
    try:
        deselectcolour()
    except:
        pass

    plt.show()

def evaluate2_g():
    # Finding f(x) ---

    # Converting the equation into what python can understand
    if fx_formula == "": # If f(x) isn't defined to anything, the calculator
        fxdata.configure(state="normal") # will just insert a blank value
        fxdata.insert(index=(1.0), text="\n")
        fxdata.configure(state="disabled")
    
    else:
        solve_step1 = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", fx_formula)
        # ↑ Like factorial, x is rearranged more for python to understand "nx" values
        solve_step2 = solve_step1.replace("²","**2") # x squared
        solve_step3 = solve_step2.replace("³","**3") # x cubed
        solve_step4 = solve_step3.replace("^","**") # power of..?
        solve_step5 = solve_step4.replace("x",xinput_g.get()) # Substitution
        fx_answer = eval(solve_step5) # Solves the equation

        # Inserts the answer into the f(x) column
        fxdata.configure(state="normal")
        fxdata.insert(index=(1.0), text=str(fx_answer) + "\n")
        fxdata.configure(state="disabled")
    
    # Finding g(x) ---
    
    # ↓ ↓ ↓ Same process as above, but with "gxdata" and "gx_answer"
    if gx_formula == "":
        gxdata.configure(state="normal")
        gxdata.insert(index=(1.0), text="\n")
        gxdata.configure(state="normal")
    else:
        solve_step1 = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", gx_formula)
        solve_step2 = solve_step1.replace("²","**2") # x squared
        solve_step3 = solve_step2.replace("³","**3") # x cubed
        solve_step4 = solve_step3.replace("^","**") # power of..?
        solve_step5 = solve_step4.replace("x",xinput_g.get())
        gx_answer = eval(solve_step5)

        gxdata.configure(state="normal")
        gxdata.insert(index=(1.0), text=str(gx_answer) + "\n")
        gxdata.configure(state="disabled")

    # Inserts the user's x value
    xdata_g.configure(state="normal")
    xdata_g.insert(index=(1.0), text=xinput_g.get() + "\n")
    xdata_g.configure(state="disabled")

    xinput_g.delete(0, ctk.END)

def functionreset():
    global fx_formula
    global gx_formula

    prompt = messagebox.askyesno("Clear all?",("""Are you sure you want to clear everything?
Clearing everything includes:
• Wiping your equations
• Resetting both functions
• Clearing all the data evaluated
This will NOT apply to any Graph windows open"""))
    if prompt:
        # Resets the functions
        fx_formula = ""
        gx_formula = ""

        # Clears any evaluated data
        xdata_g.configure(state="normal")
        xdata_g.delete("1.0", ctk.END)
        xdata_g.configure(state="disabled")
        
        fxdata.configure(state="normal")
        fxdata.delete("1.0", ctk.END)
        fxdata.configure(state="disabled")
        
        gxdata.configure(state="normal")
        gxdata.delete("1.0", ctk.END)
        gxdata.configure(state="disabled")

        xinput_g.delete(0, ctk.END) # Also resets
                                    # the entry

        # Clears the equations & Resets the function
        try:                      # highlight colour
            deselectcolour()
            equation_op1.configure(text=" ")
            equation_op2.configure(text=" ")
            equation_op3.configure(text=" ")
        except:
            pass
    
    else:
        return

def graph_rearrange(): # Unmaps and maps certain widgets
                       # based on the switches are.
    global focus_g
    prompt = changeview_g.get()
    if prompt == 1: # Maps the widgets
        # Unmap the previous main widgets
        graphiconOFF.place_forget()
        tableiconON.place_forget()
        
        xdata_gicon.place_forget()
        xdata_g.place_forget()

        fxdataicon.place_forget()
        fxdata.place_forget()

        gxdataicon.place_forget()
        gxdata.place_forget()

        xinput_g.place_forget()
        xinputlabel.place_forget()
        cleardata_g.place_forget()
        bksp2_g.place_forget()
        clear2_g.place_forget()
        define.place_forget() 
        execute2_g.place_forget()

        # Map the main widgets
        equationlabel.place(x=190, y=125)
        equationinput.place(x=255, y=125)
        clear_g.place(x=255,y=195)
        bksp_g.place(x=310,y=194)
        execute_g.place(x=420, y=194)
        xinsert_g.place(x=180, y=270)
        x2insert_g.place(x=385, y=270)
        x3insert_g.place(x=509, y=270)
        power_n_g.place(x=592,y=270)
        
        # Configure the icons
        graphiconON.place(x=30, y=90)
        tableiconOFF.place(x=30,y=230)
        
        focus_g = equationinput

    elif prompt == 2:
        # Unmap the previous main widgets
        graphiconON.place_forget()
        tableiconOFF.place_forget()
        
        equationlabel.place_forget()
        equationinput.place_forget()
        clear_g.place_forget()
        bksp_g.place_forget()
        execute_g.place_forget()
        xinsert_g.place_forget()
        x2insert_g.place_forget()
        x3insert_g.place_forget()
        power_n_g.place_forget()

        # Map the main widgets
        xdata_gicon.place(x=448,y=77)
        xdata_g.place(x=425,y=120)

        fxdataicon.place(x=528, y=77)
        fxdata.place(x=510, y=120)

        gxdataicon.place(x=625, y=77)
        gxdata.place(x=608, y=120)

        xinput_g.place(x=170,y=75)
        xinputlabel.place(x=150, y=75)
        cleardata_g.place(x=151,y=161)
        bksp2_g.place(x=151,y=230)
        clear2_g.place(x=286,y=161)
        define.place(x=286,y=230) 
        execute2_g.place(x=151,y=301)

        # Configure the icons
        graphiconOFF.place(x=30,y=90)
        tableiconON.place(x=30, y=230)

        focus_g = xinput_g

# This detects whether you're on Graph or Table
# 1 → Graph
# 2 → Table
# By Default is Graph (1)
changeview_g = tk.IntVar(value="1")

# Graph Drawing ---
graphiconONimg = ctk.CTkImage(Image.open("\images\evaldraw.png"), size=(70,70))
graphiconON = ctk.CTkLabel(graph, text=None, image=graphiconONimg) # Icon image
                                                                   # on

graphiconOFFimg = ctk.CTkImage(Image.open("\images\drawoff.png"), size=(70,75))
graphiconOFF = ctk.CTkLabel(graph, text=None, image=graphiconOFFimg) # Icon image
                                                                     # off

graphoption = ctk.CTkRadioButton(graph, text="Graph", command=graph_rearrange,
                                variable=changeview_g, value="1", font=("segoe ui bold", 21),
                                fg_color="deepskyblue4")
graphoption.place(x=20, y=180) # Switch to the graph option

# Table Solving ---
tableiconONimg = ctk.CTkImage(Image.open("\images\ctableon.png"), size=(75,70))
tableiconON = ctk.CTkLabel(graph, text=None, image=tableiconONimg) # Icon image
                                                                   # on

tableiconOFFimg = ctk.CTkImage(Image.open("\images\ctableoff.png"), size=(75,70))
tableiconOFF = ctk.CTkLabel(graph, text=None, image=tableiconOFFimg) # Icon image
                                                                     # off
tableiconOFF.place(x=30, y=90)

tableoption = ctk.CTkRadioButton(graph, text="Table", command=graph_rearrange,
                                variable=changeview_g, value="2", font=("segoe ui bold", 21),
                                fg_color="deepskyblue4")
tableoption.place(x=20, y=320) # Switch to the table option

xinsert_g = ctk.CTkButton(graph, text="x", font=("STIX Two Text italic", 30),
                          height=50, width=200, fg_color="grey26",
                          hover_color="grey19", command=lambda:
                          equationinput.insert(ctk.INSERT, "x")) # Insert x

x2insert_g = ctk.CTkButton(graph, text=" x² ", font=("STIX Two Text italic", 30),
                           height=50, width=120, fg_color="grey26",
                           hover_color="grey19", command=lambda:
                           equationinput.insert(ctk.INSERT, "x²")) # Insert x squared
                                                # "x", "x²", "x³", "^"

x3insert_g = ctk.CTkButton(graph, text="x³", font=("STIX Two Text italic", 30),
                           height=50, width=80, fg_color="grey26",
                           hover_color="grey19", command=lambda:
                           equationinput.insert(ctk.INSERT, "x³")) # Insert x cubed

power_n_gimg = ctk.CTkImage(Image.open("\images\sqaren.png"), size=(43,43))
power_n_g = ctk.CTkButton(graph, text=None, image=power_n_gimg,
                          height=50, width=80, fg_color="grey26", 
                          hover_color="grey19", command=lambda:
                          equationinput.insert(ctk.INSERT, "^")) # Insert something
                                                            # to the power of
                                                            # something

# ---

graph_line = ctk.CTkLabel(graph, text=None, fg_color="white", width=1, height=400, 
                         corner_radius=1)
graph_line.place(x=143, y=75) # Once again, this is just a line

# Graph ---

equationlabel = ctk.CTkLabel(graph, font=("STIX Two Text italic", 37), text="y =") 
                             # Label for "y=...?"
equationinput = ctk.CTkEntry(graph, font=("Noto Sans Math", 40), fg_color="grey14",
                             border_color="grey14", width=400) 
                             # Equation input

clear_gimg = ctk.CTkImage(Image.open("\images\clear.png"))
clear_g = ctk.CTkButton(graph, image=clear_gimg, # Clears the entry box
                        height=48, width=52, text_color="red2", text=None,
                        fg_color="grey14", border_color="red2", hover_color="red4",
                        border_width=2, command=lambda: equationinput.delete(0, ctk.END))

bksp_gimg = ctk.CTkImage(Image.open("\images\down.png"))
bksp_g = ctk.CTkButton(graph, image=bksp_gimg, text=None, # Entry backspace
                       hover_color="red4", fg_color="grey14", height=48, width=108,
                       border_color="deepskyblue4", border_width=2, 
                       command=backspace_g)

execute_gimg = ctk.CTkImage(Image.open("\images\evaldraw.png"), size=(35,35))
execute_g = ctk.CTkButton(graph, image=execute_gimg, text=None, fg_color="deepskyblue4",
                            height=48, width=236, command=evaluate_g)
                            # Button to draw the graph

# Table ---

xinputlabelimg = ctk.CTkImage(Image.open("/images/x.png"), size=(15,15))
xinputlabel = ctk.CTkLabel(graph, text=None, image=xinputlabelimg)
xinput_g = ctk.CTkEntry(graph, # Entry box
                        height=80, width=245, font=("Noto Sans Math", 40),
                        fg_color="grey14", border_color="grey14")

cleardata_gimg = ctk.CTkImage(Image.open("\images\deleteforever.png"), size=(25,25))
cleardata_g = ctk.CTkButton(graph, image=cleardata_gimg, text=" Clear ALL ", border_color="red2",
                          border_width=2, text_color="red2", hover_color="red4", font=
                          ("segoe ui bold", 15), height=64, width=130, fg_color="grey14",
                          command=functionreset) # Clears everything

clear2_gimg = ctk.CTkImage(Image.open("\images\clear_wh.png"), size=(25,25))
clear2_g = ctk.CTkButton(graph, image=clear2_gimg, text="Clear Entry ", border_color="red2",
                          border_width=2, text_color="white", hover_color="red4", font=
                          ("segoe ui bold", 15), height=64, width=130, fg_color="grey14",
                          command=lambda: xinput_g.delete(0, ctk.END)) # Clears the entry

bksp2_gimg = ctk.CTkImage(Image.open("\images\down.png"), size=(25,25))
bksp2_g = ctk.CTkButton(graph, image=bksp2_gimg, text=" Backspace", font=("segoe ui bold", 15),
                       hover_color="red4", fg_color="grey14", height=65, width=130,
                       border_color="deepskyblue4", border_width=2, 
                       command=backspace2_g) # Backspace button
                                    # same function as backspace_g()
                                    # but with a different variable

defineimg = ctk.CTkImage(Image.open("\images\cvariables.png"), size=(25,25))
define = ctk.CTkButton(graph, image=defineimg, font=("segoe ui bold", 15), height=65, width=130,
                       text_color="white", fg_color="grey14", border_color="deepskyblue4",
                       border_width=2, hover_color="grey26", text="     Define... ",
                       command=fgdefine) # Opens up a window to define each
                                        # function

execute2_gimg = ctk.CTkImage(Image.open("\images\ctableon.png"), size=(50,50))
execute2_g = ctk.CTkButton(graph, text=None, font=("segoe ui", 40), height=70, width=268,
                          text_color="white", fg_color="deepskyblue4", image=execute2_gimg,
                          command=evaluate2_g) # Evaluates f(x) and/or g(x)

xdata_giconimg = ctk.CTkImage(Image.open("/images/x.png"), size=(35,35))
xdata_gicon = ctk.CTkLabel(graph, text=None, image=xdata_giconimg)
xdata_g = ctk.CTkTextbox(graph, font=("Montserrat", 15),
                        height=250, width=80, text_color="black",
                        fg_color="white", state="disabled", border_color="grey17",
                        border_width=5) # User input histroy

fxdataiconimg = ctk.CTkImage(Image.open("/images/xfunct.png"), size=(55,35))
fxdataicon = ctk.CTkLabel(graph, text=None, image=fxdataiconimg)
fxdata = ctk.CTkTextbox(graph, font=("Montserrat", 15),
                        height=250, width=90, text_color="black",
                        fg_color="white", state="disabled")
# f(x) results 

gxdataiconimg = ctk.CTkImage(Image.open("/images/xfunctg.png"), size=(55,35))
gxdataicon = ctk.CTkLabel(graph, text=None, image=gxdataiconimg)
gxdata = ctk.CTkTextbox(graph, font=("Montserrat", 15),
                        height=250, width=90, text_color="black",
                        fg_color="white", state="disabled")
# g(x) results

graph_rearrange()



# [CONVERSION] -------



# These are just banners - user interface cosmetic
banner_v = ctk.CTkLabel(conv, text="  Conversion", font=("segoe ui bold", 35),
                         height=70, width=420, fg_color="deepskyblue4", anchor="w")
banner_v.place(x=0,y=0)
banner_v2 = ctk.CTkLabel(conv, text=None, fg_color="deepskyblue3", height=70,
                          width=160)
banner_v2.place(x=419,y=0)
banner_v3 = ctk.CTkLabel(conv, text=None, fg_color="deepskyblue2", height=70,
                          width=160)
banner_v3.place(x=578,y=0)

# 1 - Length
# 2 - Area
# 3 - Weight
# 4 - Volume
# 5 - Temperature
# 6 - Speed

topicfocus = ""
focus_v = ""
focusbutton_v = 0
def topicselect():
    # Opens a new window to allow the
    # user to select a conversion topic
    viewvalue = tk.IntVar(value="0")
    def changeview():
        prompt = viewvalue.get()
        global selecticonimg
        global selecticon
        global unitinfo
        global topicfocus
        selecticon.place_forget()
        unitinfo.delete("1.0", ctk.END)

        if prompt == 1: # Length
            topicfocus = "length"
            top_options.configure(values=["Millimeter (mm)","Kilometer (Km)",
                               "Centimeter (cm)","Meter (M)",
                               "Yard (Yd)","Foot (Ft)",
                               "Mile (Mi)", "Inch (In)"])
            bot_options.configure(values=["Millimeter (mm)","Kilometer (Km)",
                               "Centimeter (cm)","Meter (M)",
                               "Yard (Yd)","Foot (Ft)",
                               "Mile (Mi)", "Inch (In)"])
            
            # Topic Window ---
            units = """• Millimeter  • Kilometer
• Centimeter  • Meter
• Yard  • Foot
• Mile  • Inch"""
            unitinfo.insert("1.0", units)
            selecticonimg = ctk.CTkImage(Image.open("\images\length.png"), size=(90,90))
            selecticon.configure(image=selecticonimg) # Conversion topic icon
            selecticon.place(x=180, y=114)

            # Main Window ---
            conviconimg = ctk.CTkImage(Image.open("\images\length.png"), size=(100,100))
            convicon.configure(image=conviconimg)
            convicon.place(x=550,y=70)
            convlabel.configure(text="Length")
            convlabel.place(x=550,y=160)

        elif prompt == 2: # Area
            topicfocus = "area"
            top_options.configure(values=["Square Meter (M²)","Square Decimeter (dm²)",
                               "Square Centimeter (cm²)","Square Kilometer (Km²)",
                               "Square Millimeter (mm²)"])
            bot_options.configure(values=["Square Meter (M²)","Square Decimeter (dm²)",
                               "Square Centimeter (cm²)","Square Kilometer (Km²)",
                               "Square Millimeter (mm²)"])
            
            # Topic Window ---
            units = """• Square Meter
• Square Decimeter
• Square Centimeter  
• Square Kilometer
• Square Millimeter"""
            unitinfo.insert("1.0", units)            
            selecticonimg = ctk.CTkImage(Image.open("\images\carea.png"), size=(90,90))
            selecticon.configure(image=selecticonimg)
            selecticon.place(x=180, y=114)

            # Main Window ---
            conviconimg = ctk.CTkImage(Image.open("\images\carea.png"), size=(100,100))
            convicon.configure(image=conviconimg)
            convicon.place(x=550,y=69)
            convlabel.configure(text="Area")
            convlabel.place(x=570,y=161)

        # ↓ ↓ ↓ Same process as above, just with "units" text and different image icons
        elif prompt == 3: # Weight
            topicfocus = "weight"
            top_options.configure(values=["Gram (g)","Milligram (mg)",
                               "Kilogram (Kg)","Pound (lb)",
                               "Tonne (T)"])
            bot_options.configure(values=["Gram (g)","Milligram (mg)",
                               "Kilogram (Kg)","Pound (lb)",
                               "Tonne (T)"])

            # Topic Window --- 
            units = """• Gram  • Milligram
• Kilogram  • Pound
• Tonne"""
            unitinfo.insert("1.0", units)             
            selecticonimg = ctk.CTkImage(Image.open("\images\weight.png"), size=(90,90))
            selecticon.configure(image=selecticonimg)
            selecticon.place(x=180, y=114)        
        
            # Main Window ---
            conviconimg = ctk.CTkImage(Image.open("\images\weight.png"), size=(100,100))
            convicon.configure(image=conviconimg)
            convicon.place(x=550,y=70)
            convlabel.configure(text="Weight")
            convlabel.place(x=550,y=160)

        elif prompt == 4: # Volume
            topicfocus = "volume"
            # Configures both option menus to have these options:
            # Same process for all other conversion topics, except
                                    # with their own measure units
            top_options.configure(values=["Millilitre (ml)","Litre (L)",
                               "UK Gallon (UK Gal)","UK Fluid Ounce (UK fl oz)"])
            bot_options.configure(values=["Millilitre (ml)","Litre (L)",
                               "UK Gallon (UK Gal)","UK Fluid Ounce (UK fl oz)"])

            # Topic Window ---
            units = """• Millilitre  • Litre
• UK Gallon  
• UK Fluid Ounce"""
            unitinfo.insert("1.0", units)            
            selecticonimg = ctk.CTkImage(Image.open("\images\cvolume.png"), size=(90,90))
            selecticon.configure(image=selecticonimg)
            selecticon.place(x=180, y=114)

            # Main Window ---
            conviconimg = ctk.CTkImage(Image.open("\images\cvolume.png"), size=(100,100))
            convicon.configure(image=conviconimg) # Configures the image
            convicon.place(x=550,y=70)            # to be a volume icon
            convlabel.configure(text="Volume") # Configures the text label
            convlabel.place(x=547,y=162)
            # ↑ ↑ ↑ Same process for all other conversion topics

        elif prompt == 5: # Temperature
            topicfocus = "temp"
            top_options.configure(values=["Celsius (°C)","Fahrenheit (°F)",
                               "Kelvin (K)"])
            bot_options.configure(values=["Celsius (°C)","Fahrenheit (°F)",
                               "Kelvin (K)"])
            
            # Topic Window ---
            units = """• Celsius
• Fahrenheit
• Kelvin"""
            unitinfo.insert("1.0", units)
            selecticonimg = ctk.CTkImage(Image.open("\images\ctemp.png"), size=(90,90))
            selecticon.configure(image=selecticonimg)
            selecticon.place(x=180, y=114)
        
            # Main Window ---
            conviconimg = ctk.CTkImage(Image.open("\images\ctemp.png"), size=(100,100))
            convicon.configure(image=conviconimg)
            convicon.place(x=550,y=70)
            convlabel.configure(text="Temperature")
            convlabel.place(x=510,y=163)

        elif prompt == 6: # Speed
            topicfocus = "speed"
            top_options.configure(values=["Miles/hour (MPH)","Meters/second (m/s)",
                               "Kilometers/second (km/s)"])
            bot_options.configure(values=["Miles/hour (MPH)","Meters/second (m/s)",
                               "Kilometers/second (km/s)"])
            
            # Topic Window ---
            units = """• Miles/hour
• Kilometers/second
• Meters/second"""
            unitinfo.insert("1.0", units)
            selecticonimg = ctk.CTkImage(Image.open("\images\speed.png"), size=(90,90))
            selecticon.configure(image=selecticonimg)
            selecticon.place(x=180, y=114)

            # Main Window ---
            conviconimg = ctk.CTkImage(Image.open("\images\speed.png"), size=(100,100))
            convicon.configure(image=conviconimg)
            convicon.place(x=550,y=70)
            convlabel.configure(text="Speed")
            convlabel.place(x=555,y=160)
        
        # Enables the user to use the Option Menus after a conversion
                                              # topic has been chosen
        top_options.configure(state="normal")
        bot_options.configure(state="normal")
        top_options.set("...")
        bot_options.set("...")
    global roottop
    try:
        if roottop.winfo_exists():
            return
    except:
        pass
    roottop = ctk.CTkToplevel()
    roottop.geometry("345x200+1020+40")
    roottop.title("Conversion Topic Selection")
    roottop.resizable(0,0)

    miscbox_t = ctk.CTkLabel(roottop, # an area for misc buttons
                            height=49, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_t.place(x=300,y=140)

    closewindow = ctk.CTkButton(roottop, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=roottop.destroy)
    closewindow.place(x=303,y=145)
    
    # ---
    global selecticon
    global selecticonimg
    global unitinfo

    # Default conversion topic upon selection
    unitinfo = ctk.CTkTextbox(roottop, width=215, height=105, font=("segoe ui", 17))
    unitinfo.place(x=118, y=10)

    selecticonimg = ctk.CTkImage(Image.open("\images\length.png"), size=(90,90))
    selecticon = ctk.CTkLabel(roottop, text=None, image=selecticonimg)
    selecticon.place(x=180, y=114)

    # All of the conversion topics ---
    length = ctk.CTkRadioButton(roottop, text="Length", command=changeview,
                                variable=viewvalue, value="1", 
                                font=("segoe ui bold", 16), fg_color="deepskyblue4")
    length.place(x=12,y=10) # 1 - Length
    
    area = ctk.CTkRadioButton(roottop, text="Area", command=changeview, variable=
                              viewvalue, value="2", font=("segoe ui bold", 16),
                              fg_color="deepskyblue4")
    area.place(x=12,y=40) # 2 - Area

    weight = ctk.CTkRadioButton(roottop, text="Weight", command=changeview, variable=
                              viewvalue, value="3", font=("segoe ui bold", 16),
                              fg_color="deepskyblue4")
    weight.place(x=12,y=70) # 3 - Weight
    
    volume = ctk.CTkRadioButton(roottop, text="Volume", command=changeview, variable=
                              viewvalue, value="4", font=("segoe ui bold", 16),
                              fg_color="deepskyblue4")
    volume.place(x=12,y=100) # 4 - Volume
    
    temp = ctk.CTkRadioButton(roottop, text="Temperature", command=changeview, variable=
                              viewvalue, value="5", font=("segoe ui bold", 16),
                              fg_color="deepskyblue4")
    temp.place(x=12,y=130) # 5 - Temperature

    speed = ctk.CTkRadioButton(roottop, text="Speed", command=changeview, variable=
                              viewvalue, value="6", font=("segoe ui bold", 16),
                              fg_color="deepskyblue4")
    speed.place(x=12,y=160) # 6 - Speed

    changeview()
    units = """Select a Topic..."""
    unitinfo.insert("1.0", units)
    roottop.attributes("-topmost", True)

def opennumpad_conv():
    global rootnum
    try:
        if rootnum.winfo_exists():
            return
    except:
        pass
    rootnum = ctk.CTkToplevel()
    rootnum.geometry("345x185+1020+335")
    rootnum.title("Conversion Number Keyboard")
    rootnum.resizable(0,0)

    miscbox_c = ctk.CTkLabel(rootnum, # an area for misc buttons
                            height=130, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=300,y=46)

    closewindow = ctk.CTkButton(rootnum, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootnum.destroy)
    closewindow.place(x=303,y=130)

    select = ctk.CTkImage(Image.open("\images\ctypingcursor.png"), size=(25,25))
    focusoption = ctk.CTkButton(rootnum, # Focus typing on another entry
                      height=40, width=40, text=None, image=select,
                      fg_color="grey12", hover_color="grey26", corner_radius=0)
    focusoption.place(x=303,y=50)
    
    # ---

    topfocus = ctk.CTkImage(Image.open("/images/uppertype.png"))
    botfocus = ctk.CTkImage(Image.open("/images/lowertype.png"))
    def focustyping_v():
        global focusbutton_v
        global focus_v
        global focustyping_v
        if focusbutton_v == 0:
            focusoption.configure(image=topfocus)
            focusbutton_v = 1
            focus_v = inputoutputTOP_v
        elif focusbutton_v == 1:
            focusoption.configure(image=botfocus)
            focusbutton_v = 0        
            focus_v = inputoutputBOT_v
    focusoption.configure(command=focustyping_v)
    focustyping_v()
    
    def numpadbind(insert):
        if insert == "paste":
            focus_v.insert(ctk.INSERT, inputoutput.get())
        else:
            focus_v.insert(ctk.INSERT, insert)
        
        if focus_v == inputoutputTOP_v:
            evaluateTOPtoBOT_v(None)
        elif focus_v == inputoutputBOT_v:
            evaluateBOTtoTOP_v(None)
    
    pasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    paste = ctk.CTkButton(rootnum, image=pasteimg,
                      height=40, width=40, text=None,
                      fg_color="grey12", hover_color="grey26", corner_radius=0,
                      command=lambda: numpadbind(insert="paste"))
    paste.place(x=303, y=90)

    num1 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="1",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="1"))
    num1.place(x=24,y=15)

    num2 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="2",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="2"))
    num2.place(x=114,y=15)

    num3 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="3",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="3"))
    num3.place(x=204,y=15)

    num4 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="4",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="4"))
    num4.place(x=24,y=55)

    num5 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="5",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="5"))
    num5.place(x=114,y=55)

    num6 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="6",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="6"))
    num6.place(x=204,y=55)

    num7 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="7",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="7"))
    num7.place(x=24,y=95)

    num8 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="8",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="8"))
    num8.place(x=114,y=95)

    num9 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="9",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="9"))
    num9.place(x=204,y=95)

    decimal = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text=".",
                    fg_color="grey19", hover_color="grey26",
                    command=lambda: numpadbind(insert="."))
    decimal.place(x=24,y=135)

    num0 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="0",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="0"))
    num0.place(x=114,y=135)

    x_variable = ctk.CTkButton(rootnum, font=("STIX Two Text italic", 21), height=37,
                           width=42, text_color="white", text="x", 
                           fg_color="grey19", hover_color="grey26",
                           command=lambda: numpadbind(insert="x"))
    x_variable.place(x=204, y=135)

    y_variable = ctk.CTkButton(rootnum, font=("STIX Two Text italic", 21), height=37,
                           width=42, text_color="white", text="y",
                           fg_color="grey19", hover_color="grey26",
                           command=lambda: numpadbind(insert="y"))
    y_variable.place(x=248, y=135)
    rootnum.attributes("-topmost", True)

def misc_co():
    miscbox_c = ctk.CTkLabel(conv, # an area for misc buttons
                            height=167.5, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=705,y=205)

    close_windowimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
    close_window_c = ctk.CTkButton(conv, height=40, width=40, text=None,
                                 fg_color="grey12", image=close_windowimg, command=shutdown,
                                 hover_color="red4", corner_radius=0)
    close_window_c.place(x=708,y=328)

    infoimg = ctk.CTkImage(Image.open("\images\info.png"))
    info = ctk.CTkButton(conv, image=infoimg,
                         height=40, width=40, text=None, corner_radius=0,
                         fg_color="grey12", hover_color="grey26", command=information)
    info.place(x=708, y=288)

    xyimg = ctk.CTkImage(Image.open("\images\cvariables.png"))
    xy_c = ctk.CTkButton(conv, image=xyimg,
                       height=40, width=40, text=None, command=editvariable,
                       fg_color="grey12", hover_color="grey26", corner_radius=0)
    xy_c.place(x=708,y=248)

    numpadimg = ctk.CTkImage(Image.open("\images\cnumbers.png"))
    numpad = ctk.CTkButton(conv, image=numpadimg,
                           height=40, width=40, text=None, command=opennumpad_conv,
                           fg_color="grey12", hover_color="grey26", corner_radius=0)
    numpad.place(x=708, y=208)
misc_co()

# -----------------

# Dictionaries

length = {
# mm to...
"mm_mm": "1",
"mm_Km": "0.000001",
"mm_cm": "0.1",
"mm_M": "0.001",
"mm_Yd": "0.00109361",
"mm_Ft": "0.00328084",
"mm_Mi": "0.000000621371",
"mm_In": "0.0393701",

# Km to..
"Km_mm": "1000000",
"Km_Km": "1",
"Km_cm": "100000",
"Km_M": "1000",
"Km_Yd": "1094.0",
"Km_Ft": "3280.84",
"Km_Mi": "0.621371",
"Km_In": "39370.1",

# cm to...
"cm_mm": "10",
"cm_Km": "0.00001",
"cm_cm": "1",
"cm_M": "0.01",
"cm_Yd": "0.0109361",
"cm_Ft": "0.0328084",
"cm_Mi": "0.00000621371",
"cm_In": "0.393701",

# M to...
"M_mm": "1000",
"M_Km": "0.001",
"M_cm": "100",
"M_M": "1",
"M_Yd": "1.09361",
"M_Ft": "3.28084",
"M_Mi": "0.000621371",
"M_In": "39.3701",

# Yd to...
"Yd_mm": "914.4",
"Yd_Km": "0.0009144",
"Yd_cm": "91.44",
"Yd_M": "0.9144",
"Yd_Yd": "1",
"Yd_Ft": "3",
"Yd_Mi": "0.000568182",
"Yd_In": "36",

# Ft to...
"Ft_mm": "304.8",
"Ft_Km": "0.0003048",
"Ft_cm": "30.48",
"Ft_M": "0.3048",
"Ft_Yd": "0.333333",
"Ft_Ft": "1",
"Ft_Mi": "0.000189394",
"Ft_In": "12",

# Mi to...
"Mi_mm": "1609344",
"Mi_Km": "1.60934",
"Mi_cm": "160934.4",
"Mi_M": "1609.34",
"Mi_Yd": "1760",
"Mi_Ft": "5280",
"Mi_Mi": "1",
"Mi_In": "63360",

# In to...
"In_mm": "25.4",
"In_Km": "0.0000254",
"In_cm": "2.54",
"In_M": "0.0254",
"In_Yd": "0.0277778",
"In_Ft": "0.0833333",
"In_Mi": "0.0000157828",
"In_In": "1",
}

# Same concept as above, just with their own units
area = {
    # M² to...
    "M²_M²": "1",
    "M²_dm²": "100",
    "M²_cm²": "10000",
    "M²_Km²": "0.000001",
    "M²_mm²": "1000000",
    
    # dm² to...
    "dm²_M²": "0.01",
    "dm²_dm²": "1",
    "dm²_cm²": "100",
    "dm²_Km²": "0.0000001",
    "dm²_mm²": "10000",
    
    # cm² to...
    "cm²_M²": "0.0001",
    "cm²_dm²": "0.01",
    "cm²_cm²": "1",
    "cm²_Km²": "0.0000000001",
    "cm²_mm²": "100",
    
    # Km² to...
    "Km²_M²": "1000000",
    "Km²_dm²": "100000000",
    "Km²_cm²": "10000000000",
    "Km²_Km²": "1",
    "Km²_mm²": "1000000000000",
    
    # mm² to...
    "mm²_M²": "0.000001",
    "mm²_dm²": "0.0001",
    "mm²_cm²": "0.01",
    "mm²_Km²": "0.000000000001",
    "mm²_mm²": "1"
}

weight = {
# g to...
"g_g": "1",
"g_mg": "1000",
"g_Kg": "0.001",
"g_lb": "0.00220462",
"g_T": "0.000001",

# mg to...
"mg_g": "0.001",
"mg_mg": "1",
"mg_Kg": "0.000001",
"mg_lb": "0.00000220462",
"mg_T": "0.000000001",

# Kg to...
"Kg_g": "1000",
"Kg_mg": "1000000",
"Kg_Kg": "1",
"Kg_lb": "2.20462",
"Kg_T": "0.001",

# lb to...
"lb_g": "453.592",
"lb_mg": "453592",
"lb_Kg": "0.453592",
"lb_lb": "1",
"lb_T": "0.000453592",

# T to...
"T_g": "1000000",
"T_mg": "1000000000",
"T_Kg": "1000",
"T_lb": "2204.62",
"T_T": "1"
}

volume = {
# ml to...
"ml_ml": "1",
"ml_L": "0.001",
"ml_UK Gal": "0.000219969",
"ml_UK fl oz": "0.0351951",

# L to...
"L_ml": "1000",
"L_L": "1",
"L_UK Gal": "0.219969",
"L_UK fl oz": "35.1951",

# UK Gal to...
"UK Gal_ml": "4546.09",
"UK Gal_L": "4.54609",
"UK Gal_UK Gal": "1",
"UK Gal_UK fl oz": "160",

# UK fl oz to...
"UK fl oz_ml": "28.4131",
"UK fl oz_L": "0.0284131",
"UK fl oz_UK Gal": "0.00625",
"UK fl oz_UK fl oz": "1"
}

speed = {
# MPH to...
"MPH_MPH": "1",
"MPH_m/s": "0.44704",
"MPH_km/s": "0.00160934",

# m/s to...
"m/s_MPH": "2.23694",
"m/s_m/s": "1",
"m/s_km/s": "0.001",

# km/s to...
"km/s_MPH": "3600",
"km/s_m/s": "1000",
"km/s_km/s": "1"
}

def evaluateTOPtoBOT_v(event): # Converting the top value to
    global answer_v                             # the bottom
    # Resets the error handling.
    inputoutputTOP_v.configure(border_color="grey14",
                               border_width=4)
    inputoutputBOT_v.configure(border_color="grey14",
                               border_width=4)

    if inputoutputTOP_v.get() == "":
        inputoutputBOT_v.delete(0, ctk.END)
        return

    # When the user focuses on an entry box, the text turns bold
    inputoutputTOP_v.configure(font=("segoe ui bold", 60))
    # Bottom entry is cleared for the answer
    inputoutputBOT_v.delete(0, ctk.END)
    from_unit = top_options.get()
    to_unit = bot_options.get()
    
    # Conversion process
    try:
        formula = from_unit + "_" + to_unit # Creates an expression
        convert = inputoutputTOP_v.get() # i.e. from_input = mm
                                         # to_input = Yd
                                         # mm_Yd
        if "x" in convert or "y" in convert: 
            convert = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", convert))
        
        if topicfocus == "length":          
            # Processes
            formula = formula.replace("Millimeter (mm)", "mm")
            formula = formula.replace("Kilometer (Km)", "Km")
            formula = formula.replace("Centimeter (cm)", "cm")
            formula = formula.replace("Meter (M)", "M")
            formula = formula.replace("Yard (Yd)", "Yd")
            formula = formula.replace("Foot (Ft)", "Ft")
            formula = formula.replace("Mile (Mi)", "Mi")
            formula = formula.replace("Inch (In)", "In")
            
            # Evaluates the value (i.e. 25 and mm_Yd → 25 * 0.00109361)
            answer = float(convert)*float(length[formula])
            
        # ↓ ↓ ↓ Same process above, just with different 
        # units using their own respective dictionary     
        if topicfocus == "area":
            formula = formula.replace("Square Meter (M²)", "M²")
            formula = formula.replace("Square Decimeter (dm²)", "dm²")
            formula = formula.replace("Square Centimeter (cm²)", "cm²")
            formula = formula.replace("Square Kilometer (Km²)", "Km²")
            formula = formula.replace("Square Millimeter (mm²)", "mm²")

            answer = float(convert)*float(area[formula])    
        
        elif topicfocus == "weight":
            formula = formula.replace("Gram (g)", "g")
            formula = formula.replace("Milligram (mg)", "mg")
            formula = formula.replace("Kilogram (Kg)", "Kg")
            formula = formula.replace("Pound (lb)", "lb")
            formula = formula.replace("Tonne (T)", "T")

            answer = float(convert)*float(weight[formula])

        elif topicfocus == "volume":
            formula = formula.replace("Millilitre (ml)", "ml")
            formula = formula.replace("Litre (L)", "L")
            formula = formula.replace("UK Gallon (UK Gal)", "UK Gal")
            formula = formula.replace("UK Fluid Ounce (UK fl oz)", "UK fl oz")

            answer = float(convert)*float(volume[formula])
        
        elif topicfocus == "temp":
            from_unit = from_unit.replace("Celsius (°C)", "°C")
            from_unit = from_unit.replace("Fahrenheit (°F)", "°F")
            from_unit = from_unit.replace("Kelvin (K)", "K")
            
            to_unit = to_unit.replace("Celsius (°C)", "°C")
            to_unit = to_unit.replace("Fahrenheit (°F)", "°F")
            to_unit = to_unit.replace("Kelvin (K)", "K")
            
            convert = float(convert)

            # Formulas
            if from_unit == "°C" and to_unit == "°C":
                answer_v = convert * 1
            elif from_unit == "°C" and to_unit == "°F":
                answer_v = (convert * 9/5) + 32
            elif from_unit == "°C" and to_unit == "K":
                answer_v = convert + 273.15
            elif from_unit == "°F" and to_unit == "°F":
                answer_v = convert * 1
            elif from_unit == "°F" and to_unit == "°C":
                answer_v = (convert - 32) * 5/9
            elif from_unit == "°F" and to_unit == "K":
                answer_v = (convert - 32) * 5/9 + 273.15
            elif from_unit == "K" and to_unit == "°C":
                answer_v = convert - 273.15
            elif from_unit == "K" and to_unit == "°F":
                answer_v = (convert - 273.15) * 9/5 + 32
            elif from_unit == "K" and to_unit == "K":
                answer_v = convert*1
            answer = answer_v

        elif topicfocus == "speed":
            formula = formula.replace("Miles/hour (MPH)", "MPH")
            formula = formula.replace("Meters/second (m/s)", "m/s")
            formula = formula.replace("Kilometers/second (km/s)", "km/s")

            answer = float(convert)*float(speed[formula])

        inputoutputBOT_v.insert(ctk.INSERT, answer)
        inputoutputBOT_v.configure(font=("segoe ui", 60))
    
    except: # Error handling
        inputoutputTOP_v.configure(border_color="red2",
                                   border_width=2)

# Same process as above, just in the context of
                             # the bottom entry
def evaluateBOTtoTOP_v(event):
    inputoutputTOP_v.configure(border_color="grey14",
                               border_width=4)
    inputoutputBOT_v.configure(border_color="grey14",
                               border_width=4)

    if inputoutputBOT_v.get() == "":
        inputoutputTOP_v.delete(0, ctk.END)
        return
    
    inputoutputBOT_v.configure(font=("segoe ui bold", 60))
    inputoutputTOP_v.delete(0, ctk.END)
    from_unit = bot_options.get()
    to_unit = top_options.get()

    try:
        formula = from_unit + "_" + to_unit
        convert = inputoutputBOT_v.get()
        if "x" in convert or "y" in convert: 
            convert = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", convert))
        if topicfocus == "length":
            formula = formula.replace("Millimeter (mm)", "mm")
            formula = formula.replace("Kilometer (Km)", "Km")
            formula = formula.replace("Centimeter (cm)", "cm")
            formula = formula.replace("Meter (M)", "M")
            formula = formula.replace("Yard (Yd)", "Yd")
            formula = formula.replace("Foot (Ft)", "Ft")
            formula = formula.replace("Mile (Mi)", "Mi")
            formula = formula.replace("Inch (In)", "In")
                
            answer = float(convert)*float(length[formula])
            
        if topicfocus == "area":
            formula = formula.replace("Square Meter (M²)", "M²")
            formula = formula.replace("Square Decimeter (dm²)", "dm²")
            formula = formula.replace("Square Centimeter (cm²)", "cm²")
            formula = formula.replace("Square Kilometer (Km²)", "Km²")
            formula = formula.replace("Square Millimeter (mm²)", "mm²")

            answer = float(convert)*float(area[formula])    
        
        elif topicfocus == "weight":
            formula = formula.replace("Gram (g)", "g")
            formula = formula.replace("Milligram (mg)", "mg")
            formula = formula.replace("Kilogram (Kg)", "Kg")
            formula = formula.replace("Pound (lb)", "lb")
            formula = formula.replace("Tonne (T)", "T")

            answer = float(convert)*float(weight[formula])

        elif topicfocus == "volume":
            formula = formula.replace("Millilitre (ml)", "ml")
            formula = formula.replace("Litre (L)", "L")
            formula = formula.replace("UK Gallon (UK Gal)", "UK Gal")
            formula = formula.replace("UK Fluid Ounce (UK fl oz)", "UK fl oz")

            answer = float(convert)*float(volume[formula])
        
        elif topicfocus == "temp":
            from_unit = from_unit.replace("Celsius (°C)", "°C")
            from_unit = from_unit.replace("Fahrenheit (°F)", "°F")
            from_unit = from_unit.replace("Kelvin (K)", "K")
            
            to_unit = to_unit.replace("Celsius (°C)", "°C")
            to_unit = to_unit.replace("Fahrenheit (°F)", "°F")
            to_unit = to_unit.replace("Kelvin (K)", "K")
            
            convert = float(convert)

            if from_unit == "°C" and to_unit == "°C":
                answer_v = convert * 1
            elif from_unit == "°C" and to_unit == "°F":
                answer_v = (convert * 9/5) + 32
            elif from_unit == "°C" and to_unit == "K":
                answer_v = convert + 273.15
            elif from_unit == "°F" and to_unit == "°F":
                answer_v = convert * 1
            elif from_unit == "°F" and to_unit == "°C":
                answer_v = (convert - 32) * 5/9
            elif from_unit == "°F" and to_unit == "K":
                answer_v = (convert - 32) * 5/9 + 273.15
            elif from_unit == "K" and to_unit == "°C":
                answer_v = convert - 273.15
            elif from_unit == "K" and to_unit == "°F":
                answer_v = (convert - 273.15) * 9/5 + 32
            elif from_unit == "K" and to_unit == "K":
                answer_v = convert*1
            answer = answer_v

        elif topicfocus == "speed":
            formula = formula.replace("Miles/hour (MPH)", "MPH")
            formula = formula.replace("Meters/second (m/s)", "m/s")
            formula = formula.replace("Kilometers/second (km/s)", "km/s")

            answer = float(convert)*float(speed[formula])

        inputoutputTOP_v.insert(ctk.INSERT, answer)
        inputoutputTOP_v.configure(font=("segoe ui", 60))
    except:
        inputoutputBOT_v.configure(border_color="red2",
                                   border_width=2)

inputoutputTOP_v = ctk.CTkEntry(conv, width=500, height=140, font=("segoe ui", 60),
                       fg_color="grey17", border_color="grey14", border_width=4,
                       corner_radius=8)
# These are the exact same attributes as the bottom entry
inputoutputTOP_v.place(x=0,y=80) # Top input/output entry

top_options = ctk.CTkOptionMenu(conv, state="disabled", bg_color="grey17",
                                fg_color="grey17", font=("segoe ui", 16),
                                button_color="grey17", dropdown_fg_color="grey12",
                                dropdown_font=("Montserrat italic", 13), 
                                dropdown_hover_color="deepskyblue4",
                                button_hover_color="grey14",
                                width=487, command=None, values=["..."])
top_options.set("") # Option menu for the top entry
top_options.place(x=5,y=185)

# As soon as a value is entered in the top 
# entry, it is immidietly converted so the user
# doesn't neet to press a button 
inputoutputTOP_v.bind("<KeyRelease>", evaluateTOPtoBOT_v)

inputoutputBOT_v = ctk.CTkEntry(conv, width=500, height=140, font=("segoe ui", 60),
                       fg_color="grey17", border_color="grey14", border_width=4,
                       corner_radius=8)
inputoutputBOT_v.place(x=0,y=230) # Bottom input/output entry

bot_options = ctk.CTkOptionMenu(conv, state="disabled", bg_color="grey17",
                                fg_color="grey17", font=("segoe ui", 16),
                                button_color="grey17", dropdown_fg_color="grey12",
                                dropdown_font=("Montserrat italic", 13), 
                                dropdown_hover_color="deepskyblue4",
                                button_hover_color="grey14",
                                width=487, command=None, values=["..."])
bot_options.set("") # Option menu for the bottom entry
bot_options.place(x=5,y=336)

inputoutputBOT_v.bind("<KeyRelease>", evaluateBOTtoTOP_v)

# ---

def backspace_v():
    expression = root.focus_get().get()
    root.focus_get().delete(len(expression)-1, ctk.END)

def clearall_v():
    inputoutputTOP_v.delete(0, ctk.END)
    inputoutputBOT_v.delete(0, ctk.END)

bksp_vimg = ctk.CTkImage(Image.open("\images\down.png"), size=(30,30))
bksp_v = ctk.CTkButton(conv, image=bksp_vimg, text=None,
                       hover_color="red4", fg_color="grey14",
                       width=95, height=65, border_color="deepskyblue4", border_width=2,
                       command=backspace_v) # Backspace
bksp_v.place(x=605,y=230)

clear_vimg = ctk.CTkImage(Image.open("\images\clear.png"), size=(30,30))
clear_v = ctk.CTkButton(conv, image=clear_vimg, text=None,
                        hover_color="red4", fg_color="grey14",
                        width=95, height=65, border_color="red2", border_width=2,
                        text_color="red2", command=clearall_v)
clear_v.place(x=505,y=230) # Clear both enteries

topicselectionimg = ctk.CTkImage(Image.open("\images\menu.png"), size=(35,35))
topicselection = ctk.CTkButton(conv, image=topicselectionimg, text="Topic Selection",
                               font=("segoe ui bold",18), hover_color="grey26", fg_color=
                               "grey14", border_color="deepskyblue4", border_width=2,
                               width=196, height=70, command=topicselect)
topicselection.place(x=505,y=300) # Opens the conversoin topic selection window

conv_lineimg = ctk.CTkImage(Image.open("\images\line_2bgrey.png"), size=(193,30))
conv_line = ctk.CTkLabel(conv, text=None, image=conv_lineimg)
conv_line.place(x=505, y=200)

convicon = ctk.CTkLabel(conv, text=None, image=None)
convlabel = ctk.CTkLabel(conv, text="Select a\nconversion\ntopic...", 
                         font=("segoe ui bold", 30))
convlabel.place(x=525,y=80)



# [MATH BOX] EXTRA MODE --- 



# These are just banners - user interface cosmetic
banner_m = ctk.CTkLabel(box, text="  Math Box", font=("segoe ui bold", 35),
                         height=70, width=420, fg_color="deepskyblue4", anchor="w")
banner_m.place(x=0,y=0)
banner_m2 = ctk.CTkLabel(box, text=None, fg_color="deepskyblue3", height=70,
                          width=160)
banner_m2.place(x=419,y=0)
banner_m3 = ctk.CTkLabel(box, text=None, fg_color="deepskyblue2", height=70,
                          width=160)
banner_m3.place(x=578,y=0)

def opennumpad_m():
    global focus_m
    global rootnum
    try:
        if rootnum.winfo_exists():
            return
    except:
        pass
    rootnum = ctk.CTkToplevel()
    rootnum.geometry("345x185+1020+335")
    rootnum.title("Math Box Number Keyboard")
    rootnum.resizable(0,0)

    def numpadbind(insert):
        if insert == "paste":
            focus_m.insert(ctk.INSERT, inputoutput.get())
        else:
            focus_m.insert(ctk.INSERT, insert)

        if focus_m == heads_input:
            autoprob_heads(None)
        elif focus_m == outcome_input:
            updateslider(None)

    miscbox_c = ctk.CTkLabel(rootnum, # an area for misc buttons
                            height=88, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_c.place(x=300,y=86)

    closewindow = ctk.CTkButton(rootnum, image=close_windowimg,
                            height=40, width=40, text=None,
                            fg_color="grey12", hover_color="red4", corner_radius=0,
                            command=rootnum.destroy)
    closewindow.place(x=303,y=130) # Button to close the numpad

    pasteimg = ctk.CTkImage(Image.open("\images\paste_white.png"))
    paste = ctk.CTkButton(rootnum, image=pasteimg, # Pastes the CALCULATE value into
                      height=40, width=40, text=None, #                    the entry
                      fg_color="grey12", hover_color="grey26", corner_radius=0,
                      command=lambda: numpadbind(insert="paste"))
    paste.place(x=303, y=90)

    num1 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 1
                    height=37, width=87, text_color="white", text="1",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="1"))
    num1.place(x=24,y=15)

    num2 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 2
                    height=37, width=87, text_color="white", text="2",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="2"))
    num2.place(x=114,y=15)

    num3 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 3
                    height=37, width=87, text_color="white", text="3",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="3"))
    num3.place(x=204,y=15)

    num4 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 4 etc...
                    height=37, width=87, text_color="white", text="4",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="4"))
    num4.place(x=24,y=55)

    num5 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="5",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="5"))
    num5.place(x=114,y=55)

    num6 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="6",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="6"))
    num6.place(x=204,y=55)

    num7 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="7",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="7"))
    num7.place(x=24,y=95)

    num8 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="8",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="8"))
    num8.place(x=114,y=95)

    num9 = ctk.CTkButton(rootnum, font=("segoe ui", 21),
                    height=37, width=87, text_color="white", text="9",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="9"))
    num9.place(x=204,y=95)

    decimal = ctk.CTkButton(rootnum, font=("segoe ui", 21), # decimal
                    height=37, width=87, text_color="white", text=".",
                    fg_color="grey19", hover_color="grey26",
                    command=lambda: numpadbind(insert="."))
    decimal.place(x=24,y=135)

    num0 = ctk.CTkButton(rootnum, font=("segoe ui", 21), # 0
                    height=37, width=177, text_color="white", text="0",
                    fg_color="grey26", hover_color="grey19",
                    command=lambda: numpadbind(insert="0"))
    num0.place(x=114,y=135)

    rootnum.attributes("-topmost", True)

def misc_m():
    miscbox_m = ctk.CTkLabel(box, # an area for misc buttons
                            height=167.5, width=100, text=None,
                            fg_color="grey12", corner_radius=8)
    miscbox_m.place(x=705,y=205)

    close_windowimg = ctk.CTkImage(Image.open("\images\closewindow.png"))
    close_window_m = ctk.CTkButton(box, height=40, width=40, text=None,
                                 fg_color="grey12", image=close_windowimg, command=shutdown,
                                 hover_color="red4", corner_radius=0)
    close_window_m.place(x=708,y=328)

    infoimg = ctk.CTkImage(Image.open("\images\info.png"))
    info = ctk.CTkButton(box, image=infoimg,
                         height=40, width=40, text=None, corner_radius=0,
                         fg_color="grey12", hover_color="grey26", command=information)
    info.place(x=708, y=288)

    xyimg = ctk.CTkImage(Image.open("\images\cvariables.png"))
    xy_m = ctk.CTkButton(box, image=xyimg,
                       height=40, width=40, text=None, command=editvariable,
                       fg_color="grey12", hover_color="grey26", corner_radius=0)
    xy_m.place(x=708,y=248)

    numpadimg = ctk.CTkImage(Image.open("\images\cnumbers.png"))
    numpad = ctk.CTkButton(box, image=numpadimg,
                           height=40, width=40, text=None, command=opennumpad_m,
                           fg_color="grey12", hover_color="grey26", corner_radius=0)
    numpad.place(x=708, y=208)
misc_m()

# ---

def mathbox_rearrange(): # Rarranges the widgets based on 
    global focus_m       # if the user chooses coin or dice
    prompt = changeview_m.get()
    if prompt == 1: # Coin
        mathbox_label.place_forget()
        # Unmap the previous main widgets
        coiniconOFF.place_forget()
        diceiconON.place_forget()
        outcome_label.place_forget()
        outcome_input.place_forget()
        outcome_slider.place_forget()
        
        execute2_m.place_forget()
        clear2_m.place_forget()
        bksp2_m.place_forget()
        
        dicetemplate_3.place_forget()
        dicetemplate_6.place_forget()
        dicetemplate_10.place_forget()
        dicetemplate_100.place_forget()

        customdice.place_forget()
        
        execute2_m.place_forget()
        # Map the main widgets
        biased_setting()
        heads_label.place(x=160, y=95)
        heads_input.place(x=310, y=90)
        heads_p.place(x=493, y=126)

        tails_label.place(x=180, y=170)
        tails_input.place(x=310, y=165)
        tails_p.place(x=493, y=201)

        biasedcoin.place(x=515, y=250)

        execute_m.place(x=190, y=292)

        # Configure the icons
        coiniconON.place(x=15, y=80)
        diceiconOFF.place(x=25,y=230)

        focus_m = heads_input

    elif prompt == 2: # Dice
        mathbox_label.place_forget()
        # Unmap the previous main widgets
        coiniconON.place_forget()
        diceiconOFF.place_forget()

        heads_label.place_forget()
        heads_input.place_forget()
        heads_p.place_forget()

        tails_label.place_forget()
        tails_input.place_forget()
        tails_p.place_forget()

        biasedcoin.place_forget()
        coin5050.place_forget()
        coinbiased.place_forget()

        clear_m.place_forget()
        bksp_m.place_forget()
        execute_m.place_forget()
    
        # Map the main widgets
        dice_setting()
        outcome_label.place(x=190, y=125)
        outcome_input.place(x=190, y=160)

        execute2_m.place(x=190, y=292)

        # Configure the icons
        coiniconOFF.place(x=15, y=80)
        diceiconON.place(x=25, y=230)

        focus_m = outcome_input

def biased_setting():
    prompt = coinsetting.get()
    if prompt == "fair": # Switches to the fair coin
        heads_input.delete(0, ctk.END)
        tails_input.delete(0, ctk.END)
        heads_input.insert(ctk.END, "50") # Equal chances of
        tails_input.insert(ctk.END, "50") # heads and tails
        
        # Disables the entries
        heads_input.configure(state="disabled", fg_color="grey17",
                              border_color="grey17", text_color="grey30")
        tails_input.configure(state="disabled", fg_color="grey17",
                              border_color="grey17", text_color="grey30")
        clear_m.place_forget()
        bksp_m.place_forget()

        # Configures the icon
        coinbiased.place_forget()
        coin5050.place(x=545, y=90)

    elif prompt == "biased": # Switches to the biased coin
        # Enables the entries for custom probaility inputs
        heads_input.configure(state="normal", fg_color="grey14",
                              border_color="grey14", text_color="white")
        tails_input.configure(state="normal", fg_color="grey14",
                              border_color="grey14", text_color="white")
        clear_m.place(x=190, y=240)
        bksp_m.place(x=305,y=240)

        # Configures the icon
        coin5050.place_forget()
        coinbiased.place(x=545, y=90)

def dice_setting():
    prompt = dicesetting.get()
    if prompt == "templates": # Displays presets of dice outcomes
        # Unmaps the previous "custom" widgets
        outcome_slider.place_forget()
        clear2_m.place_forget()
        bksp2_m.place_forget()
        customdice.place(x=505, y=300) # Repositions
                                      # the checkbox

        # Maps the widgets containing presets
        dicetemplate_3.place(x=285, y=110)
        dicetemplate_6.place(x=285, y=185)
        dicetemplate_10.place(x=473, y=110)
        dicetemplate_100.place(x=473, y=185)
        dicetemplate_3.configure(fg_color="grey17", hover_color="dodgerblue4")
        dicetemplate_6.configure(fg_color="grey17", hover_color="dodgerblue4")
        dicetemplate_10.configure(fg_color="grey17", hover_color="dodgerblue4")
        dicetemplate_100.configure(fg_color="grey17", hover_color="dodgerblue4")

        outcome_input.delete(0, ctk.END)
        outcome_input.insert(ctk.END, "0")

        # Disables the entry
        outcome_input.configure(state="disabled", fg_color="grey17",
                                border_color="grey17", text_color="grey30")

    elif prompt == "custom": # Enables the custom input of dice outcomes
        # Unmaps the previous "templates" widgets
        dicetemplate_3.place_forget()
        dicetemplate_6.place_forget()
        dicetemplate_10.place_forget()
        dicetemplate_100.place_forget()
        customdice.place(x=505, y=270) # Repositions the checkbox

        # Maps the widgets for custom inputs
        outcome_slider.place(x=280,y=170)
        clear2_m.place(x=190, y=240)
        bksp2_m.place(x=305,y=240)
        outcome_slider.set(int(outcome_input.get()))

        # Enables the entry
        outcome_input.configure(state="normal", fg_color="grey14",
                                border_color="grey14", text_color="white")

def setoutcome(preset):
    # Resets the foreground colour of the buttons
    dicetemplate_3.configure(fg_color="grey17", hover_color="dodgerblue4")
    dicetemplate_6.configure(fg_color="grey17", hover_color="dodgerblue4")
    dicetemplate_10.configure(fg_color="grey17", hover_color="dodgerblue4")
    dicetemplate_100.configure(fg_color="grey17", hover_color="dodgerblue4")

    outcome_input.configure(state="normal")
    if preset == 3: # Sets the dice to have 3 outcomes
        outcome_input.delete(0, ctk.END)
        outcome_input.insert(ctk.END, "3")
        dicetemplate_3.configure(fg_color="deepskyblue4", 
                                 hover_color="deepskyblue4")

    elif preset == 6: # Sets the dice to have 6 outcomes
        outcome_input.delete(0, ctk.END)
        outcome_input.insert(ctk.END, "6")
        dicetemplate_6.configure(fg_color="deepskyblue4", 
                                 hover_color="deepskyblue4")

    elif preset == 10: # Sets the dice to have 10 outcomes
        outcome_input.delete(0, ctk.END)
        outcome_input.insert(ctk.END, "10")
        dicetemplate_10.configure(fg_color="deepskyblue4", 
                                 hover_color="deepskyblue4")

    elif preset == 100: # Sets the dice to have 100 outcomes
        outcome_input.delete(0, ctk.END)
        outcome_input.insert(ctk.END, "100")
        dicetemplate_100.configure(fg_color="deepskyblue4", 
                                 hover_color="deepskyblue4")
    
    outcome_input.configure(state="disabled")

def updateslider(event):
    # Resets the border colour
    outcome_input.configure(border_color="grey14")

    try: # Attempts to update the slider
        # Checks if the value is 0 or below, or over 1000 
        value = outcome_input.get()
        value = int(eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", value)))
        if value <= 1000 and value >= 1: # ↑ ↑ ↑ Substitutes x and/or y values
            pass
        
        else: # If invalid...
            outcome_input.configure(border_color="red2")
        
        outcome_slider.set(value) # Updates the slider

    except: # If invalid...
        outcome_input.configure(border_color="red2")

def autoprob_heads(event):
    heads_input.configure(border_color="grey14")
    tails_input.configure(border_color="grey14")
    if heads_input.get() == "": # if there's nothing or the user cleared
                                # the heads entry, this function will do nothing
        tails_input.delete(0, ctk.END)
        return
    
    try: # Attempts to calculate the value of tails
        heads_value = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", heads_input.get()))
        calculation = 100 - float(heads_value)
        if calculation <= -1 or calculation >= 101:
            # If this is a negative value or over 100, the entry box outline is
            # coloured red to let the user know that the value provided in heads
            # is invalid
            heads_input.configure(border_color="red2")
            tails_input.delete(0, ctk.END)
            return
        tails_input.delete(0, ctk.END)
        tails_input.insert(ctk.INSERT, str(calculation))
    
    except: # If this results in an error, the entry box is also outlined red
        heads_input.configure(border_color="red2")
        tails_input.delete(0, ctk.END)

# ↓ ↓ ↓ Same function as above, except with tails
def autoprob_tails(event):
    heads_input.configure(border_color="grey14")
    tails_input.configure(border_color="grey14")
    if tails_input.get() == "":
        heads_input.delete(0, ctk.END)
        return    
    
    try:
        tails_value = eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", tails_input.get()))
        calculation = 100 - float(tails_value)
        if calculation <= -1 or calculation >= 101:
            tails_input.configure(border_color="red2")
            heads_input.delete(0, ctk.END)
            return
        heads_input.delete(0, ctk.END)
        heads_input.insert(ctk.INSERT, str(calculation))
    
    except:
        tails_input.configure(border_color="red2")
        heads_input.delete(0, ctk.END)

def updateoutcome(value):
    outcome_input.configure(border_color="grey17")
    outcome_input.delete(0, ctk.END)
    outcome_input.insert(ctk.END, int(value))

def backspace_m():
    expression = root.focus_get().get()
    root.focus_get().delete(len(expression)-1, ctk.END)

def coinclear():
    heads_input.delete(0, ctk.END)
    tails_input.delete(0, ctk.END)

def backspace2_m():
    expression = outcome_input.get()
    outcome_input.delete(len(expression)-1, ctk.END)

norepeat_coin = 0
def evaluate_m(): # Outputs the coin's side
    # Error handling
    try: # Checks if the two percentages total up to 100 or "make sense"
        # the re library replaces the x and/or y values with the value tied to them
        headscount = float(eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", heads_input.get())))
        tailscount = float(eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", tails_input.get())))
        totalcheck = headscount + tailscount
        if totalcheck == 100:
            pass
        else:
            messagebox.showerror("Error",("""[Math ERROR]
Both probabilities you provided do not add up to 100%"""))
            return
    
    except: #  If not, the messagebox will show
        messagebox.showerror("Error",("""[Syntax ERROR]
The calculator couldn't process the probabilities. Try:
• Checking if your values is correct
• No extranous values is entered"""))
        return

    global norepeat_coin
    global rootcoin
    try: # Prevents duplicate windows
        if rootcoin.winfo_exists():
            return
    except:
        pass
    rootcoin = ctk.CTkToplevel()
    rootcoin.geometry("650x300+128+130")
    rootcoin.title("Tossing a coin...")
    rootcoin.resizable(0,0)
    def animation(frame): # Opens a new window, plays the
        global norepeat_coin # animation and shows the result
        resulticon.place_forget()
        resultlabel.place_forget()
        restart_coinimg = ctk.CTkImage(Image.open("\images\crestart_disabled.png"))
        restart_coin.configure(image=restart_coinimg, hover_color="grey12",
                               state="disabled")
        coin_anim.place(x=0,y=0)
        if frame == 1:
            while True: # Prevents quotes from being repeated 2 times
                quote = randint(1,15)
                if quote == norepeat_coin:
                    continue
                else:
                    norepeat_coin = quote
                    inspirational_quote.configure(text=quotes[quote])
                    break
        inspirational_quote.place(x=0, y=270)

        # Animation frames
        if frame == 1: # Frame 1
            coin_anim.configure(image=coin_animimg_frame1)
            coin_anim.after(400, lambda: animation(frame=2))
                            # The number here indicates is the time in ms
                            # when the frame changes
        elif frame == 2: # Frame 2
            coin_anim.configure(image=coin_animimg_frame2)
            coin_anim.after(400, lambda: animation(frame=3))
        elif frame == 3: # Frame 3
            coin_anim.configure(image=coin_animimg_frame3)
            coin_anim.after(400, lambda: animation(frame=4))
        elif frame == 4: # Frame 4
            coin_anim.configure(image=coin_animimg_frame4)
            coin_anim.after(400, lambda: animation(frame=5))
        elif frame == 5: # Frame 5
            coin_anim.configure(image=coin_animimg_frame5)
            coin_anim.after(400, lambda: animation(frame=6))
        elif frame == 6: # Frame 6
            coin_anim.configure(image=coin_animimg_frame6)
            coin_anim.after(400, lambda: animation(frame=7))
        elif frame == 7: # Frame 7
            coin_anim.configure(image=coin_animimg_frame7)
            coin_anim.after(1700, showresult)
    def showresult(): # Shows the outcome
        coin_anim.place_forget()
        inspirational_quote.place_forget()

        p_heads = headscount / 100
        p_tails = tailscount / 100
        outcome = random.random()
        if outcome < p_heads: # Outputs heads
            resulticonimg = ctk.CTkImage(Image.open("\images\heads_result.png"), size=(225,225))
            resulticon.configure(image=resulticonimg) # Icon modified to heads
            resulticon.place(x=0, y=30)

            resultlabel.configure(text="Heads!")
            resultlabel.place(x=220, y=60)

        elif outcome < p_heads + p_tails: # Outputs tails
            resulticonimg = ctk.CTkImage(Image.open("\images\ctails_result.png"), size=(225,225))
            resulticon.configure(image=resulticonimg) # Icon modifid to tails
            resulticon.place(x=0, y=30)

            resultlabel.configure(text="Tails!")
            resultlabel.place(x=220, y=60)

        restart_coinimg = ctk.CTkImage(Image.open("\images\crestart.png"))
        restart_coin.configure(image=restart_coinimg, hover_color="grey26",
                               state="normal") # Allows the user to toss the coin again
                                               # Enabled setting

    def misc():
        global restart_coin
        miscbox = ctk.CTkLabel(rootcoin, # an area for misc buttons
                                height=88, width=100, text=None,
                                fg_color="grey12", corner_radius=8)
        miscbox.place(x=605,y=196)

        closewindow = ctk.CTkButton(rootcoin, image=close_windowimg,
                                height=40, width=40, text=None,
                                fg_color="grey12", hover_color="red4", corner_radius=0,
                                command=rootcoin.destroy)
        closewindow.place(x=608,y=240) # Closes the result window

        restart_coinimg = ctk.CTkImage(Image.open("\images\crestart_disabled.png"))
        restart_coin = ctk.CTkButton(rootcoin, image=restart_coinimg, # Tosses the coin again
                        height=40, width=40, text=None, state="disabled",
                        fg_color="grey12", hover_color="grey12", corner_radius=0,
                        command=lambda: animation(frame=1))
        restart_coin.place(x=608, y=200)

    # Animation frames/images
    # Each frame is denoted by it's number. After the a set amount of time, the frame
    # is changed to another frame by +1
    coin_animimg_frame1 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame1.png"),
                                        size=(650,270))
    coin_animimg_frame2 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame2.png"),
                                        size=(650,270))
    coin_animimg_frame3 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame3.png"),
                                        size=(650,270))
    coin_animimg_frame4 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame4.png"),
                                        size=(650,270))
    coin_animimg_frame5 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame5.png"),
                                        size=(650,270))
    coin_animimg_frame6 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame6.png"),
                                        size=(650,270))
    coin_animimg_frame7 = ctk.CTkImage(Image.open("\images\multiframe\coin_frame7.png"),
                                        size=(650,270))
    
    coin_anim = ctk.CTkLabel(rootcoin, text=None, image=None)
    coin_anim.place(x=0, y=0) # Animation picture

    # Quotes (not really relevant but cool to put in)
    quotes = {
1:"Lucky or not?",
2:"Heads or tails...?",
3:"You pulled a...",
4:"Placing my bets on tails",
5:"Placing my bets on heads",
6:"This reminds me of the hit game, ULTRAKILL",
7:"You got...",
8:"Where did this coin come from anyways?",
9:"Nice coin flip by the way!",
10:"This coin isn't real by the way",
11:"There's no such thing as a 'tie' by the way",
12:"Heads and tails are mutually exclusive by the way",
13:"Red VS blue type of deal",
14:"You reckon this coin could cost like 2 quid?",
15:"I wonder where this concept of Heads & Tails came from..."
}

    inspirational_quote = ctk.CTkLabel(rootcoin, text=None,
                                       font=("Montserrat italic", 20),
                                       text_color="grey35", justify="center",
                                       width=650) 
    misc() # This is just a cool quote I put while the animation is playing

    # Result widgets
    resulticon = ctk.CTkLabel(rootcoin, text=None, image=None)
    resultlabel = ctk.CTkLabel(rootcoin, text=None, font=("Montserrat bold", 105))

    rootcoin.attributes("-topmost", True)
    coin_anim.after(100, lambda: animation(frame=1))

norepeat_dice = 0
def evaluate2_m(): # Outputs the dice's value
    # Error handling
    try: # Checks if the value of outcomes is not 0 or less, or over 1000
         # or "makes sense"
        probability = int(eval(re.sub(r"(\d)([a-zA-Z])", r"\1*\2", outcome_input.get())))
        if probability >= 1001:
            messagebox.showerror("Error",("""[Math ERROR]
There is a limit of up to 1000 possible outcomes"""))
            return
        elif probability == 0:
            messagebox.showerror("Error",("""[Math ERROR]
You cannot have 0 possible outcomes"""))
            return
        else:
            randint(1, probability)
    except:
        messagebox.showerror("Error",("""[Syntax ERROR]
The calculator couldn't process the provided value. Try:
• Checking if the value is correct
• No extranous values is entered"""))
        return    
    global rootdice
    
    try: # Prevents duplicate windows
        if rootdice.winfo_exists():
            return
    except:
        pass
    rootdice = ctk.CTkToplevel()
    rootdice.geometry("650x300+128+130")
    rootdice.title("Rolling the dice...")
    rootdice.resizable(0,0)

    def animation(frame): # Opens a new window and plays the animation and shows
        global norepeat_dice # the result
        resulticon.place_forget()
        resultlabel.place_forget()
        restart_diceimg = ctk.CTkImage(Image.open("\images\crestart_disabled.png"))
        restart_dice.configure(image=restart_diceimg, hover_color="grey12",
                               state="disabled")
        dice_anim.place(x=0,y=0)
        if frame == 1:
            while True: # Prevents quotes from being repeated 2 times
                quote = randint(1,10)
                if quote == norepeat_dice:
                    continue
                else:
                    norepeat_dice = quote
                    inspirational_quote.configure(text=quotes[quote])
                    break
        inspirational_quote.place(x=0, y=270)

        # Animation frames
        if frame == 1: # Frame 1
            dice_anim.configure(image=dice_animimg_frame1)
            dice_anim.after(600, lambda: animation(frame=2))
        elif frame == 2: # Frame 2
            dice_anim.configure(image=dice_animimg_frame2)
            dice_anim.after(600, lambda: animation(frame=3))
        elif frame == 3: # Frame 3
            dice_anim.configure(image=dice_animimg_frame3)
            dice_anim.after(600, lambda: animation(frame=4))
        elif frame == 4: # Frame 4
            dice_anim.configure(image=dice_animimg_frame4)
            dice_anim.after(600, lambda: animation(frame=5))
        elif frame == 5: # Frame 5
            dice_anim.configure(image=dice_animimg_frame5)
            dice_anim.after(1700, showresult)

    def showresult(): # Shows the outcome
        dice_anim.place_forget()
        inspirational_quote.place_forget()

        outcome = str(randint(1, probability)) # outcome
        resultlabel.configure(text=outcome) # text outcome
        resultlabel.place(x=330,y=60)
        resulticon.place(x=30,y=50)

        restart_diceimg = ctk.CTkImage(Image.open("\images\crestart.png"))
        restart_dice.configure(image=restart_diceimg, hover_color="grey26",
                               state="normal") # Allows the user to roll the dice
                                               # Enabled setting


    def misc():
        global restart_dice
        miscbox = ctk.CTkLabel(rootdice, # an area for misc buttons
                                height=88, width=100, text=None,
                                fg_color="grey12", corner_radius=8)
        miscbox.place(x=605,y=196)

        closewindow = ctk.CTkButton(rootdice, image=close_windowimg,
                                height=40, width=40, text=None,
                                fg_color="grey12", hover_color="red4", corner_radius=0,
                                command=rootdice.destroy)
        closewindow.place(x=608,y=240) # Closes the result window

        restart_diceimg = ctk.CTkImage(Image.open("\images\crestart_disabled.png"))
        restart_dice = ctk.CTkButton(rootdice, image=restart_diceimg, # Roll the dice again
                        height=40, width=40, text=None, state="disabled",
                        fg_color="grey12", hover_color="grey12", corner_radius=0,
                        command=lambda: animation(frame=1))
        restart_dice.place(x=608, y=200)
    
    # Animation frames/images
    # Each frame is denoted by it's number. After the a set amount of time, the frame
    # is changed to another frame by +1
    dice_animimg_frame1 = ctk.CTkImage(Image.open("\images\multiframe\dice_frame1.png"),
                                        size=(650,270))
    dice_animimg_frame2 = ctk.CTkImage(Image.open("\images\multiframe\dice_frame2.png"),
                                        size=(650,270))
    dice_animimg_frame3 = ctk.CTkImage(Image.open("\images\multiframe\dice_frame3.png"),
                                        size=(650,270))
    dice_animimg_frame4 = ctk.CTkImage(Image.open("\images\multiframe\dice_frame4.png"),
                                        size=(650,270))
    dice_animimg_frame5 = ctk.CTkImage(Image.open("\images\multiframe\dice_frame5.png"),
                                        size=(650,270))
    
    dice_anim = ctk.CTkLabel(rootdice, text=None, image=None)
    dice_anim.place(x=0, y=0)

    # Quote (also not necessary but cool to put in)
    quotes = {
1:"Lucky or not?",
2:"Out of all the possible outcomes, you got...",
3:"You rolled a...",
4:"Did you know? This dice can have 1000 outcomes",
5:"This dice is a fair dice by the way",
6:"This dice isn't biased by the way",
7:"Who is tossing this dice anyways?",
8:"Where did this dice even come from?",
9:"Lucky numbers here?",
10:"Unlucky numbers here?",
}

    inspirational_quote = ctk.CTkLabel(rootdice, text=None,
                                       font=("Montserrat italic", 20),
                                       text_color="grey35", justify="center",
                                       width=650) 
    misc()

    # Result widgets
    resulticonimg = ctk.CTkImage(Image.open("\images\dice_result.png"), size=(270,200))
    resulticon = ctk.CTkLabel(rootdice, text=None, image=resulticonimg)
    resultlabel = ctk.CTkLabel(rootdice, text=None, font=("Montserrat bold", 105))

    rootdice.attributes("-topmost", True)
    dice_anim.after(100, lambda: animation(frame=1)) # Starts the animation upon
                                                     # opening this window

coinsetting = ctk.StringVar(value="fair")
dicesetting = ctk.StringVar(value="templates")
changeview_m = tk.IntVar(value="0")

# Coin Toss
coiniconONimg = ctk.CTkImage(Image.open("\images\coinon.png"), size=(100,100))
coiniconON = ctk.CTkLabel(box, text=None, image=coiniconONimg) # Icon image
                                                                   # on

coiniconOFFimg = ctk.CTkImage(Image.open("\images\coinoff.png"), size=(100,100))
coiniconOFF = ctk.CTkLabel(box, text=None, image=coiniconOFFimg) # Icon image
                                                                     # off
coiniconOFF.place(x=15, y=80)

coinoption = ctk.CTkRadioButton(box, text="Coin Toss", command=mathbox_rearrange,
                                variable=changeview_m, value="1", font=("segoe ui bold", 21),
                                fg_color="deepskyblue4")
coinoption.place(x=5, y=180) # Switch to the coin option

# Dice Roll

diceiconONimg = ctk.CTkImage(Image.open("\images\diceon.png"), size=(80,80))
diceiconON = ctk.CTkLabel(box, text=None, image=diceiconONimg) # Icon image
                                                                   # on

diceiconOFFimg = ctk.CTkImage(Image.open("\images\diceoff.png"), size=(80,80))
diceiconOFF = ctk.CTkLabel(box, text=None, image=diceiconOFFimg) # Icon image
                                                                     # off
diceiconOFF.place(x=25, y=230)

diceoption = ctk.CTkRadioButton(box, text="Dice Roll", command=mathbox_rearrange,
                                variable=changeview_m, value="2", font=("segoe ui bold", 21),
                                fg_color="deepskyblue4")
diceoption.place(x=5, y=320) # Switch to the dice option

# ---

mathbox_line = ctk.CTkLabel(box, text=None, fg_color="white", width=1, height=400, 
                         corner_radius=1)
mathbox_line.place(x=143, y=75) # A white line, again

# ---

# None

mathbox_label = ctk.CTkLabel(box, text="Choose a mode...", font=("segoe ui bold", 50))
mathbox_label.place(x=225,y=170) # Prompts the user for a selection of "Coin Toss" or 
                                                                        # "Dice Roll"

# Coin

heads_label = ctk.CTkLabel(box, text="P | Heads", font=("STIX Two Text italic", 37)) # Text
heads_input = ctk.CTkEntry(box, font=("Noto Sans Math", 40), fg_color="grey14",
                           border_color="grey14", width=180) # Entry
heads_p = ctk.CTkLabel(box, text="%", font=("Noto Sans Math", 25)) # Measure label


tails_label = ctk.CTkLabel(box, text="P | Tails", font=("STIX Two Text italic", 37)) # Text
tails_input = ctk.CTkEntry(box, font=("Noto Sans Math", 40), fg_color="grey14",
                           border_color="grey14", width=180) # Entry
tails_p = ctk.CTkLabel(box, text="%", font=("Noto Sans Math", 25)) # Measure label
heads_input.bind("<KeyRelease>", autoprob_heads)
tails_input.bind("<KeyRelease>", autoprob_tails)

biasedcoin = ctk.CTkCheckBox(box, text=" Biased\n Coin", fg_color="deepskyblue4",
                            font=("segoe ui bold", 35), hover_color="deepskyblue4",
                            variable=coinsetting, onvalue="biased", offvalue=
                            "fair", checkbox_width=35, checkbox_height=35,
                            command=biased_setting) # Checkbox for turning on biased
                                                                              # coin

coin5050img = ctk.CTkImage(Image.open("\images\coin5050.png"), size=(150,150))
coin5050 = ctk.CTkLabel(box, text=None, image=coin5050img) # 50/50 coin icon

coinbiasedimg = ctk.CTkImage(Image.open("\images\coinbiased.png"), size=(150,150))
coinbiased = ctk.CTkLabel(box, text=None, image=coinbiasedimg) # biased coin icon

clear_mimg = ctk.CTkImage(Image.open("\images\clear.png"), size=(25,25))
clear_m = ctk.CTkButton(box, image=clear_mimg, # Clears the two entry boxes
                        height=48, width=110, text_color="red2", text=None,
                        fg_color="grey14", border_color="red2", hover_color="red4",
                        border_width=2, command=coinclear)

bksp_mimg = ctk.CTkImage(Image.open("\images\down.png"), size=(25,25))
bksp_m = ctk.CTkButton(box, image=bksp_mimg, text=None, # Entry backspace
                       hover_color="red4", fg_color="grey14", height=48, width=170,
                       border_color="deepskyblue4", border_width=2, 
                       command=backspace_m)

execute_mimg = ctk.CTkImage(Image.open("\images\coin_eval.png"), size=(57,57))
execute_m = ctk.CTkButton(box, image=execute_mimg, text=None, height=48,
                          width=285, fg_color="deepskyblue4",
                          command=evaluate_m)
# Tosses the coin to either output "heads" or "tails" based on the
# probability

# Dice

outcome_label = ctk.CTkLabel(box, text="Sides", font=
                             ("STIX Two Text italic", 23)) # Text
outcome_input = ctk.CTkEntry(box, font=("Noto Sans Math", 25), width=75, border_color=
                            "grey17", fg_color="grey17", text_color="grey30") 
outcome_input.insert(ctk.END, "0")
outcome_input.configure(state="disabled")
outcome_input.bind("<KeyRelease>", updateslider)
# Entry/display of possible outcome

outcome_slider = ctk.CTkSlider(box, from_=1, to=1000, command=updateoutcome, progress_color=
                               "deepskyblue4", width=400, height=20) # Custom slider

dicetemplate_3img = ctk.CTkImage(Image.open("\images\card3.png"), size=(60,60))
dicetemplate_3 = ctk.CTkButton(box, image=dicetemplate_3img, text="3 | 33⅓%",
                                  font=("segoe ui bold", 22), fg_color="grey17", border_color=
                                  "deepskyblue4", hover_color="dodgerblue4", border_width=2,
                                  command=lambda: setoutcome(preset=3))
# Inserts 3 possible outcomes

dicetemplate_6img = ctk.CTkImage(Image.open("\images\dice6.png"), size=(60,60))
dicetemplate_6 = ctk.CTkButton(box, image=dicetemplate_6img, text="6 | 16⅔%",
                                font=("segoe ui bold", 22), fg_color="grey17", border_color=
                                "deepskyblue4", hover_color="dodgerblue4", border_width=2,
                                command=lambda: setoutcome(preset=6))
# Inserts 6 possible outcomes

dicetemplate_10img = ctk.CTkImage(Image.open("\images\stackof10.png"), size=(60,60))
dicetemplate_10 = ctk.CTkButton(box, image=dicetemplate_10img, text="10 | 10%",
                                font=("segoe ui bold", 22), fg_color="grey17", border_color=
                                "deepskyblue4", hover_color="dodgerblue4", border_width=2,
                                command=lambda: setoutcome(preset=10))
# Inserts 10 possible outcomes                                   # ↑ or 3 or 6 or 100

dicetemplate_100img = ctk.CTkImage(Image.open("\images\card100.png"), size=(60,60))
dicetemplate_100 = ctk.CTkButton(box, image=dicetemplate_100img, text="100 | 1%",
                                font=("segoe ui bold", 22), fg_color="grey17", border_color=
                                "deepskyblue4", hover_color="dodgerblue4", border_width=2,
                                command=lambda: setoutcome(preset=100))
# Inserst 100 possible outcomes

customdice = ctk.CTkCheckBox(box, text=" Custom", fg_color="deepskyblue4",
                            font=("segoe ui bold", 35), hover_color="deepskyblue4",
                            variable=dicesetting, onvalue="custom", offvalue=
                            "templates", checkbox_width=35, checkbox_height=35,
                            command=dice_setting) # Switches to a slider and entry inputs
                                      # for entering a custom number of possible outcomes

clear2_mimg = ctk.CTkImage(Image.open("\images\clear.png"), size=(25,25))
clear2_m = ctk.CTkButton(box, image=clear2_mimg, # Clears the entry box
                        height=48, width=110, text_color="red2", text=None,
                        fg_color="grey14", border_color="red2", hover_color="red4",
                        border_width=2, command=lambda: outcome_input.delete(0, ctk.END))

bksp2_mimg = ctk.CTkImage(Image.open("\images\down.png"), size=(25,25))
bksp2_m = ctk.CTkButton(box, image=bksp2_mimg, text=None, # Entry backspace
                       hover_color="red4", fg_color="grey14", height=48, width=170,
                       border_color="deepskyblue4", border_width=2, 
                       command=backspace2_m)

execute2_mimg = ctk.CTkImage(Image.open("\images\dice_fillwh.png"), size=(57,57))
execute2_m = ctk.CTkButton(box, image=execute2_mimg, text=None, height=48,
                          width=285, fg_color="deepskyblue4", command=evaluate2_m)
# Rolls the dice to output the number of the outcome

def ks_evaluate(event): # When the enter key is pressed
    if tabview.get() == "Calculate":
        execute()

    elif tabview.get() == "Statistics":
        insertdata()
    
    elif tabview.get() == "Graph & Table":
        prompt = changeview_g.get()
        if prompt == 1:
            evaluate_g()
        elif prompt == 2:
            evaluate2_g()
    
    elif tabview.get() == "Math Box":
        prompt = changeview_m.get()
        if prompt == 1:
            evaluate_m()
        elif prompt == 2:
            evaluate2_m()
    
    else:
        pass
root.bind("<Return>", ks_evaluate)

root.bind("<Control-y>", lambda e: tabview.set("Calculate")) # Press Ctrl+Y to switch to calculate
root.bind("<Control-u>", lambda e: tabview.set("Statistics")) #  | ...U for statstics
root.bind("<Control-i>", lambda e: tabview.set("Graph & Table"))#| ...I for Graph & Table
root.bind("<Control-o>", lambda e: tabview.set("Conversion")) #  | etc.
root.bind("<Control-p>", lambda e: tabview.set("Math Box")) #    |

# -----------------------------------------------------------------------------------------
root.mainloop()