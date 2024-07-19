#!/usr/bin/bash

###
### reproducing FIG. 8 of 1412.7166
###


### variables
RUNSUFFIX=""
TAGSUFFIX=""

BARETAG=validation_ee_tu
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
RESTRICTION=cptx31_ctex1x31
MT=172.5

### only generate if output directory is absent
if [[ ! -d "${OUTDIR}" ]] ; then

### make a restriction
cd $MODEL
$PYTHON ./write_param_card.py
sed -i 's/[0-9.e+-]\+ *# *cptx31/0.456846812 # cptx31/' param_card.dat
sed -i 's/[0-9.e+-]\+ *# *ctex1x31/0.874654541 # ctex1x31/' param_card.dat
mv param_card.dat restrict_${RESTRICTION}.dat
cd $OLDPWD


### generate and output
echo "set acknowledged_v3.1_syntax True --global
import model ${MODEL}-${RESTRICTION}
generate e+ e- > t u~ QCD=0 QED=2 NP=2 [QCD]
output $OUTDIR" > ${TAG}.cmd
$MG -f ${TAG}.cmd

fi

for II in 1 2 3 ; do

### red line
if [[ "$II" -eq "1" ]] ; then
CPHIU=7.6
CEU=0
fi

# blue line
if [[ "$II" -eq "2" ]] ; then
CPHIU=1e-3
CEU=1.27
fi


# green line
if [[ "$II" -eq "3" ]] ; then
CPHIU=7.6
CEU=1.27
fi



# loop over centre-of-mass energies
for SQS in 188 190 192 194 196 198 200 202 204 206 208 ; do

EBEAM=$(( $SQS / 2 ))

#date && echo "--- $SQS $EBEAM"


RUNNAME=run_${CPHIU}_${CEU}_${SQS}

### only run if results do not exist yet
if [[ ! -f "${OUTDIR}/Events/$RUNNAME/MADatNLO.HwU" ]] ; then

echo "--- can't find ${OUTDIR}/Events/$RUNNAME/MADatNLO.HwU"

echo "set web_browser nothing
launch $OUTDIR -n $RUNNAME
fixed_order=ON
order=NLO
done
set cptx31          $CPHIU
set ctex1x31        $CEU
set aewm1           127.9          # input parameters from the paper
set as              0.10767
set MZ              91.1876
set gf              1.16637e-5
set ebeam1          $EBEAM
set ebeam2          $EBEAM
set fixed_ren_scale True           # central scales are fixed to MT
set fixed_fac_scale True
set MT              $MT
set muR_ref_fixed   $MT
set muF_ref_fixed   $MT
set ptj             0              # remove default cut
set req_acc_fo      0.01
0" > ${TAG}.cmd

$MG -f ${TAG}.cmd

fi

done

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

# loop over parameter values
files = glob.glob('$OUTDIR/Events/run_*/MADatNLO.HwU')
files = [file.split('/')[-2].split('_') for file in files if '15.2' not in file]
for cphiu,ceu in sorted(set([(file[1],file[2]) for file in files])):

    # loop over centre-of-mass energies
    xsecs = []
    sqss  = []
    for fname in glob.glob('$OUTDIR/Events/run_{:}_{:}_*/MADatNLO.HwU'.format(cphiu,ceu)):
        
        # get the centre-of-mass energy
        runname = fname.split('/')[-2].split('_')
        sqs = float(runname[-1])
        sqss.append(sqs)
        
        # load histogram file
        file = hist.HwUList(fname)
        
        # get the right histogram
        histname  = 'total rate'
        for name in file.get_hist_names():
            if histname in name and 'Born' not in name:
                h = file.get(name)
        
        # get the histogram content
        x = np.array([bb for b in h.bins for bb in b.boundaries])
        y = np.array( h.get('central') )
        scales  = np.array([h.get(entry) for entry in file.get_wgt_names()
            if entry[0] == 'scale_adv' and entry[2] in [0.5,1,2] and entry[3] in [0.5,1,2] ])
        
        u = np.max( scales, axis=0 )
        d = np.min( scales, axis=0 )
        e = np.array(h.get('stat_error'))
        
        # collect that
        xsecs.append([y[0],u[0],d[0],e[0]])

    # order by centre-of-mass energy, and fix normalisation
    ii = np.argsort(sqss)
    sqss = np.array(sqss)[ii]
    xsecs = np.array(xsecs)[ii].T*1e3*2       # in femtobarns, for tcbar+tbarc
    
    # make the plot
    p = plt.plot(sqss,xsecs[0], label='\$c_{\\\varphi u}^{(3+1)}=%s, c_{eu}^{(1,3+1)}=%s\$'%(cphiu,ceu))
    plt.fill_between(sqss,xsecs[1],xsecs[2], color=p[0].get_color(), linewidth=0, alpha=.5)
    plt.fill_between(sqss,xsecs[0]-xsecs[3],xsecs[0]+xsecs[3], color='black', linewidth=0, alpha=.5)
    
    # output numbers to log
    print(cphiu,ceu)
    print(repr(sqss))
    print(repr(xsecs))

