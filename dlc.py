import numpy as np
from numpy import median
from astropy.io import fits
from astropy.time import Time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import pylab
import operator

ap,dx,dy=[],[],[]
x_in,y_in=[],[]
ref=5

m='/media/pranitha/backup/Blz_j1222p0413_1/20170103_c/Clean/j1222p413R23_ubfc.mch'
with open(m) as ip:
	f = ip.read().splitlines(True)
	for line in f[0:]:
		row = line.split()
		ap.append(row[0])
		dx.append(float(row[2]))
		dy.append(float(row[3]))
#print(ap)
#print(dx)
#print(dy)

n='coord_shift.dat'
with open(n) as ip:
	f = ip.read().splitlines(True)
	for line in f[1:7]:
		row = line.split()
		x_in.append(float(row[0]))
		y_in.append(float(row[1]))
#print(x_in)
#print(y_in)

for l in range(1):
	apx1,apy1,f1=[],[],[]
	with open(ap[l]) as ip:
		f1 = ip.read().splitlines(True)
		i=3
	for line in f1[4:]:
		row = line.split()
		#print(row)
		if(i%3==0):
			apx1.append(float(row[1]))
			apy1.append(float(row[2]))
		i=i+1
x=np.asarray(apx1)
y=np.asarray(apy1)
delx=x-x_in[0]
dely=y-y_in[0]
#print(delx)


delm_matrix,delem_matrix=[],[]			
f10=open("coord_time.txt","w+")
for l in range(len(ap)):
	f10.write("%s\t"%ap[l])
	apx,apy,apmag2,aperr_mag2,f1=[],[],[],[],[]
	mag2_frame,err_mag2_frame=[],[]
	with open(ap[l]) as ip:
		f1 = ip.read().splitlines(True)
		i,j=3,2
	for line in f1[4:]:
		row = line.split()
		if(i%3==0):
			apx.append(float(row[1]))
			apy.append(float(row[2]))
			apmag2.append(float(row[4]))
		if(j%3==0):
			aperr_mag2.append(float(row[4]))
		i=i+1
		j=j+1
	apx = np.asarray(apx)
	apx_correct=apx+dx[l]
	apy = np.asarray(apy)
	apy_correct=apy+dy[l]
	apmag2 = np.asarray(apmag2)
	aperr_mag2 = np.asarray(aperr_mag2)
	distance1=((apx_correct-x_in[ref])**2+(apy_correct-y_in[ref])**2)**0.5
	#print(distance1)
	#print(min(distance1))
	min_index1, min_value = min(enumerate(distance1), key=operator.itemgetter(1))
	#print(min_index1)
	#print('%f,%f'%(x_in[ref],y_in[ref]))
	#print('%f,%f'%(apx_correct[min_index1],apy_correct[min_index1]))
	mag_ref=apmag2[min_index1]
	emag_ref=aperr_mag2[min_index1]
	#print(mag_ref)
	delm,delem=[],[]
	for k in range(len(apx1)):
		distance=((apx_correct-apx1[k])**2+(apy_correct-apy1[k])**2)**0.5
		min_index, min_value = min(enumerate(distance), key=operator.itemgetter(1))
		mag2_frame.append(apmag2[min_index])
		err_mag2_frame.append(aperr_mag2[min_index])
		delm.append(mag2_frame[-1]-mag_ref)
		f10.write("%f\t"%delm[-1])
		delem.append(((err_mag2_frame[-1])**2+(emag_ref)**2)**0.5)
	#print(ap[l])	
	#print(x)
	#print(y)	
	#print('mag2_frame = ',mag2_frame)
	#print('err_mag2_frame =',err_mag2_frame)
	delm_matrix.append(delm)
	delem_matrix.append(delem)
	f10.write("\n")	
#print('delm=',(delm_matrix))

#time calculation
fit_list,time_jd,time_ut=[],[],[]
with open('bfct_list.txt') as ip:
	m=ip.read().splitlines(True)
	for line in m[0:]:
		row = line.split()
		fit_list.append(row[0])
		with fits.open(fit_list[-1]) as hdul:
			date_obs=hdul[0].header['DATE-OBS']
			#print(date_obs)
			a=list(date_obs)
			#print(a)
			hr=int(a[11]+a[12])
			if(hr==0):
				hr=24
			mn=int(a[14]+a[15])
			se=int(a[17]+a[18])
			exptime=(hdul[0].header['EXPTIME'])
			#print(exptime)
			exptime_inday=(exptime/3600)/24.0
			#t = Time(date_obs, format='iso', scale='utc')
			#jd=t.mjd-exptime_inday*0.5
			ut=hr+mn/60+se/3600-exptime*0.5/3600
			#print(jd)
			#time_jd.append(jd)
			time_ut.append(ut)
