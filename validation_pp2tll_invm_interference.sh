#!/usr/bin/bash

###
### reproducing FIG. 9 of 1412.7166
###


### variables
RUNSUFFIX=""
TAGSUFFIX=""
#for TAGSUFFIX in cptx31 ctex1x31 ; do

BARETAG=validation_pp2tll_invm
TAG=${BARETAG}${TAGSUFFIX}
OUTDIR=$TAG


### redirect output to log file
exec >> ${TAG}.log  2>&1


### setup madgraph if the tar.gz file is not present, assumes it is setup already otherwise
PYTHON=python3
VERSION=354
MGLINK=https://github.com/mg5amcnlo/mg5amcnlo/archive/refs/tags/v3.5.4.tar.gz
MGTAR=mg5_v${VERSION}.tar.gz

if [[ ! -f "$MGTAR" ]] ; then

### get MG
date && echo "--- Get madgraph"
wget -O $MGTAR $MGLINK
tar xzf $MGTAR
MGBASE=`tar tzf $MGTAR | grep -m1 'madgraph/$' | sed 's/\/madgraph\///'`
MG="$PYTHON $MGBASE/bin/mg5_aMC"
date && echo "--- Using MG executable: $MG"


### get utilities
date && echo "--- Install utilities"
echo "install ninja
install collier
" > ${OUTDIR}.cmd
time $MG -f ${OUTDIR}.cmd

fi

### MG
MGBASE=`tar tzf $MGTAR | grep -m1 'madgraph/$' | sed 's/\/madgraph\///'`
MG="$PYTHON $MGBASE/bin/mg5_aMC"
date && echo "--- MGBASE: $MGBASE"


### model
MODEL=./TopFCNC4f
RESTRICTION=$TAGSUFFIX
MT=172.5

### only generate if output directory is absent
if [[ ! -d "${OUTDIR}" ]] ; then

### make a restriction
cd $MODEL
$PYTHON ./write_param_card.py
if [[ "$TAGSUFFIX" = "" ]] ; then
sed -i 's/[0-9.e+-]\+ *# *cptx31/0.456846812 # cptx31/' param_card.dat
sed -i 's/[0-9.e+-]\+ *# *ctex1x31/0.874654541 # ctex1x31/' param_card.dat
fi
if [[ "$TAGSUFFIX" = "cptx31" ]] ; then
sed -i 's/[0-9.e+-]\+ *# *cptx31/0.456846812 # cptx31/' param_card.dat
fi
if [[ "$TAGSUFFIX" = "ctex1x31" ]] ; then
sed -i 's/[0-9.e+-]\+ *# *ctex1x31/0.874654541 # ctex1x31/' param_card.dat
fi
mv param_card.dat restrict_${RESTRICTION}.dat
cd $OLDPWD


### generate and output
echo "set acknowledged_v3.1_syntax True --global
import model ${MODEL}-${RESTRICTION}
generate p p > t e+ e- \$\$ t~ QCD=1 QED=1 NP=2 [QCD]
output $OUTDIR" > ${TAG}.cmd
$MG -f ${TAG}.cmd


### set fixed order analysis
cat << EOF > ${OUTDIR}/FixedOrderAnalysis/analysis_HwU_template.f
c
c This file contains the default histograms for fixed order runs: it
c only plots the total rate as an example. It can be used as a template
c to make distributions for other observables.
c
c This uses the HwU package and generates histograms in the HwU/GnuPlot
c format. This format is human-readable. After running, the histograms
c can be found in the Events/run_XX/ directory.
c
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      subroutine analysis_begin(nwgt,weights_info)
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c This subroutine is called once at the start of each run. Here the
c histograms should be declared. 
c
c Declare the histograms using 'HwU_book'.
c     o) The first argument is an integer that labels the histogram. In
c     the analysis_end and analysis_fill subroutines this label is used
c     to keep track of the histogram. The label should be a number
c     starting at 1 and be increased for each plot.
c     o) The second argument is a string that will apear above the
c     histogram. Do not use brackets "(" or ")" inside this string.
c     o) The third, forth and fifth arguments are the number of bis, the
c     lower edge of the first bin and the upper edge of the last
c     bin.
c     o) When including scale and/or PDF uncertainties, declare a
c     histogram for each weight, and compute the uncertainties from the
c     final set of histograms
c
      implicit none