# plot formating
plt.yscale('log')
plt.ylim(25,400)
plt.xlim(188,208)
plt.legend()
plt.xlabel('\$\\sqrt{s}\$')
plt.ylabel('\$2\\\times\\sigma(e^+e^-\\\to t \\\bar{c})\$ [fb]')
plt.savefig('${BARETAG}.pdf')
"
$PYTHON -c "$PYCODE"

### expected results are:
#
#	1e-3 1.27
#	array([188., 190., 192., 194., 196., 198., 200., 202., 204., 206., 208.])
#	array([[4.1837960e+01, 5.2194600e+01, 6.3773560e+01, 7.5764700e+01,
#		8.8668060e+01, 1.0261476e+02, 1.1712066e+02, 1.3205396e+02,
#		1.4806966e+02, 1.6463726e+02, 1.8084332e+02],
#	       [4.2949200e+01, 5.3559240e+01, 6.5421440e+01, 7.7699340e+01,
#		9.0898880e+01, 1.0518198e+02, 1.1998562e+02, 1.3527742e+02,
#		1.5163446e+02, 1.6853652e+02, 1.8508122e+02],
#	       [4.0924660e+01, 5.1073040e+01, 6.2419260e+01, 7.4174680e+01,
#		8.6834640e+01, 1.0050486e+02, 1.1476608e+02, 1.2940474e+02,
#		1.4513992e+02, 1.6143260e+02, 1.7736038e+02],
#	       [7.9571840e-02, 1.0183424e-01, 1.2013624e-01, 1.5364708e-01,
#		1.8051728e-01, 2.2549260e-01, 2.8777360e-01, 3.1235740e-01,
#		3.4472900e-01, 3.9650440e-01, 4.3441960e-01]])
#	7.6 0
#	array([188., 190., 192., 194., 196., 198., 200., 202., 204., 206., 208.])
#	array([[7.14006800e+01, 8.41301600e+01, 9.65819600e+01, 1.08909180e+02,
#		1.20981460e+02, 1.32291920e+02, 1.43195840e+02, 1.53870180e+02,
#		1.63402040e+02, 1.72545980e+02, 1.82270860e+02],
#	       [7.33206200e+01, 8.63363000e+01, 9.90573200e+01, 1.11634100e+02,
#		1.23953920e+02, 1.35470980e+02, 1.46573100e+02, 1.57432640e+02,
#		1.67111420e+02, 1.76394800e+02, 1.86281740e+02],
#	       [6.98227800e+01, 8.23170000e+01, 9.45475800e+01, 1.06669680e+02,
#		1.18538540e+02, 1.29679200e+02, 1.40420220e+02, 1.50942340e+02,
#		1.60353460e+02, 1.69382800e+02, 1.78974480e+02],
#	       [1.19116074e-01, 1.36353980e-01, 1.64173700e-01, 1.87310880e-01,
#		2.15537180e-01, 2.31963400e-01, 2.60209200e-01, 2.79733000e-01,
#		3.06216000e-01, 3.29710000e-01, 3.46152400e-01]])
#	7.6 1.27
#	array([188., 190., 192., 194., 196., 198., 200., 202., 204., 206., 208.])
#	array([[4.13504400e+01, 4.89371600e+01, 5.66754200e+01, 6.44730200e+01,
#		7.21959600e+01, 8.03917800e+01, 8.84361000e+01, 9.64656400e+01,
#		1.05086300e+02, 1.13056880e+02, 1.21339440e+02],
#	       [4.24752400e+01, 5.02276400e+01, 5.81166000e+01, 6.60735400e+01,
#		7.39383200e+01, 8.22858200e+01, 9.04737800e+01, 9.86440400e+01,
#		1.07418480e+02, 1.15486900e+02, 1.23925680e+02],
#	       [4.04260400e+01, 4.78765600e+01, 5.54909800e+01, 6.31576200e+01,
#		7.07640000e+01, 7.88351600e+01, 8.67614200e+01, 9.46753200e+01,
#		1.03169580e+02, 1.11059760e+02, 1.19213900e+02],
#	       [8.88567000e-02, 9.16147000e-02, 1.13637200e-01, 1.47836596e-01,
#		1.72868560e-01, 1.89611840e-01, 2.06028400e-01, 2.24337800e-01,
#		2.44383400e-01, 2.66036600e-01, 2.98113600e-01]])


