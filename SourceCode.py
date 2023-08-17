from tkinter import *
from tkinter import messagebox
import sqlite3
import random
from PIL import ImageTk,Image #This library needs to be installed via pip
root=Tk()
root.iconbitmap("c:/users/USER/Desktop/New Folder/icon2.ico")
root.title('Raghav Shankar Bank')
global wb
global nb
global index
global noticelabel
global indx
global bnext1
global k
k=0


#create a database
'''conn=sqlite3.connect('bankman.db')
c=conn.cursor()
c.execute("""CREATE TABLE member(
name text,
password text,
gender text,
mobno text,
adhaarno text,
acctype text,
paisalaaya text,
accountno text
)




	""")
conn.commit()
#close the connection
conn.close()
'''


cp1=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c1.jpg"))
cp2=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c2.jpg"))
cp3=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c3.jpg"))
cp4=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c4.jpg"))
cp5=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c5.jpg"))
cp6=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c6.jpg"))
cp7=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c7.jpg"))
cp8=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c8.jpg"))
cp9=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c9.jpg"))
cp10=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c10.jpg"))
cp11=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c11.jpg"))
cp12=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c12.jpg"))
cp13=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c13.jpg"))
cp14=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c14.jpg"))
cp15=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c15.jpg"))
cp16=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c16.jpg"))
cp17=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c17.jpg"))
cp18=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c18.jpg"))
cp19=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c19.jpg"))
cp20=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c20.jpg"))
cp21=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c21.jpg"))
cp22=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c22.jpg"))
cp23=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c23.jpg"))
cp24=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c24.jpg"))
cp25=ImageTk.PhotoImage(Image.open("c:/users/USER/Desktop/New Folder/c25.jpg"))


im1=Image.open("c:/users/USER/Desktop/New Folder/sharddha.jpg")
im3=Image.open("c:/users/USER/Desktop/New Folder/sukant.jpg")
im4=Image.open("c:/users/USER/Desktop/New Folder/divyanshm.jpg")
im5=Image.open("c:/users/USER/Desktop/New Folder/shreya.jpg")
im6=Image.open("c:/users/USER/Desktop/New Folder/siddharth.jpg")
im7=Image.open("c:/users/USER/Desktop/New Folder/anurag.jpg")
im8=Image.open("c:/users/USER/Desktop/New Folder/aryan.jpg")
im9=Image.open("c:/users/USER/Desktop/New Folder/priyanshu.jpg")
im10=Image.open("c:/users/USER/Desktop/New Folder/prateek.jpg")
im11=Image.open("c:/users/USER/Desktop/New Folder/devarshi.jpg")
im12=Image.open("c:/users/USER/Desktop/New Folder/vipul.jpg")
im13=Image.open("c:/users/USER/Desktop/New Folder/shruti.jpg")
im14=Image.open("c:/users/USER/Desktop/New Folder/hardik.jpg")
im15=Image.open("c:/users/USER/Desktop/New Folder/sneha.jpg")
im16=Image.open("c:/users/USER/Desktop/New Folder/mohnish.jpg")
im17=Image.open("c:/users/USER/Desktop/New Folder/pawan.jpg")
im18=Image.open("c:/users/USER/Desktop/New Folder/utsav.jpg")
im19=Image.open("c:/users/USER/Desktop/New Folder/adnaan.jpg")
im20=Image.open("c:/users/USER/Desktop/New Folder/abhisheky.jpg")
im21=Image.open("c:/users/USER/Desktop/New Folder/adityaj.jpg")
im22=Image.open("c:/users/USER/Desktop/New Folder/khushi.jpg")
im23=Image.open("c:/users/USER/Desktop/New Folder/palak.jpg")
im24=Image.open("c:/users/USER/Desktop/New Folder/kartik.jpg")
im25=Image.open("c:/users/USER/Desktop/New Folder/raghav.jpg")
im26=Image.open("c:/users/USER/Desktop/New Folder/vaibhav.jpg")
im27=Image.open("c:/users/USER/Desktop/New Folder/naveen.jpg")
im28=Image.open("c:/users/USER/Desktop/New Folder/shivani.jpg")
im29=Image.open("c:/users/USER/Desktop/New Folder/jaideep.jpg")
im30=Image.open("c:/users/USER/Desktop/New Folder/eshita.jpg")
im31=Image.open("c:/users/USER/Desktop/New Folder/gaurav.jpg")
im32=Image.open("c:/users/USER/Desktop/New Folder/divyanshg.jpg")
im33=Image.open("c:/users/USER/Desktop/New Folder/vedant.jpg")
im34=Image.open("c:/users/USER/Desktop/New Folder/abhishekr.jpg")
im35=Image.open("c:/users/USER/Desktop/New Folder/ayush.jpg")
im36=Image.open("c:/users/USER/Desktop/New Folder/himanshuy.jpg")
im37=Image.open("c:/users/USER/Desktop/New Folder/uday.jpg")
im38=Image.open("c:/users/USER/Desktop/New Folder/chandra.jpg")
im39=Image.open("c:/users/USER/Desktop/New Folder/ashvani.jpg")
im40=Image.open("c:/users/USER/Desktop/New Folder/adityap.jpg")
im41=Image.open("c:/users/USER/Desktop/New Folder/harshit.jpg")
im42=Image.open("c:/users/USER/Desktop/New Folder/urvij.jpg")
im43=Image.open("c:/users/USER/Desktop/New Folder/ankit.jpg")
im44=Image.open("c:/users/USER/Desktop/New Folder/shivansh.jpg")
im45=Image.open("c:/users/USER/Desktop/New Folder/nishant.jpg")
im46=Image.open("c:/users/USER/Desktop/New Folder/himanshu.jpg")
im47=Image.open("c:/users/USER/Desktop/New Folder/aman.jpg")


