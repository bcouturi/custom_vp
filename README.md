Building a custom Detector
=========================


```
git clone ssh://git@gitlab.cern.ch:7999/lhcb/Detector.git
cd Detector/
lb-project-init 
export LCG_VERSION=97a
lb-set-platform x86_64-centos7-gcc9-opt
make install
cd ..
ln -s Detector Detector_0.1
lb-run --dev-dir=`pwd` --nightly lhcb-gaussino/790 Gauss/Futurev3 gaudirun.py run_gaussino.py 
```

