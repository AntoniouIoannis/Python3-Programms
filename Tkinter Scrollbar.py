from tkinter import *
Macedonia = Tk()

scrollbarY = Scrollbar(Macedonia, orient='vertical', width=20)
scrollbarY.pack(side='right', fill='y')
scrollbarX = Scrollbar(Macedonia, orient='horizontal', width=20)
scrollbarX.pack(side='bottom', fill='x')

truth = Text(Macedonia, width=100, height=50, pady=10, padx=10, wrap='none',
                yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)

for i in range(30):
    truth.insert(END, 'Macedonia is Greek!!!\n\tMacedonia\nGreek: Μακεδονία\nMakedonía  is a geographic and former '
                         'administrative region of Greece, in the southern Balkans. Macedonia is the largest and '
                         'second-most-populous Greek geographic region, with a population of 2.36 million in 2020. '
                         'It is highly mountainous, with most major urban centres such as Thessaloniki and Kavala being'
                         'concentrated on its southern coastline. Together with Thrace, and sometimes also Thessaly and'
                         'Epirus, it is part of Northern Greece. Macedonia encompasses entirely the southern part of '
                         'the wider region of Macedonia, making up 51% of the total area of that region. '
               
                         '\n\tMacedonia incorporates most of the territories of ancient Macedon, a kingdom ruled by the'
                         'Argeads, whose most celebrated members were Alexander the Great and his father Philip II. '
                         'Before the expansion of Macedonia under Philip in the 4th century BC, the kingdom of the '
                         'Macedonians covered anarea corresponding roughly to the administrative regions of Western '
                         'and Central Macedonia in modern Greece.')

truth.pack(side='top', fill='both')

scrollbarY.config(command=truth.yview)
scrollbarX.config(command=truth.xview)

Macedonia.mainloop()