rim1=im1.resize((200,200),Image.ANTIALIAS)
rim3=im3.resize((200,200),Image.ANTIALIAS)
rim4=im4.resize((200,200),Image.ANTIALIAS)
rim5=im5.resize((200,200),Image.ANTIALIAS)
rim6=im6.resize((200,200),Image.ANTIALIAS)
rim7=im7.resize((200,200),Image.ANTIALIAS)
rim8=im8.resize((200,200),Image.ANTIALIAS)
rim9=im9.resize((200,200),Image.ANTIALIAS)
rim10=im10.resize((200,200),Image.ANTIALIAS)
rim11=im11.resize((200,200),Image.ANTIALIAS)
rim12=im12.resize((200,200),Image.ANTIALIAS)
rim13=im13.resize((200,200),Image.ANTIALIAS)
rim14=im14.resize((200,200),Image.ANTIALIAS)
rim15=im15.resize((200,200),Image.ANTIALIAS)
rim16=im16.resize((200,200),Image.ANTIALIAS)
rim17=im17.resize((200,200),Image.ANTIALIAS)
rim18=im18.resize((200,200),Image.ANTIALIAS)
rim19=im19.resize((200,200),Image.ANTIALIAS)
rim20=im20.resize((200,200),Image.ANTIALIAS)
rim21=im21.resize((200,200),Image.ANTIALIAS)
rim22=im22.resize((200,200),Image.ANTIALIAS)
rim23=im23.resize((200,200),Image.ANTIALIAS)
rim24=im24.resize((200,200),Image.ANTIALIAS)
rim25=im25.resize((200,200),Image.ANTIALIAS)
rim26=im26.resize((200,200),Image.ANTIALIAS)
rim27=im27.resize((200,200),Image.ANTIALIAS)
rim28=im28.resize((200,200),Image.ANTIALIAS)
rim29=im29.resize((200,200),Image.ANTIALIAS)
rim30=im30.resize((200,200),Image.ANTIALIAS)
rim31=im31.resize((200,200),Image.ANTIALIAS)
rim32=im32.resize((200,200),Image.ANTIALIAS)
rim33=im33.resize((200,200),Image.ANTIALIAS)
rim34=im34.resize((200,200),Image.ANTIALIAS)
rim35=im35.resize((200,200),Image.ANTIALIAS)
rim36=im36.resize((200,200),Image.ANTIALIAS)
rim37=im37.resize((200,200),Image.ANTIALIAS)
rim38=im38.resize((200,200),Image.ANTIALIAS)
rim39=im39.resize((200,200),Image.ANTIALIAS)
rim40=im40.resize((200,200),Image.ANTIALIAS)
rim41=im41.resize((200,200),Image.ANTIALIAS)
rim42=im42.resize((200,200),Image.ANTIALIAS)
rim43=im43.resize((200,200),Image.ANTIALIAS)
rim44=im44.resize((200,200),Image.ANTIALIAS)
rim45=im45.resize((200,200),Image.ANTIALIAS)
rim46=im46.resize((200,200),Image.ANTIALIAS)
rim47=im47.resize((200,200),Image.ANTIALIAS)