c When including scale and/or PDF uncertainties the total number of
c weights considered is nwgt
      integer nwgt
c In the weights_info, there is an text string that explains what each
c weight will mean. The size of this array of strings is equal to nwgt.
      character*(*) weights_info(*)
c Initialize the histogramming package (HwU). Pass the number of
c weights and the information on the weights:
      call HwU_inithist(nwgt,weights_info)
c declare (i.e. book) the histograms
      call HwU_book(1,'total rate      ', 5,0.5d0,5.5d0)
      call HwU_book(2,'total rate Born ', 5,0.5d0,5.5d0)
      
      call HwU_book(3,'Mepem NLO', 25, 0.d0, 500.d0)
      call HwU_book(4,'Mepem  LO', 25, 0.d0, 500.d0)
      
      return
      end


cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      subroutine analysis_end(dummy)
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c This subroutine is called once at the end of the run. Here the
c histograms are written to disk. Note that this is done for each
c integration channel separately. There is an external script that will
c read the HwU data files in each of the integration channels and
c combines them by summing all the bins in a final single HwU data file
c to be put in the Events/run_XX directory, together with a gnuplot
c file to convert them to a postscript histogram file.
      implicit none
      double precision dummy
      call HwU_write_file
      return                
      end


cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      subroutine analysis_fill(p,istatus,ipdg,wgts,ibody)
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c This subroutine is called for each n-body and (n+1)-body configuration
c that passes the generation cuts. Here the histrograms are filled.
      implicit none
c This includes the 'nexternal' parameter that labels the number of
c particles in the (n+1)-body process
      include 'nexternal.inc'
c This is an array which is '-1' for initial state and '1' for final
c state particles
      integer istatus(nexternal)
c This is an array with (simplified) PDG codes for the particles. Note
c that channels that are combined (i.e. they have the same matrix
c elements) are given only 1 set of PDG codes. This means, e.g., that
c when using a 5-flavour scheme calculation (massless b quark), no
c b-tagging can be applied.
      integer iPDG(nexternal)
c The array of the momenta and masses of the initial and final state
c particles in the lab frame. The format is "E, px, py, pz, mass", while
c the second dimension loops over the particles in the process. Note
c that these are the (n+1)-body particles; for the n-body there is one
c momenta equal to all zero's (this is not necessarily the last particle
c in the list). If one uses IR-safe obserables only, there should be no
c difficulty in using this.
      double precision p(0:4,nexternal)
c The weight of the current phase-space point is wgts(1). If scale
c and/or PDF uncertainties are included through reweighting, the rest of
c the array contains the list of weights in the same order as described
c by the weigths_info strings in analysis_begin
      double precision wgts(*)
c The ibody variable is:
c     ibody=1 : (n+1)-body contribution
c     ibody=2 : n-body contribution (excluding the Born)
c     ibody=3 : Born contribution
c The histograms need to be filled for all these contribution to get the
c physics NLO results. (Note that the adaptive phase-space integration
c is optimized using the sum of the contributions, therefore plotting
c them separately might lead to larger than expected statistical
c fluctuations).
      integer ibody
c local variable
      double precision var

c get the electrons
      integer i, iem, iep
      real*8 getinvm4_2, Mepem
      
      iem=0
      iep=0
      do i=1,nexternal
         if (ipdg(i).eq.11) then
            iem=i
         elseif(ipdg(i).eq.-11) then
            iep=i
         endif
      enddo
      
      if (iem.ne.0 .and. iep.ne.0) then
         Mepem=getinvm4_2(p(0,iem),p(0,iep))
         call HwU_fill(3,Mepem,wgts)
         if (ibody.eq.3) call HwU_fill(4,Mepem,wgts)
      endif
      

c
c Fill the histograms here using a call to the HwU_fill()
c subroutine. The first argument is the histogram label, the second is
c the numerical value of the variable to plot for the current
c phase-space point and the final argument is the weight of the current
c phase-space point.
      var=1d0