#print('\n Time_mjd:',time_jd)
#print('\n Time_UT',time_ut)
#print(len(time_ut))

v=0.04
dlc_matrix,t_matrix,err_matrix,med_matrix=[],[],[],[]
alpha,dec,alpha_hr,dec_hr=[],[],[],[]
if(int(len(x)/30)==len(x)/30):
	plots=int(len(x)/30)
else:
	plots=int(len(x)/30)+1
#print(plots)

for h in range(plots):
	a= h*30
	fig = plt.figure()
	#fig.set_size_inches(7185,3841,figsize=(6.195,3.841),dpi=150)
	plt.axis('off')
	fig.subplots_adjust(top=0.965,bottom=0.060,left=0.050,right=0.995,hspace=0.0,wspace=0.140)
	plt.title('J122222.99+041315.95  Date of obs.: 2017-01-03    1.3 DFOT(r)  X=1058.10 Y=949.54')
	for i in range(1,31):
		if(i+a>=len(apx1)+1):
			break
		ax = fig.add_subplot(10,3,i)
		dlc,t,yerr,med=[],[],[],[]
		for j in range(len(delm_matrix)):
			if(delm_matrix[j][i+a-1]>-10 and delm_matrix[j][i+a-1]<10):
				dlc.append(delm_matrix[j][i+a-1])
				#print(delm_matrix[j][i+a-1])
				t.append(time_ut[j])
				yerr.append(delem_matrix[j][i+a-1])
		if(len(dlc)==0):
			dlc=[0]
			t=[20]
			yerr=[0]
		dlc=np.asarray(dlc)
		#print(dlc)
		#print(t)
		m=median(dlc)
		#print(m)
		dlc_less,dlc_more,dlc_med,t_less,t_more,t_med,yerr_less,yerr_med,yerr_more=[],[],[],[],[],[],[],[],[]
		for k in range(len(dlc)):
			if(dlc[k]>m-v and dlc[k]<m+v):
				dlc_med.append(dlc[k])
				t_med.append(t[k])
				yerr_med.append(yerr[k])
		for l in range(len(dlc)):
			med.append(m)	
		alpha.append((12+(22/60)+(22.99/3600))*15+delx[i+a-1]*0.54/3600)
		a_hh=int(alpha[-1]/15)
		a_mm=int((alpha[-1]/15-a_hh)*60)
		a_ss=(((alpha[-1]/15-a_hh)*60)-a_mm)*60
		alpha_hr.append(a_hh*10000+a_mm*100+a_ss)
		dec.append(4+(13/60)+(15.95/3600)+dely[i+a-1]*0.54/3600)
		d_dd=int(dec[-1])
		d_mm=int((dec[-1]-d_dd)*60)
		d_ss=((dec[-1]-d_dd)*60-d_mm)*60
		dec_hr.append(d_dd*10000+d_mm*100+d_ss)
		ax.text(.5,.8,'Id=%d,apx1=%.1f,apy1=%.1f'%(i+a-1,x[i+a-1],y[i+a-1]),horizontalalignment='center',size=7.0,transform=ax.transAxes)
		ax.text(.5,0,'α=%.4f,dec=%.4f,α=%.2f,dec=%.2f'%(alpha[i+a-1],dec[i+a-1],alpha_hr[i+a-1],dec_hr[i+a-1]),horizontalalignment='center',size=7.0,transform=ax.transAxes)
		ax.errorbar(t_med,dlc_med,yerr=yerr_med,fmt='o',markersize=2.0,ecolor= 'g',elinewidth=0.35 , capthick=0.1)		
		ax.plot(t,med,'--',linewidth=0.4)
		ax.set_ylim(m-v-0.1,m+v+0.1)
		plt.xlabel('UT')
		plt.rcParams.update({'font.size': 9.0})
		dlc_matrix.append(dlc)
		t_matrix.append(t)
		err_matrix.append(yerr)
	manager = plt.get_current_fig_manager()
	manager.window.showMaximized()
plt.show()
f10.close()