dim1=ImageTk.PhotoImage(rim1)
dim3=ImageTk.PhotoImage(rim3)
dim4=ImageTk.PhotoImage(rim4)
dim5=ImageTk.PhotoImage(rim5)
dim6=ImageTk.PhotoImage(rim6)
dim7=ImageTk.PhotoImage(rim7)
dim8=ImageTk.PhotoImage(rim8)
dim9=ImageTk.PhotoImage(rim9)
dim10=ImageTk.PhotoImage(rim10)
dim11=ImageTk.PhotoImage(rim11)
dim12=ImageTk.PhotoImage(rim12)
dim13=ImageTk.PhotoImage(rim13)
dim14=ImageTk.PhotoImage(rim14)
dim15=ImageTk.PhotoImage(rim15)
dim16=ImageTk.PhotoImage(rim16)
dim17=ImageTk.PhotoImage(rim17)
dim18=ImageTk.PhotoImage(rim18)
dim19=ImageTk.PhotoImage(rim19)
dim20=ImageTk.PhotoImage(rim20)
dim21=ImageTk.PhotoImage(rim21)
dim22=ImageTk.PhotoImage(rim22)
dim23=ImageTk.PhotoImage(rim23)
dim24=ImageTk.PhotoImage(rim24)
dim25=ImageTk.PhotoImage(rim25)
dim26=ImageTk.PhotoImage(rim26)
dim27=ImageTk.PhotoImage(rim27)
dim28=ImageTk.PhotoImage(rim28)
dim29=ImageTk.PhotoImage(rim29)
dim30=ImageTk.PhotoImage(rim30)
dim31=ImageTk.PhotoImage(rim31)
dim32=ImageTk.PhotoImage(rim32)
dim33=ImageTk.PhotoImage(rim33)
dim34=ImageTk.PhotoImage(rim34)
dim35=ImageTk.PhotoImage(rim35)
dim36=ImageTk.PhotoImage(rim36)
dim37=ImageTk.PhotoImage(rim37)
dim38=ImageTk.PhotoImage(rim38)
dim39=ImageTk.PhotoImage(rim39)
dim40=ImageTk.PhotoImage(rim40)
dim41=ImageTk.PhotoImage(rim41)
dim42=ImageTk.PhotoImage(rim42)
dim43=ImageTk.PhotoImage(rim43)
dim44=ImageTk.PhotoImage(rim44)
dim45=ImageTk.PhotoImage(rim45)
dim46=ImageTk.PhotoImage(rim46)
dim47=ImageTk.PhotoImage(rim47)



i1=Image.open("c:/users/USER/Desktop/New Folder/rsb.png")
i2=Image.open("c:/users/USER/Desktop/New Folder/mb.png")
rs1=i1.resize((550,550),Image.ANTIALIAS)
rs2=i2.resize((550,550),Image.ANTIALIAS)
np1=ImageTk.PhotoImage(rs1)
np2=ImageTk.PhotoImage(rs2)