c always fill the total rate
      call HwU_fill(1,var,wgts)
c only fill the total rate for the Born when ibody=3
      if (ibody.eq.3) call HwU_fill(2,var,wgts)
      return
      end



      function getinvm(en,ptx,pty,pl)
      implicit none
      real*8 getinvm,en,ptx,pty,pl,tiny,tmp
      parameter (tiny=1.d-5)
c
      tmp=en**2-ptx**2-pty**2-pl**2
      if(tmp.gt.0.d0)then
        tmp=sqrt(tmp)
      elseif(tmp.gt.-tiny)then
        tmp=0.d0
      else
        write(*,*)'Attempt to compute a negative mass'
        stop
      endif
      getinvm=tmp
      return
      end


      function getinvm4_2(p1,p2)
      implicit none
      real*8 getinvm4_2,p1(0:3),p2(0:3),p(0:3)
      real*8 getinvm
      integer i
      do i=0,3
         p(i)=p1(i)+p2(i)
      enddo
      getinvm4_2=getinvm(p(0),p(1),p(2),p(3))
      return
      end

EOF

fi


### launch


for II in 1 2 3 ; do

### red line
if [[ "$II" -eq "1" ]] ; then
#if [[ "$TAGSUFFIX" = "cptx31" ]] ; then
CPHIU=1  # extra factor of 1/2 normalisation
CEU=1e-5
fi

# blue line
if [[ "$II" -eq "2" ]] ; then
#if [[ "$TAGSUFFIX" = "ctex1x31" ]] ; then
CPHIU=1e-5
CEU=1
fi


## green line
if [[ "$II" -eq "3" ]] ; then
CPHIU=1
CEU=1
fi


RUNNAME=run_${CPHIU}_${CEU}${RUNSUFFIX}

### only run if results do not exist yet
if [[ ! -f "${OUTDIR}/Events/$RUNNAME/MADatNLO.HwU" ]] ; then

echo "--- can't find ${OUTDIR}/Events/$RUNNAME/MADatNLO.HwU"

echo "launch $OUTDIR -n $RUNNAME
fixed_order=ON
order=NLO
done
set cptx31          $CPHIU
set ctex1x31        $CEU
set aewm1           127.9          # input parameters from the paper
set as              0.10767
set MZ              91.1876
set gf              1.16637e-5
set fixed_ren_scale True           # central scales are fixed to MT
set fixed_fac_scale True
set MT              $MT
set muR_ref_fixed   $MT
set muF_ref_fixed   $MT
set mll_sf          0              # remove default cut
set req_acc_fo      0.005          # increase default accuracy
0" > ${TAG}.cmd

$MG -f ${TAG}.cmd

fi

done



### get histogram information
date && echo "--- Get histogram information"
VARIOUS=$MGBASE/madgraph/various
PYCODE="import sys, glob
import numpy as np
import matplotlib.pyplot as plt
here = '$VARIOUS/'
if here not in sys.path:
    sys.path.append(here)
import histograms as hist

def plot(x,y,fmt=None,**args):
    X = x
    Y = y.repeat(2)
    if fmt:
        return plt.plot(X,Y,fmt,**args)
    else:
        return plt.plot(X,Y,**args)

def plotfill(x,y,z,**args):
    X = x
    Y = y.repeat(2)
    Z = z.repeat(2)
    return plt.fill_between(X,Y,Z,linewidth=0,**args)

# loop over histogram files
histname  = 'Mepem NLO'
for fname in sorted(glob.glob('${BARETAG}*/Events/run_*/MADatNLO.HwU')):
    print(fname)
    file = hist.HwUList(fname)
    cphiu, ceu = fname.split('/')[-2].split('_')[1:3]
    for name in file.get_hist_names():
        if histname not in name:
            continue
        
        h = file.get(name)
        x = np.array([bb for b in h.bins for bb in b.boundaries])
        y = np.array( h.get('central') )
        scales  = np.array([h.get(entry) for entry in file.get_wgt_names()
            if entry[0] == 'scale_adv' and entry[2] in [0.5,1,2] and entry[3] in [0.5,1,2] ])
        
        u = np.max( scales, axis=0 )
        d = np.min( scales, axis=0 )
        e = np.array(h.get('stat_error'))
        
        fac = 1e3/20.                  # to femtobarns, per 20 GeV bin
