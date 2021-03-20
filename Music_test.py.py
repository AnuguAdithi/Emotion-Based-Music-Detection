from tkinter import *
import re
from pygame import mixer
import random
mixer.init()
from collections import defaultdict



root=Tk()
root.geometry('600x600')

def getText():
    res=textarea.get("1.0","end-1c")
    #emotion_output=Entry(root,text="")
    d=defaultdict(list)
    happy_l=['happy','happier','enjoying','enjoyed','happiest','enjoy','cheerful','contended','delighted','ecstatic','elated']
    sad_l=['sad','dismal','cry','cried','crying','forgive','forgiveness','calm','heartbroken','meloncholy','mournful','pessimistic','somber','depressed','sorry']
    anger_l=['angry','annoy','hatred','impatience','irritation','temper','violence','rage','enimity']
    fear_l=['fear','frightened','frightening','frighten','terror','panic','panicked','horror','anxiety','suspicion','suspicious','unease','phobia']
    d['happy']=happy_l
    d['sad']=sad_l
    d['anger']=anger_l
    d['fear']=fear_l
    st=res
    st=st.lower()
    l= re.findall(r"[\w']+", st)
    total=len(l)
    hc,sc,ac,fc=0,0,0,0
    for i in range(len(l)):
        if(l[i] in d['happy']):
            print(l[i],'happy')
            hc+=1
        if(l[i] in d['sad']):
            print(l[i],'sad')
            sc+=1
        if(l[i] in d['anger']):
            print(l[i],'anger')
            ac+=1
        if(l[i] in d['fear']):
            print(l[i],'fear')
            fc+=1
    hc_p=(hc/total)*100
    sc_p=(sc/total)*100
    ac_p=(ac/total)*100
    fc_p=(fc/total)*100
    m=max(hc_p,sc_p,ac_p,fc_p)
    print(m)
    ''' if(m==hc_p):
        emotion_output.insert(END,'Happy')
    elif(m==sc_p):
        emotion_output.insert(END,'Sad')
    elif(m==fc_p):
        emotion_output.insert(END,'Fear')
    else:
        emotion_output.insert(END,'Angry')'''
    print(m,hc_p,sc_p,ac_p,fc_p)
    if(m==0):
        emotion_output.insert(END,'Neutral')
        a=['Buttabomma.mp3','friends.mp3','Mari song.mp3','Senorita.mp3','ShapeOfYou.mp3']
        fname=random.choice(a)
        mixer.music.load(fname)
        s=str(radio.get())
        if(s=='1'):
            mixer.music.play()
        if(s=='2'):
            mixer.music.pause()
    elif(m==hc_p):
        emotion_output.insert(END,'Happy')
        b=['Buttabomma.mp3','friends.mp3','Mari song.mp3','Rangamma.mp3','Samajavaragamana.mp3','Senorita.mp3','ShapeOfYou.mp3','takitaki.mp3']
        fname=random.choice(b)
        mixer.music.load(fname)
        s=str(radio.get())
        if(s=='1'):
            mixer.music.play()
        if(s=='2'):
            mixer.music.pause()
        
    elif(m==sc_p):
        emotion_output.insert(END,'Sad')
        c=['Bekhayali.mp3','Emitemitemito.mp3','Give Me Some Sunshine.mp3','Imagine_Dragons_Believer.mp3','Oosupodu.mp3','Undiporaadhey.mp3','Vellipomakey.mp3']
        fname=random.choice(c)
        mixer.music.load(fname)
        s=str(radio.get())
        if(s=='1'):
            mixer.music.play()
        if(s=='2'):
            mixer.music.pause()

    elif(m==fc_p):
        emotion_output.insert(END,'Fear')
        d=['Chal_Chalo.mp3','Give Me Some Sunshine.mp3','Maari_2_Rowdy_Baby.mp3','Nee_Kallalona.mp3','Rangamma.mp3','saddadil.mp3','Vellipomakey.mp3']
        fname=random.choice(d)
        mixer.music.load(fname)
        s=str(radio.get())
        if(s=='1'):
            mixer.music.play()
        if(s=='2'):
            mixer.music.pause()
 
    else:
        emotion_output.insert(END,'Angry')
        e=['Emitemitemito.mp3','Vellipomaake.mp3','Oosupodu.mp3','Maari_2_Rowdy_Baby.mp3','Chal_Chalo.mp3']
        fname=random.choice(e)
        mixer.music.load(fname)
        s=str(radio.get())
        if(s=='1'):
            mixer.music.play()
        if(s=='2'):
            mixer.music.pause()
    
root.configure(bg='lightgoldenrod')
l=Label(text="Your emotion right now!")
textarea=Text(root,height=5,width=52)
btn=Button(root,text="Submit",command=lambda:getText())
emotion_output=Text(root,height=1,width=10)
textarea.pack()
btn.pack()
l.pack()
emotion_output.pack()
radio=IntVar()
lbl=Label(text="Song play")
lbl.pack()
r1=Radiobutton(root,text="Play",variable=radio,value=1,command=getText)
r1.pack()
r2=Radiobutton(root,text="Pause",variable=radio,value=2,command=getText)
r2.pack()
root.mainloop()