'''I am using mutiple lists because i believe that
these are more efficient and extremely easy to edit'''
lname=['shraddha','sukant','divyanshm','shreya','siddharth','anurag','aryan','priyanshu' ,
'prateek','devarshi','vipul','shruti','hardik','sneha','mohnish','pawan','utsav','adnaan','abhisheky',
'adityaj','khushi','palak','kartik','raghav','vaibhav','naveen','shivani','jaideep','eshita','gaurav',
'divyanshg','vedant','abhishekr','ayush','himanshuy','uday','chandra','ashvani','adityap','harshit','urvij','ankit',
'shivansh','nishant','himanshu','aman']


lpass=['sharddha','sukant','divyanshm','shreya','siddharth','anurag','aryan','priyanshu' ,
'prateek','devarshi','vipul','shruti','hardik','sneha','mohnish','pawan','utsav','adnaan','abhisheky',
'adityaj','khushi','palak','kartik','raghav','vaibhav','naveen','shivani','jaideep','eshita','gaurav',
'divyanshg','vedant','abhishekr','ayush','himanshuy','uday','chandra','ashvani','adityap','harshit','urvij','ankit',
'shivansh','nishant','himanshu','aman']



lgend=['f','m','m','f','m','m','m','m','m','m','m','f','m','f','m','m','m','m','m','m','f','f','m','m','m','m','f','m','f','m','m','m',
'm','m','m','m','m','m','m','m','m','m','m','m','m','m']


lacct=['Reccuring Deposit',
'Current',
'Salary',
'Saving',
'Saving',
'Salary',
'Current',
'Salary',
'Current',
'Reccuring Deposit',
'Salary',
'Saving',
'Current',
'Reccuring Deposit',
'Current',
'Salary',
'Reccuring Deposit',
'Reccuring Deposit',
'Current',
'Saving',
'Current',
'Reccuring Deposit',
'Reccuring Deposit',
'Saving',
'Salary',
'Saving',
'Saving',
'Current',
'Salary',
'Current',
'Current',
'Current',
'Saving',
'Saving',
'Salary',
'Saving',
'Reccuring Deposit',
'Reccuring Deposit',
'Saving',
'Reccuring Deposit',
'Current',
'Current',
'Current',
'Salary',
'Saving','Saving']


lacco=[3993083112,
3381965199,
2646489464,
2010877551,
2768895647,
3127723990,
2844833755,
2423604225,
2719686417,
2976644233,
2677918246,
3595189400,
2111285438,
2109717489,
3657440053,
2009468789,
3029686477,
2385198980,
2823130297,
3989452079,
3717428918,
3296512128,
2809548205,
3473407292,
3203717986,
2558558260,
2424322085,
3724818555,
3931201035,
3262583744,
2855856694,
3270826717,
2916669867,
2182716352,
2574907741,
2483381493,
3539372105,
2638374273,
2886895714,
3919315726,
3376321556,
5468567089,
3077658090,
3730593778,
3138868797,
4635345267]


lmobn=[9855961705,
8200902444,
7974248849,
8462027649,
7359005827,
6607283119,
8905446661,
7824994818,
8153794701,
9211128710,
8424964278,
9068081186,
7924977996,
8312394713,
8204884709,
6410286778,
7725189134,
6140845945,
7967848103,
7930142436,
6079388976,
8823235790,
9768732993,
7961019678,
8067973620,
9837928398,
8752482876,
6571512003,
6697607775,
8077804927,
7512556023,
6096618563,
7455048562,
8389416757,
8652920664,
6739645222,
8022378981,
6341707609,
7308357833,
7874112283,
7168756966,
9558848161,
9697787946,
9784630684,
9051906724,
9394003821,
9777898799]

ladhr=[888215322936,
222923933526,
639824044918,
828528007136,
770545479287,
814056753329,
364425700134,
194554041161,
723553101911,
207144395326,
838844270356,
122651057638,
376022899827,
549901343838,
534175865055,
762095597062,
223174067188,
449137560201,
360033528777,
767300578121,
245992168224,
891930769590,
144231377609,
386859109046,
213407727870,
140639836673,
360786883633,
601512558902,
371373403218,
152522714678,
665752905545,
686575544898,
373383277809,
478136432903,
106978749231,
465199239274,
596097370899,
159168096718,
261260578195,
551254893372,
706588384737,
312390880745,
702085559548,
211685123498,
379868985726,
345354564678]