#       p = plot(x,y*fac, label='\$c_{\\\varphi t}^{(31)}=%s, c_{te}^{(1,31)}=%s\$'%(cphiu,ceu))
        p = plot(x,y*fac, label=fname.split('/')[-2])
        plotfill(x,u*fac,d*fac, color=p[0].get_color(), alpha=.3)
        plotfill(x,(y+e)*fac,(y-e)*fac, color='black', alpha=.4)
        
        print(x)
        print(y*fac)
        
plt.yscale('log')
plt.ylim(1e-3,10)
plt.xlim(0,500)
plt.legend(loc='upper right')
plt.xlabel('\$m_{e^+e^-}\$ [GeV]')
plt.ylabel('\$d\\sigma(p p \\\to t e^+e^-)/dm_{e^+e^-}\$ [fb/GeV] at \$\\sqrt{s}=13\$ TeV')
plt.savefig('${BARETAG}.pdf')
#plt.show()
"
$PYTHON -c "$PYCODE"

### expected results are:
#
#	validation_pp2tll_invm/Events/run_1_1/MADatNLO.HwU
#	[  0.  20.  20.  40.  40.  60.  60.  80.  80. 100. 100. 120. 120. 140.
#	 140. 160. 160. 180. 180. 200. 200. 220. 220. 240. 240. 260. 260. 280.
#	 280. 300. 300. 320. 320. 340. 340. 360. 360. 380. 380. 400. 400. 420.
#	 420. 440. 440. 460. 460. 480. 480. 500.]
#	[0.0023771  0.00877855 0.02198472 0.07748426 1.87069225 0.04026298
#	 0.01414664 0.01817481 0.02352766 0.02954039 0.03452312 0.03865846
#	 0.0435529  0.04640111 0.04978555 0.05196215 0.05516975 0.05644454
#	 0.05846014 0.05961148 0.06074369 0.06088169 0.06073713 0.06304942
#	 0.06263917]
#	validation_pp2tll_invm/Events/run_1_1e-5/MADatNLO.HwU
#	[  0.  20.  20.  40.  40.  60.  60.  80.  80. 100. 100. 120. 120. 140.
#	 140. 160. 160. 180. 180. 200. 200. 220. 220. 240. 240. 260. 260. 280.
#	 280. 300. 300. 320. 320. 340. 340. 360. 360. 380. 380. 400. 400. 420.
#	 420. 440. 440. 460. 460. 480. 480. 500.]
#	[ 5.59162350e-04  2.10614180e-03  6.66338800e-03  4.13880800e-02
#	  1.84433525e+00  6.74730450e-02  1.22158375e-02  5.20636000e-03
#	  2.21133980e-03  1.86721015e-03  1.03403855e-03  6.18545500e-04
#	  9.49411100e-04  3.80928290e-04  1.11944655e-03  4.84836400e-04
#	  7.01225700e-04  5.89135450e-04 -2.23796600e-04  3.34080700e-04
#	  4.24282150e-04  3.71218000e-04  4.10916000e-04  1.29468850e-04
#	  1.46721800e-04]
#	validation_pp2tll_invm/Events/run_1e-5_1/MADatNLO.HwU
#	[  0.  20.  20.  40.  40.  60.  60.  80.  80. 100. 100. 120. 120. 140.
#	 140. 160. 160. 180. 180. 200. 200. 220. 220. 240. 240. 260. 260. 280.
#	 280. 300. 300. 320. 320. 340. 340. 360. 360. 380. 380. 400. 400. 420.
#	 420. 440. 440. 460. 460. 480. 480. 500.]
#	[0.00072082 0.00258347 0.00635783 0.01002966 0.01481502 0.01891547
#	 0.02301854 0.02784683 0.03317711 0.0368584  0.04262262 0.04611158
#	 0.04856139 0.05174995 0.05430263 0.05645853 0.05845971 0.05984913
#	 0.0611262  0.06222771 0.06297284 0.06382676 0.06415142 0.06458629
#	 0.06469553]
