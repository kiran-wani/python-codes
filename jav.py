#running the javelin code in easy mode
from javelin.zylc import get_data
from javelin.lcmodel import Cont_Model, Pmap_Model, Rmap_Model
c=get_data(["continuum.txt"])
cm=Cont_Model(c)
cm.do_mcmc(nwalkers=1000, nburn=200, nchain=100)

cy=get_data(["continuum.txt", "hb.txt"])
cym=Pmap_Model(cy)
cym.do_mcmc(conthpd=cm.hpd,nwalkers=1000, nburn=200, nchain=100)
cym.show_hist()
cym.get_hpd()
cymhpd=cym.hpd

par_best=cymhpd[1,:]
cym_best=cym.do_pred(par_best)
cym_best.plot(set_pred=True, obs=cy)