lpics=[dim1,dim3,dim4,dim5,dim6,dim7,dim8,dim9,dim10,dim11,dim12,dim13,dim14,dim15,
dim16,dim17,dim18,dim19,dim20,dim21,dim22,dim23,dim24,dim25,dim26,dim27,dim28,dim29,dim30,
dim31,dim32,dim33,dim34,dim35,dim36,dim37,dim38,dim39,dim40,dim41,dim42,dim43,dim44,dim45,dim46,dim47] 


laccb=[1383224,
1389238,
82164,
1316997,
1472474,
1351636,
1123478,
718584,
25085,
9598,
899923,
707771,
1327544,
140534,
669439,
1149353,
927934,
104855,
1197935,
728552,
1122183,
1190302,
1313967,
988242123,
1017672,
357077,
465315,
159303,
1220531,
987868,
595380,
141661,
91033,
400343,
1136375,
903958,
463984,
984122,
1076266,
494713,
875875,
1338569,
372560,
1201287,
215963,
7666576]


lcapt=[cp1,cp2,cp3,cp4,cp5,cp6,cp7,cp8,cp9,cp10,cp11,cp12,cp13,cp14,cp15,cp16,cp17,cp18,cp19,cp20,cp21,cp22,cp23,cp24,cp25]
lcapans=['4nv3a','xkwdn','br8x6','9m4bp','w9nb4','mcsxh','dt6jx','b4t9s','n8c6h','jn6ts',
'6ar8r','uxp4d','tsms9','6h3t8','459ct','yu4rt','padtc','3jyp4','hwjrc','x8b9a','urvtp',
'hsd5a','hapk3','d4tsh','3m56r']





def signuppage():
	def newacmade(): #here i m gonna append all info of new member in lists

			if(len(nmobn.get())==10 and len(nadha.get())==12 and nname.get()!='' and npass.get()!='' ):
				conn=sqlite3.connect('bankman.db')
				c=conn.cursor()
				c.execute("INSERT INTO member VALUES (:name,:password,:gender,:mobno,:adhaarno,:acctype,:paisalaaya,:accountno)",
					{
					'name':nname.get(),
					'password':npass.get(),
					'gender':gender.get(),
					'mobno':nmobn.get(),
					'adhaarno':nadha.get(),
					'acctype':actype.get(),
					'paisalaaya':acbale.get(),
					'accountno':str(random.randint(200000000000,999999999999))
					} )
				conn.commit()
				#close the connection
				conn.close()
				noticelabel=Label(root,text='Your Info. are saved\n **Have A Good Day**')
				noticelabel.grid(pady=5)
				bnext3.grid_forget()
			else:
				messagebox.showerror('Warning!!','Wrong Information') 
				nnb.grid_forget()
				tqb.grid_forget()
				nname.grid_forget()
				npb.grid_forget()
				npass.grid_forget()
				ngb.grid_forget()
				r1.grid_forget()
				r2.grid_forget()
				r3.grid_forget()
				r4.grid_forget()
				r5.grid_forget()
				r6.grid_forget()
				r7.grid_forget()
				nmobnb.grid_forget()
				nmobn.grid_forget()
				nadrb.grid_forget()
				nadha.grid_forget()
				nactb.grid_forget()
				acbale.grid_forget()
				acbalb.grid_forget()
				bnext3.grid_forget()
				signuppage()

			

	global tqb
	global nnb
	tqb=Label(root,text='***Thanks For Choosing RSB***',font=('BOLD',20))
	tqb.grid(padx=65)
	nnb=Label(root,text='Please Enter Your Name(lower case)')
	nnb.grid(padx=100)
	global nname
	global nmobn
	global npass
	global nadha
	global actype
	global gender
	global acbale
	nname=Entry(root,borderwidth='5')
	nname.grid()
	npb=Label(root,text='Please Enter Your Password(lower case)')
	npb.grid()
	npass=Entry(root,borderwidth='5')
	npass.grid()
	ngb=Label(root,text='Please Select Your Gender')
	ngb.grid()
	gender=StringVar()
	r1=Radiobutton(root,text='Male',variable=gender,value='m')
	r1.grid()
	r2=Radiobutton(root,text='Female',variable=gender,value='f')
	r2.grid()
	r3=Radiobutton(root,text='Rather Not Say',variable=gender,value='n')
	r3.grid()
	nmobnb=Label(root,text='Please Enter Your Mobile Number')
	nmobnb.grid()
	nmobn=Entry(root,borderwidth='5')
	nmobn.grid()
	nadrb=Label(root,text='Please Enter Your Adhaar Number')
	nadrb.grid()
	nadha=Entry(root,borderwidth='5')
	nadha.grid()
	nactb=Label(root,text='Please Select Your Account Type')
	nactb.grid()
	actype=StringVar()
	r4=Radiobutton(root,text='Current a/c',variable=actype,value='Current')
	r4.grid()
	r5=Radiobutton(root,text='Saving a/c',variable=actype,value='Saving')
	r5.grid()
	r6=Radiobutton(root,text='Salary a/c',variable=actype,value='Salary')
	r6.grid()
	r7=Radiobutton(root,text='Recurring Deposit',variable=actype,value='Reccuring Deposit')
	r7.grid()
	acbalb=Label(root,text='Deposit Some Money')
	acbalb.grid()
	acbale=Entry(root,borderwidth='5')
	acbale.grid()
	bnext3=Button(root,text='Proceed',command=newacmade,bg='LIGHT GREEN')
	bnext3.grid()

def profile2():
	wmb.grid_forget()
	wma.grid_forget()
	bnext5.grid_forget()
	tq2.grid_forget()
	cl.grid_forget()
	cimg.grid_forget()
	cal.grid_forget()
	cans.grid_forget()
	bnext4.grid_forget()
	profile()

def profile3():
	dmb.grid_forget()
	dma.grid_forget()
	bnext6.grid_forget()
	tq2.grid_forget()
	cl.grid_forget()
	cimg.grid_forget()
	cal.grid_forget()
	cans.grid_forget()
	bnext4.grid_forget()
	profile()


def moneytaken():
	conn=sqlite3.connect('bankman.db')
	c=conn.cursor()
	c.execute("SELECT *,oid FROM member")
	records=c.fetchall()
	for record in records:
		if(name.get() in record):
			imp=records.index(record)
			break
	index=lname.index(name.get())
	indx=index
	dummy=int(records[imp][6])
	if((wma.get()).isdigit() and (int(wma.get())<=int(records[imp][6]))):
		dummy-=int(wma.get())

		global tq2
		tq2=Label(root,text='Money Withdrawn')
		tq2.grid()
		root.after(1000,profile2)
	else:
		messagebox.showerror('Warning!!','Wrong Amount')
		wmb.grid_forget()
		wma.grid_forget()
		bnext5.grid_forget()
		withdraw()
	c.execute("""UPDATE member SET
		paisalaaya=:paisalaaya
		 WHERE name=:x""",
		{'paisalaaya':str(dummy),
		 'x':name.get()

		}
		)
	conn.commit()
	conn.close()

def moneygiven():
	conn=sqlite3.connect('bankman.db')
	c=conn.cursor()
	c.execute("SELECT *,oid FROM member")
	records=c.fetchall()
	for record in records:
		if(name.get() in record):
			imp=records.index(record)
			break
	index=lname.index(name.get())
	indx=index
	dummy=int(records[imp][6])
	if((dma.get()).isdigit()):
		dummy+=int(dma.get())
		global tq2
		tq2=Label(root,text='Money Deposited')
		tq2.grid()
		root.after(1000,profile3)
	else:
		messagebox.showerror('Warning!!','Wrong Amount')
		dmb.grid_forget()
		dma.grid_forget()
		bnext6.grid_forget()
		deposit()
	c.execute("""UPDATE member SET
		paisalaaya=:paisalaaya
		 WHERE name=:x""",
		{'paisalaaya':str(dummy),
		  'x':name.get()

		}
		)
	conn.commit()
	conn.close()
	
def withdraw():
	memprof.grid_forget()
	memname.grid_forget()
	memgen.grid_forget()
	memmob.grid_forget()
	memadhaar.grid_forget()
	memaccno.grid_forget()
	memacctype.grid_forget()
	memaccbal.grid_forget()
	bfunc1.grid_forget()
	bfunc2.grid_forget()
	global wmb
	global wma
	global bnext5
	wmb=Label(root,text='Enter Amount to be withdrawn')
	wmb.grid()
	wma=Entry(root,borderwidth='5')
	wma.grid()
	bnext5=Button(root,text='Withdraw',command=moneytaken,bg='LIGHT BLUE')
	bnext5.grid()
def deposit():
	memprof.grid_forget()
	memname.grid_forget()
	memgen.grid_forget()
	global dmb
	global dma
	global bnext6
	memmob.grid_forget()
	memadhaar.grid_forget()
	memaccno.grid_forget()
	memacctype.grid_forget()
	memaccbal.grid_forget()
	bfunc1.grid_forget()
	bfunc2.grid_forget()
	dmb=Label(root,text='Enter Amount to be deposited')
	dmb.grid()
	dma=Entry(root,borderwidth='5')
	dma.grid()
	bnext6=Button(root,text='Deposit',command=moneygiven,bg='LIGHT BLUE')
	bnext6.grid()

def profile():
	cl.grid_forget()
	cimg.grid_forget()
	cal.grid_forget()
	cans.grid_forget()
	bnext4.grid_forget()
	global memprof
	global memname
	global memgen
	global memmob
	global memadhaar
	global memaccno
	global memacctype
	global memaccbal
	global bfunc1
	global bfunc2
	global bfunc3
	if (name.get() in lname):
		indx=lname.index(name.get())
		memprof=Label(image=lpics[indx])
		memprof.grid()
	else:
		memprof=Label(image=lpics[7])
		memprof.grid()
	conn=sqlite3.connect('bankman.db')
	c=conn.cursor()
	c.execute("SELECT *,oid FROM member")
	records=c.fetchall()
	for record in records:
		if(name.get() in record):
			imp=records.index(record)
			break
	conn.commit()
	conn.close()
	memname=Label(root,text='Name: '+records[imp][0].capitalize())
	memname.grid()
	memgen=Label(root,text='Gender: '+records[imp][2].capitalize())
	memgen.grid()
	memmob=Label(root,text='Mob. No: '+records[imp][3])
	memmob.grid()
	memadhaar=Label(root,text='Adhaar No: '+records[imp][4])
	memadhaar.grid()
	memaccno=Label(root,text='Account No: '+records[imp][7])
	memaccno.grid()
	memacctype=Label(root,text='Account Type: '+records[imp][5])
	memacctype.grid()
	memaccbal=Label(root,text='Account Balance: '+records[imp][6])
	memaccbal.grid()
	bfunc1=Button(root,text='Withdraw money',command=withdraw,bg='LIGHT BLUE')
	bfunc1.grid(pady=5)
	bfunc2=Button(root,text='Deposit money',command=deposit,bg='LIGHT BLUE')
	bfunc2.grid(pady=5)






def captchaclear():
	def captchaclear2():
		if(cans.get()==lcapans[luck]):
			profile()
		else:
			messagebox.showerror('Warning!!','Wrong Characters')
			cl.grid_forget()
			cimg.grid_forget()
			cal.grid_forget()
			cans.grid_forget()
			bnext4.grid_forget()
			captchaclear()
	global cl
	global cimg
	global cal
	global cans
	global bnext4
	cl=Label(root,text='Complete this and we\'ll take u to your profile' )
	cl.grid()
	luck=random.randint(0,24)
	cimg=Label(image=lcapt[luck])
	cimg.grid()
	cal=Label(root,text='Fill the characters same as above(use lower case)')
	cal.grid()
	cans=Entry(root,borderwidth='5')
	cans.grid()
	bnext4=Button(root,text='Proceed',command=captchaclear2,bg='LIGHT GREEN')
	bnext4.grid()



def delay2(): #for welcoming and asking ques.
	ml.pack_forget()
	q1=messagebox.askquestion('IMPORTANT!!!',"Already a Member?") #the very first and important ques.
	if q1=='yes':
		def passpage():
			conn=sqlite3.connect('bankman.db')
			c=conn.cursor()
			c.execute("SELECT *,oid FROM member")
			records=c.fetchall()
			k=0
			for record in records:
				if(name.get() in record):
					k=1
				else:
					continue
			if(k==1):
		  		def profpage():
		  			conn=sqlite3.connect('bankman.db')
		  			c=conn.cursor()
		  			c.execute("SELECT *,oid FROM member")
		  			records=c.fetchall()
		  			for record in records:
		  				if(name.get() in record):
		  					imp=records.index(record)
		  					break
		  			conn.commit()
		  			conn.close()
		  			if(passw.get() == records[imp][1] and cbx.get()==1):
		  				pb.grid_forget()
		  				passw.grid_forget()
		  				bnext2.grid_forget()
		  				cc.grid_forget()
		  				captchaclear()
		  				#now i m gonna use grid system with fun 
		  				#here we should display profile of candidate  
		  				#but captcha clearing is a must		  				
		  			elif(passw.get() == name.get() and cbx.get()!=1):
		  				messagebox.showerror('Warning!!','You didn\'t select Captcha option' )
		  			else:
		  				messagebox.showerror('Warning!!','Wrong Password')
		  				pb.grid_forget()
		  				passw.grid_forget()
		  				bnext2.grid_forget()
		  				cc.grid_forget()
		  				passpage()
		  		wb.grid_forget()
		  		nb.grid_forget()
		  		name.grid_forget()
		  		bnext1.grid_forget()
		  		pb=Label(root,text='Please Enter Your Password')
		  		pb.grid(padx=20)
		  		global passw
		  		passw=Entry(root,borderwidth='5')
		  		passw.grid(padx=100)
		  		passw.get()
		  		cbx=IntVar()
		  		cc=Checkbutton(root,text='I am not a robot(Captcha)',variable=cbx)
		  		cc.grid()
		  		bnext2=Button(root,text='Proceed',command=profpage,bg='LIGHT GREEN')
		  		bnext2.grid()
			else: #if name is wrong
		  		messagebox.showwarning('Warning!!','This Username Does Not Exist')
		  		q2=messagebox.askquestion('Warning!!',' '''
		  		'''Do You want to re-enter Name? If you choose No,we'll take you to  sign-up page''' )
		  		if(q2=='yes'):
		  			wb.grid_forget()
		  			nb.grid_forget()
		  			name.grid_forget()
		  			bnext1.grid_forget()
		  			delay2() #Here idk why some bug's acting but still it gives better option once again 
		  		else:
		  			wb.grid_forget()
		  			nb.grid_forget()
		  			name.grid_forget()
		  			bnext1.grid_forget()
		  			signuppage()
			conn.commit()
			conn.close()
		wb=Label(root,text='***Welcome***',font=('BOLD',20))
		wb.grid(padx=20)
		nb=Label(root,text='Please Enter Your Name(lower case)')
		nb.grid(padx=100)	
		global name
		name=Entry(root,borderwidth='5')
		name.grid()
		name.get()
		bnext1=Button(root,text='Proceed',command=passpage,bg='LIGHT GREEN')
		bnext1.grid()
	else:
		#here we have to make sign-up page
		signuppage()

def delay1(): #to show made by banner
	ml.config(image=np2)
	ml.after(5000,delay2)
ml=Label(image=np1) #to show rsi banner
ml.pack()
ml.after(5000,delay1)
root.mainloop()